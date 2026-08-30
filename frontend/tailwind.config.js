module.exports = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        // Professional warm tones - inspired by educational institutions
        'kec-primary': {
          50: '#fef5e7',
          100: '#fce4c8',
          200: '#f9d3a3',
          300: '#f5c27e',
          400: '#f2b159',
          500: '#d4a574',  // Warm gold/tan primary
          600: '#b8915b',
          700: '#8b7043',
          800: '#5e4a2d',
          900: '#3a2e1f',
        },
        'kec-accent': {
          50: '#f0f4f8',
          100: '#d9e2ec',
          200: '#c2d0e0',
          300: '#a8bcd4',
          400: '#6b8cbe',  // Rich professional blue
          500: '#4a6fa5',
          600: '#365a87',
          700: '#2a4469',
          800: '#1f314d',
          900: '#141f31',
        },
        'kec-secondary': {
          50: '#faf6f0',
          100: '#f5ede5',
          200: '#ede4d9',
          300: '#dcc9b8',
          400: '#c4a882',  // Warm bronze
          500: '#a8916f',
          600: '#8c765a',
          700: '#6d5a45',
          800: '#4f4035',
          900: '#332a23',
        },
        // Elegant grays for backgrounds and text
        'slate-warm': {
          50: '#faf9f7',
          100: '#f5f3f0',
          200: '#e8e4e0',
          300: '#d5cfc9',
          400: '#a9a19a',
          500: '#7f776f',
          600: '#6b6360',
          700: '#4f4945',
          800: '#3a3530',
          900: '#27231f',
          950: '#1a1715',
        },
      },
      animation: {
        'fade-in': 'fadeIn 0.6s ease-in',
        'slide-up': 'slideUp 0.8s cubic-bezier(0.34, 1.56, 0.64, 1)',
        'drift': 'drift 6s ease-in-out infinite',
        'float': 'float 3s ease-in-out infinite',
        'scroll-appear': 'scrollAppear 0.8s ease-out forwards',
        'drone-fly': 'droneFly 4s ease-in-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { transform: 'translateY(40px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        drift: {
          '0%, 100%': { transform: 'translateX(0) translateY(0)' },
          '25%': { transform: 'translateX(20px) translateY(-10px)' },
          '50%': { transform: 'translateX(-10px) translateY(15px)' },
          '75%': { transform: 'translateX(-25px) translateY(-5px)' },
        },
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-20px)' },
        },
        scrollAppear: {
          '0%': { opacity: '0', transform: 'translateY(30px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        droneFly: {
          '0%': { transform: 'translate(0, 0) scale(1)', opacity: '1' },
          '100%': { transform: 'translate(-400px, -600px) scale(0.3)', opacity: '0' },
        },
      },
      backgroundImage: {
        'gradient-warm': 'linear-gradient(135deg, #d4a574 0%, #f2b159 50%, #8b7043 100%)',
        'gradient-elegant': 'linear-gradient(135deg, #fef5e7 0%, #f9d3a3 100%)',
        'gradient-accent': 'linear-gradient(135deg, #4a6fa5 0%, #6b8cbe 100%)',
      },
    },
  },
  plugins: [],
  darkMode: 'class',
}
