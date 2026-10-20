import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// In development the FastAPI backend runs on :8000 and Vite proxies /api to it.
export default defineConfig({
  plugins: [react()],
  build: { chunkSizeWarningLimit: 6000 }, // plotly.js is large; fine for a local teaching app
  server: {
    port: 5173,
    proxy: { "/api": "http://127.0.0.1:8000" },
  },
});
