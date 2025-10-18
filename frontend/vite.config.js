import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import dotenv from 'dotenv'
import path from 'path'

dotenv.config({ path: path.resolve(__dirname, '../.env') })
const apiUrl = `http://localhost:${API_PORT}}`

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: process.env.APACHE_DIRECTORY_PATH,
    emptyOutDir: true,
  },
  server: {
    proxy: {
      '/api': apiUrl,
    },
  },
})
