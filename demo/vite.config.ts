import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
  // Vercel kök adreste açar ('/'); GitHub Pages ise bstkpnr.github.io/job-fit-agent/ altında.
  // GITHUB_PAGES değişkenini deploy-demo.yml ayarlıyor.
  base: process.env.GITHUB_PAGES ? '/job-fit-agent/' : '/',
  plugins: [react()],
})
