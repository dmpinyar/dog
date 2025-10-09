import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  root: "src/",
  publicDir: "public/",
  base: "./",
  plugins: [react()],
  build: {
    outDir: "/var/www/html",
    emptyOutDir: true,
  },
});

