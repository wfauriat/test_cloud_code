--[[
monographie.lua — pandoc Lua filter for the monograph (pandoc >= 3.1).

Responsibilities, in pass order:
  1. includes        ::: {.inclure fichier="tableaux/x.md"} ::: is replaced by the parsed file
  2. normalize       display equations labelled {#eq:...}; table captions labelled {#tbl:...};
                     "Points clés" headings made unnumbered
  3. collect         number chapters, sections, figures, tables, equations, propositions,
                     definitions, parts (numbers must match LaTeX's own numbering)
  4. render          the six blocks, statements (with mandatory statut), cross-references
                     (@id, [-@id]), A-VERIFIER markers, missing figures, book structure markers
  5. typography      French spacing (non-breaking spaces before : ; ! ? » % and after «)
  6. parts           LaTeX part pages, each followed by its introduction (environment
                     introductionpartie, gabarit/preambule.tex)

Must run before citeproc (see gabarit/commun.yaml), so that cross-references and
A-VERIFIER markers are never seen as bibliographic citations.
--]]

local stringify = pandoc.utils.stringify
local LATEX = FORMAT:match('latex') ~= nil
local HTML = FORMAT:match('html') ~= nil

local function warn(msg) io.stderr:write('[monographie] ' .. msg .. '\n') end

local function esc(s) -- escape plain text for LaTeX
  s = s:gsub('\\', '\\textbackslash{}')
  s = s:gsub('([{}%$&#_%%])', '\\%1')
  s = s:gsub('%^', '\\^{}'):gsub('~', '\\~{}')
  return s
end

local function inlines_latex(inl) -- render inlines to a LaTeX string
  return pandoc.write(pandoc.Pandoc({ pandoc.Plain(inl) }), 'latex'):gsub('%s+$', '')
end

-- Six signaled blocks: class -> {displayed name, LaTeX environment}
local BLOCS = {
  ['outils']              = { 'Boîte à outils', 'blocoutils' },
  ['formel']              = { 'Noyau formel', 'blocformel' },
  ['exemple-quantitatif'] = { 'Exemple quantitatif', 'blocexemple' },
  ['cas']                 = { 'Étude de cas', 'bloccas' },
  ['nuance']              = { 'Nuance et discussion ouverte', 'blocnuance' },
  ['question']            = { 'Question à se poser', 'blocquestion' },
}
local STATUTS = {
  ['définition'] = true, ['résultat sous hypothèses'] = true,
  ['hypothèse de travail'] = true, ['constat empirique'] = true,
}
-- Reference prefixes handled as cross-references (never as citations)
local PREFIXES = { sec = true, prop = true, def = true, fig = true, tbl = true, eq = true }

local REFS = {}      -- id -> { kind = ..., num = ..., title = ... }
local SANS_NUMERO = {} -- ids of sub-headings of unnumbered chapters (LaTeX must not number them)
PREMIER = nil        -- first chapter number when previewing a single chapter (make chapitre)

-- Keys of candidate (not yet verified) references: their citations are marked with an orange "?"
local A_VERIFIER = {}
do
  local fh = io.open('commun/biblio_a_verifier.bib', 'r')
  if fh then
    for key in fh:read('a'):gmatch('@%w+%s*{%s*([^,%s]+)%s*,') do A_VERIFIER[key] = true end
    fh:close()
  end
end
local STATS = { averifier = 0, refs_manquantes = 0, statuts_manquants = 0, figures_manquantes = 0 }

---------------------------------------------------------------------------
-- 1. Includes
---------------------------------------------------------------------------
local includes = {
  Div = function(d)
    if not d.classes:includes('inclure') then return nil end
    local f = d.attributes['fichier']
    local fh = f and io.open(f, 'r')
    if not fh then
      warn('fichier à inclure introuvable : ' .. tostring(f))
      return pandoc.Div({ pandoc.Para({ pandoc.Str('[Contenu généré manquant : ' .. tostring(f) .. ']') }) },
        { class = 'manquant' })
    end
    local txt = fh:read('a'); fh:close()
    return pandoc.read(txt, 'markdown').blocks
  end,
}

---------------------------------------------------------------------------
-- 2. Normalize
---------------------------------------------------------------------------
local function equations(inl)
  local out, i, changed = pandoc.Inlines {}, 1, false
  while i <= #inl do
    local el = inl[i]
    if el.t == 'Math' and el.mathtype == 'DisplayMath' then
      local j = i + 1
      if inl[j] and inl[j].t == 'Space' then j = j + 1 end
      local s = inl[j]
      local id, rest = nil, nil
      if s and s.t == 'Str' then id, rest = s.text:match('^{#(eq:[%w%-]+)}(.*)$') end
      if id then
        out:insert(pandoc.Span({ el }, { id = id, class = 'equation' }))
        if rest ~= '' then out:insert(pandoc.Str(rest)) end
        i, changed = j + 1, true
        goto continue
      end
    end
    out:insert(el); i = i + 1
    ::continue::
  end
  return changed and out or nil
end

local normalize = {
  Inlines = equations,
  Table = function(t)
    local blocks = t.caption.long
    local last = blocks[#blocks]
    if last and (last.t == 'Plain' or last.t == 'Para') then
      local inl = last.content
      local s = inl[#inl]
      local id = s and s.t == 'Str' and s.text:match('^{#(tbl:[%w%-]+)}$')
      if id then
        inl:remove(#inl)
        if inl[#inl] and inl[#inl].t == 'Space' then inl:remove(#inl) end
        t.identifier = id
        return t
      end
    end
  end,
  Header = function(h)
    if h.classes:includes('points-cles') and not h.classes:includes('unnumbered') then
      h.classes:insert('unnumbered'); h.classes:insert('unlisted'); return h
    end
  end,
}

---------------------------------------------------------------------------
-- 3. Collect numbers (document order)
---------------------------------------------------------------------------
local function roman(n)
  local t = { 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X' }
  return t[n] or tostring(n)
end

local collect = {
  Pandoc = function(doc)
    local chapnum, appx, part = 0, 0, 0
    -- single-chapter preview (make chapitre CH=NN): keep the real chapter number
    local first = doc.meta['premier-chapitre'] and tonumber(stringify(doc.meta['premier-chapitre']))
    if first then chapnum = first - 1; PREMIER = first end
    local chap, sect, fig, tab, eq, prop, def = nil, 0, 0, 0, 0, 0, 0
    local in_appendix = false
    local function define(id, entry)
      if id == nil or id == '' then return end
      if REFS[id] then warn('étiquette en double : ' .. id) end
      REFS[id] = entry
    end
    doc:walk({
      traverse = 'topdown',
      Header = function(h)
        local unnumbered = h.classes:includes('unnumbered')
        if h.level == 1 then
          if h.classes:includes('partie') then
            part = part + 1
            define(h.identifier, { kind = 'partie', num = roman(part) })
            return
          end
          if h.classes:includes('corps') then chapnum = -1 end
          if h.classes:includes('annexes') then in_appendix = true end
          fig, tab, eq, sect = 0, 0, 0, 0
          if unnumbered then
            chap = nil
            define(h.identifier, { kind = 'titre', title = h.content })
          else
            if in_appendix then
              appx = appx + 1; chap = string.char(64 + appx)
              define(h.identifier, { kind = 'annexe', num = chap })
            else
              chapnum = chapnum + 1; chap = tostring(chapnum)
              define(h.identifier, { kind = 'chapitre', num = chap })
            end
          end
        elseif h.level == 2 then
          if not chap and not unnumbered and h.identifier ~= '' then SANS_NUMERO[h.identifier] = true end
          if chap and not unnumbered then
            sect = sect + 1
            define(h.identifier, { kind = 'section', num = chap .. '.' .. sect })
          else
            define(h.identifier, { kind = 'titre', title = h.content })
          end
        elseif h.identifier ~= '' then
          if not chap and not unnumbered then SANS_NUMERO[h.identifier] = true end
          define(h.identifier, { kind = 'titre', title = h.content })
        end
      end,
      Figure = function(f)
        if f.identifier ~= '' then
          fig = fig + 1
          define(f.identifier, { kind = 'figure', num = (chap and chap .. '.' or '') .. fig })
        end
      end,
      Table = function(t)
        if t.identifier ~= '' then
          tab = tab + 1
          define(t.identifier, { kind = 'tableau', num = (chap and chap .. '.' or '') .. tab })
        end
      end,
      Span = function(s)
        if s.classes:includes('equation') then
          eq = eq + 1
          define(s.identifier, { kind = 'equation', num = (chap and chap .. '.' or '') .. eq })
        end
      end,
      Div = function(d)
        if d.classes:includes('proposition') then
          prop = prop + 1
          define(d.identifier, { kind = 'proposition', num = tostring(prop) })
        elseif d.classes:includes('definition') then
          def = def + 1
          define(d.identifier, { kind = 'definition', num = tostring(def) })
        end
      end,
    })
    return nil
  end,
}

---------------------------------------------------------------------------
-- 4. Render
---------------------------------------------------------------------------
local WORD = {
  chapitre = 'chapitre', annexe = 'annexe', section = 'section', partie = 'partie',
  figure = 'figure', tableau = 'tableau', equation = 'équation',
  proposition = 'proposition', definition = 'définition',
}

-- One reference, as inlines. bare = number only (syntax [-@id]).
local function reference(id, bare)
  local r = REFS[id]
  if not r then
    warn('référence non définie : ' .. id)
    STATS.refs_manquantes = STATS.refs_manquantes + 1
    return { pandoc.Strong({ pandoc.Str('??' .. id) }) }
  end
  if r.kind == 'titre' then -- unnumbered target: use its title
    if LATEX then
      return { pandoc.RawInline('latex', '\\hyperref[' .. id .. ']{' .. inlines_latex(r.title) .. '}') }
    end
    return { pandoc.Link(r.title, '#' .. id) }
  end
  local num = r.kind == 'equation' and ('(' .. r.num .. ')') or r.num
  if LATEX then
    local n = r.kind == 'equation' and ('\\eqref{' .. id .. '}') or ('\\ref{' .. id .. '}')
    if bare then return { pandoc.RawInline('latex', n) } end
    return { pandoc.RawInline('latex', WORD[r.kind] .. '~' .. n) }
  end
  local text = bare and num or (WORD[r.kind] .. '\u{00A0}' .. num)
  return { pandoc.Link({ pandoc.Str(text) }, '#' .. id) }
end

local function is_crossref(cite)
  for _, c in ipairs(cite.citations) do
    local p = c.id:match('^(%a+):')
    if not (p and PREFIXES[p]) then return false end
  end
  return true
end

-- LaTeX: floats (figure, longtable) are not allowed inside breakable boxes.
-- Inside blocks and statements, figures and tables become non-floating, same numbering.
local function figure_fixe(f)
  local body = pandoc.write(pandoc.Pandoc(f.content), 'latex'):gsub('\\textwidth', '\\linewidth')
  local cap = f.caption.long[1] and inlines_latex(f.caption.long[1].content) or ''
  local lab = f.identifier ~= '' and ('\\label{' .. f.identifier .. '}') or ''
  return pandoc.RawBlock('latex', '\\begin{center}\n' .. body .. '\n\\captionof{figure}{' .. cap .. '}' .. lab .. '\n\\end{center}')
end

local function tableau_fixe(t)
  local st = pandoc.utils.to_simple_table(t)
  local n, total = #st.aligns, 0
  for _, w in ipairs(st.widths) do total = total + w end
  local spec = ''
  for i, a in ipairs(st.aligns) do
    local f = (total > 0) and (st.widths[i] * n / total) or 1
    local align = a == 'AlignRight' and '\\raggedleft' or (a == 'AlignCenter' and '\\centering' or '\\raggedright')
    spec = spec .. string.format('>{\\hsize=%.3f\\hsize%s\\arraybackslash}X', f, align)
  end
  local function cell(c)
    return (pandoc.write(pandoc.Pandoc(c), 'latex'):gsub('%s+$', ''):gsub('\n', ' '))
  end
  local function row(cells)
    local t2 = {}
    for _, c in ipairs(cells) do table.insert(t2, cell(c)) end
    return table.concat(t2, ' & ') .. ' \\\\'
  end
  local out = { '\\begin{center}' }
  local cap = inlines_latex(st.caption)
  if cap ~= '' or t.identifier ~= '' then
    table.insert(out, '\\captionof{table}{' .. cap .. '}' .. (t.identifier ~= '' and ('\\label{' .. t.identifier .. '}') or ''))
  end
  table.insert(out, '\\small\\begin{tabularx}{\\linewidth}{' .. spec .. '}')
  table.insert(out, '\\toprule')
  if #st.headers > 0 then table.insert(out, row(st.headers)); table.insert(out, '\\midrule') end
  for _, r in ipairs(st.rows) do table.insert(out, row(r)) end
  table.insert(out, '\\bottomrule')
  table.insert(out, '\\end{tabularx}')
  table.insert(out, '\\end{center}')
  return pandoc.RawBlock('latex', table.concat(out, '\n'))
end

local function sans_flottants(blocks)
  return pandoc.Blocks(blocks):walk({ Figure = figure_fixe, Table = tableau_fixe })
end

local function bloc_title(name, titre, date)
  local t = titre or ''
  if date and date ~= '' then t = (t ~= '' and (t .. ' ') or '') .. '(' .. date .. ')' end
  return t
end

local render = {
  Cite = function(c)
    local cs = c.citations
    if #cs == 1 and cs[1].id == 'A-VERIFIER' then
      STATS.averifier = STATS.averifier + 1
      local txt = stringify(cs[1].suffix):gsub('^%s*:%s*', '')
      if LATEX then return pandoc.RawInline('latex', '\\averifier{' .. esc(txt) .. '}') end
      return pandoc.Span({ pandoc.Str('[à vérifier : ' .. txt .. ']') }, { class = 'a-verifier' })
    end
    if not is_crossref(c) then
      for _, ci in ipairs(cs) do
        if A_VERIFIER[ci.id] then -- candidate reference: keep the citation, mark it
          STATS.averifier = STATS.averifier + 1
          if LATEX then
            return { pandoc.RawInline('latex', '\\referenceaverifier{'), c, pandoc.RawInline('latex', '}') }
          end
          return pandoc.Span({ c }, { class = 'ref-a-verifier' })
        end
      end
      return nil
    end
    local out = pandoc.Inlines {}
    for k, ci in ipairs(cs) do
      if k > 1 then
        out:insert(pandoc.Str(k == #cs and ' et ' or ', '))
      end
      out:extend(reference(ci.id, ci.mode == 'SuppressAuthor'))
    end
    return out
  end,

  Span = function(s)
    if not s.classes:includes('equation') then return nil end
    local m = s.content[1]
    if LATEX then
      return pandoc.RawInline('latex', '\\begin{equation}' .. m.text .. '\\label{' .. s.identifier .. '}\\end{equation}')
    end
    local r = REFS[s.identifier]
    s.content = { m, pandoc.Str(' (' .. (r and r.num or '?') .. ')') }
    return s
  end,

  Div = function(d)
    for cls, spec in pairs(BLOCS) do
      if d.classes:includes(cls) then
        local titre = bloc_title(spec[1], d.attributes['titre'], d.attributes['date'])
        if LATEX then
          local blocks = pandoc.Blocks { pandoc.RawBlock('latex', '\\begin{' .. spec[2] .. '}{' .. esc(titre) .. '}') }
          blocks:extend(sans_flottants(d.content))
          blocks:insert(pandoc.RawBlock('latex', '\\end{' .. spec[2] .. '}'))
          return blocks
        end
        local head = { pandoc.Strong({ pandoc.Str(spec[1]) }) }
        if titre ~= '' then table.insert(head, pandoc.Str(' — ' .. titre)) end
        d.content:insert(1, pandoc.Div({ pandoc.Plain(head) }, { class = 'bloc-titre' }))
        d.classes:insert('bloc')
        return d
      end
    end
    local is_prop, is_def = d.classes:includes('proposition'), d.classes:includes('definition')
    if not (is_prop or is_def) then return nil end
    local titre = d.attributes['titre'] or ''
    local statut = d.attributes['statut']
    if is_prop and not (statut and STATUTS[statut]) then
      warn('statut absent ou invalide pour ' .. d.identifier .. ' : ' .. tostring(statut))
      STATS.statuts_manquants = STATS.statuts_manquants + 1
      statut = statut or '??'
    end
    local env = is_prop and 'proposition' or 'definition'
    if LATEX then
      local open = '\\begin{' .. env .. '}' .. (titre ~= '' and ('[' .. esc(titre) .. ']') or '') ..
        '\\label{' .. d.identifier .. '}' .. (is_prop and ('\\statut{' .. esc(statut) .. '}') or '')
      local blocks = pandoc.Blocks { pandoc.RawBlock('latex', open) }
      blocks:extend(sans_flottants(d.content))
      blocks:insert(pandoc.RawBlock('latex', '\\end{' .. env .. '}'))
      return blocks
    end
    local r = REFS[d.identifier]
    local head = { pandoc.Strong({ pandoc.Str((is_prop and 'Proposition ' or 'Définition ') .. (r and r.num or '?')) }) }
    if titre ~= '' then table.insert(head, pandoc.Str(' — ' .. titre)) end
    local blocks = { pandoc.Div({ pandoc.Plain(head) }, { class = 'enonce-titre' }) }
    if is_prop then table.insert(blocks, pandoc.Div({ pandoc.Plain({ pandoc.Emph({ pandoc.Str('Statut : ' .. statut) }) }) }, { class = 'statut' })) end
    d.content = pandoc.Blocks(blocks) .. d.content
    d.classes:insert('enonce')
    return d
  end,

  Header = function(h)
    if LATEX then
      local before = nil
      -- the template has already closed the front matter after the TOC: reopen it without
      -- restarting the roman page numbers (\reprendreliminaires, gabarit/preambule.tex)
      if h.classes:includes('avant-propos') then before = '\\reprendreliminaires'
      elseif h.classes:includes('corps') then before = '\\mainmatter\\setcounter{chapter}{-1}'
      elseif h.classes:includes('annexes') then before = '\\appendix'
      elseif h.classes:includes('fin') then before = '\\backmatter' end
      local out = pandoc.Blocks {}
      if before then out:insert(pandoc.RawBlock('latex', before)) end
      if h.level == 1 and not h.classes:includes('partie') then
        -- unnumbered chapter: floats numbered 1, 2… as in HTML (gabarit/preambule.tex)
        if h.classes:includes('unnumbered') then
          out:insert(pandoc.RawBlock('latex', '\\numerotationlocale{nn-' .. h.identifier:gsub('[^%w]', '-') .. '}'))
        else
          out:insert(pandoc.RawBlock('latex', '\\numerotationchapitre'))
        end
      elseif SANS_NUMERO[h.identifier] then
        h.classes:insert('unnumbered') -- still listed in the TOC, without a number
      end
      if #out == 0 then return h end
      out:insert(h)
      return out
    end
    local r = REFS[h.identifier]
    if r and r.num and (r.kind == 'chapitre' or r.kind == 'annexe' or r.kind == 'section') then
      local prefix = r.kind == 'annexe' and ('Annexe ' .. r.num .. ' — ') or (r.num .. '  ')
      h.content:insert(1, pandoc.Span({ pandoc.Str(prefix) }, { class = 'numero' }))
      return h
    end
  end,

  Figure = function(f)
    local missing = nil
    f = f:walk({ Image = function(img)
      local fh = io.open(img.src, 'r')
      if fh then fh:close() else missing = img.src; return nil end
      if not LATEX and img.src:match('%.pdf$') then -- print figure: use its .svg twin outside LaTeX
        local svg = img.src:gsub('%.pdf$', '.svg')
        local sh = io.open(svg, 'r')
        if sh then sh:close(); img.src = svg; return img end
      end
    end })
    if missing then
      warn('figure à générer : ' .. missing)
      STATS.figures_manquantes = STATS.figures_manquantes + 1
      if LATEX then
        f.content = { pandoc.Plain({ pandoc.RawInline('latex', '\\figureabsente{' .. esc(missing) .. '}') }) }
      else
        f.content = { pandoc.Div({ pandoc.Plain({ pandoc.Str('[Figure à générer : ' .. missing .. ']') }) }, { class = 'figure-absente' }) }
      end
    end
    if not LATEX and f.identifier ~= '' then
      local r = REFS[f.identifier]
      local cap = f.caption.long[1]
      if r and cap then cap.content:insert(1, pandoc.Strong({ pandoc.Str('Figure ' .. r.num .. ' — ') })) end
    end
    return f
  end,

  Table = function(t)
    if not LATEX and t.identifier ~= '' then
      local r = REFS[t.identifier]
      local cap = t.caption.long[1]
      if r and cap then cap.content:insert(1, pandoc.Strong({ pandoc.Str('Tableau ' .. r.num .. ' — ') })) end
      return t
    end
  end,
}

---------------------------------------------------------------------------
-- 5. French typography (typed spaces become the right non-breaking spaces)
---------------------------------------------------------------------------
local function space(kind) -- 'large' (before : » after «) or 'fine' (before ; ! ? %)
  if LATEX then return pandoc.RawInline('latex', kind == 'large' and '~' or '\\,') end
  return pandoc.Str(kind == 'large' and '\u{00A0}' or '\u{202F}')
end

local typography = {
  Inlines = function(inl)
    local changed = false
    for i = 1, #inl - 1 do
      local a, b = inl[i], inl[i + 1]
      if a.t == 'Space' and b.t == 'Str' then
        if b.text:match('^[;!?]') then
          inl[i] = space('fine'); changed = true
        elseif b.text:match('^:') or b.text:match('^»') then
          inl[i] = space('large'); changed = true
        elseif b.text:match('^%%') and i > 1 and inl[i - 1].t == 'Str' and inl[i - 1].text:match('%d$') then
          inl[i] = space('fine'); changed = true
        end
      elseif a.t == 'Str' and a.text:match('«$') and b.t == 'Space' then
        inl[i + 1] = space('large'); changed = true
      end
    end
    return changed and inl or nil
  end,
}

---------------------------------------------------------------------------
-- 6. Parts (LaTeX: part page with its introduction; HTML: a section)
---------------------------------------------------------------------------
local parts = {
  Pandoc = function(doc)
    local out, b, i = pandoc.Blocks {}, doc.blocks, 1
    while i <= #b do
      local el = b[i]
      if el.t == 'Header' and el.level == 1 and el.classes:includes('partie') then
        local intro, j = pandoc.Blocks {}, i + 1
        while j <= #b and not (b[j].t == 'Header' and b[j].level == 1) do intro:insert(b[j]); j = j + 1 end
        if LATEX then
          -- The title gets KOMA's part page; the introduction follows as ordinary text, so it
          -- may run over several pages (a \setpartpreamble box could not break and overflowed
          -- the part page). The next \chapter starts a new page as usual.
          out:insert(pandoc.RawBlock('latex', '\\part{' .. inlines_latex(el.content) .. '}\\label{' .. el.identifier .. '}'))
          if #intro > 0 then
            out:insert(pandoc.RawBlock('latex', '\\begin{introductionpartie}'))
            out:extend(intro)
            out:insert(pandoc.RawBlock('latex', '\\end{introductionpartie}'))
          end
        else
          local r = REFS[el.identifier]
          el.content:insert(1, pandoc.Str('Partie ' .. (r and r.num or '') .. ' — '))
          local sec = pandoc.Blocks { el }
          sec:extend(intro)
          out:insert(pandoc.Div(sec, { class = 'partie' }))
        end
        i = j
      else
        out:insert(el); i = i + 1
      end
    end
    if LATEX and PREMIER then
      out:insert(1, pandoc.RawBlock('latex', '\\setcounter{chapter}{' .. (PREMIER - 1) .. '}'))
    end
    doc.blocks = out
    local s = STATS
    if s.averifier + s.refs_manquantes + s.statuts_manquants + s.figures_manquantes > 0 then
      warn(string.format('bilan : %d à vérifier, %d références non définies, %d statuts manquants, %d figures à générer',
        s.averifier, s.refs_manquantes, s.statuts_manquants, s.figures_manquantes))
    end
    return doc
  end,
}

return { includes, normalize, collect, render, typography, parts }
