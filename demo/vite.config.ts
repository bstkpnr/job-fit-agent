import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
  // GitHub Pages: sayfa bstkpnr.github.io/job-fit-agent/ altında açılır
  base: '/job-fit-agent/',
  plugins: [react()],
})
