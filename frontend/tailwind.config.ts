import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          dark: '#0f172a',
          blue: '#1d4ed8',
          teal: '#0f766e',
          light: '#e0f2fe'
        }
      }
    },
  },
  plugins: [],
}
export default config
