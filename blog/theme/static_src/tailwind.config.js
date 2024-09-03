/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    daisyui: {
    themes: [
      "light",
      "dark",
      "retro",
      {
        mytheme: {
          "primary": "#00cba1",
          "primary-content": "#000f09",
          "secondary": "#00bcff",
          "secondary-content": "#000d16",
          "accent": "#009500",
          "accent-content": "#000800",
          "neutral": "#001316",
          "neutral-content": "#c4caca",
          "base-100": "#1e2b30",
          "base-200": "#192428",
          "base-300": "#131d21",
          "base-content": "#cdd0d1",
          "info": "#007cdc",
          "info-content": "#000511",
          "success": "#4ef12d",
          "success-content": "#021401",
          "warning": "#c49600",
          "warning-content": "#0e0800",
          "error": "#ff7688",
          "error-content": "#160506",
        }
      },
    ],
  
  },
    content: [
        '../templates/**/*.html',
        '../../templates/**/*.html',
        '../../**/templates/**/*.html',

        
    ],
    theme: {
        extend: {},
    },
    plugins: [

        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
        require("daisyui"),
    ],
}
