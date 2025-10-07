import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  root: "src/vite-root",
  publicDir: "../vite-public",
  build: {
    outDir: "/var/www/html",
    emptyOutDir: true,
  },
});

