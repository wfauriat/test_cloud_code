"""Caption cues from spec §1.2, split into ≤ 2-line chunks, plus an .srt writer."""

SCENES = [  # (name, start, end, chapter label)
    ("s1", 0.0, 8.0, "1 · The game"),
    ("s2", 8.0, 24.0, "2 · A probability for every token"),
    ("s3", 24.0, 36.0, "3 · Predict, append, repeat"),
    ("s4", 36.0, 56.0, "4 · Learning by guessing"),
    ("s5", 56.0, 68.0, "5 · Nudge, billions of times"),
    ("s6", 68.0, 80.0, "6 · The text is the answer key"),
]

CUES = [  # (start, end, text)
    (0.3, 7.6, "A large language model does one thing, over and over: it predicts the next word."),
    (8.3, 14.0, "Given “The cat sat on the”, it doesn’t pick one word."),
    (14.0, 23.6, "It scores every possible token, a probability for each, adding up to one hundred percent."),
    (24.3, 29.5, "Pick one, add it to the text, and ask again."),
    (29.5, 35.6, "Whole answers are written this way, one token at a time."),
    (36.3, 41.0, "So how does it learn? By playing the same game on text that already exists."),
    (41.0, 46.5, "Hide the next word, guess, then check the real one."),
    (46.5, 50.8, "The size of the miss is the loss."),
    (50.8, 55.7, "A confident right guess costs little; a confident wrong guess costs a lot."),
    (56.3, 61.5, "A big miss nudges millions of internal numbers, just slightly,"),
    (61.5, 65.3, "so the right word becomes a little more likely next time."),
    (65.3, 67.7, "Repeat that billions of times."),
    (68.3, 72.5, "No labels, no teacher. The text itself is the answer key."),
    (72.5, 77.3, "Get good enough at predicting, and grammar, facts, even reasoning start to emerge."),
]


def _stamp(t):
    ms = round(t * 1000)
    return f"{ms // 3_600_000:02d}:{ms // 60_000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


def write_srt(path="captions.srt"):
    with open(path, "w", encoding="utf-8") as f:
        for i, (a, b, text) in enumerate(CUES, 1):
            f.write(f"{i}\n{_stamp(a)} --> {_stamp(b)}\n{text}\n\n")


if __name__ == "__main__":
    write_srt()
