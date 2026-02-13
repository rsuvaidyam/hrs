module.exports = {
	presets: [require("frappe-ui/src/utils/tailwind.config")],
	content: [
		"./index.html",
		"./src/**/*.{vue,js,ts,jsx,tsx}",
		"./node_modules/frappe-ui/src/components/**/*.{vue,js,ts,jsx,tsx}",
		"../node_modules/frappe-ui/src/components/**/*.{vue,js,ts,jsx,tsx}",
	],
	theme: {
		extend: {
			fontFamily: {
				serif: ['Cormorant Garamond', 'Georgia', 'serif'],
				sans: ['DM Sans', 'system-ui', 'sans-serif'],
			},
			colors: {
				cream: { DEFAULT: '#FDF8F3', dark: '#F5EDE4' },
				blush: { DEFAULT: '#E8C4B8', soft: '#F5E6E0' },
				beige: { DEFAULT: '#D4A574', light: '#E8D5C4' },
				chocolate: { DEFAULT: '#5C4033', soft: '#8B7355' },
				bakery: {
					primary: '#C17F59',
					'primary-hover': '#A66B47',
					footer: '#2C2419',
				},
				footer: {
					text: '#E8E0D8',
					muted: '#9A8F82',
				},
			},
			backgroundColor: {
				'primary': 'var(--color-bg-primary)',
				'secondary': 'var(--color-bg-secondary)',
				'tatary': 'var(--color-bg-tatary)',
				'btn-primary': 'var(--color-bg-btn-primary)',
				'btn-secondary': 'var(--color-bg-btn-secondary)',
			},
			textColor: {
				'primary': 'var(--color-text-primary)',
				'main': 'var(--color-text-main)',
				'secondary': 'var(--color-text-secondary)',
				'tatary': 'var(--color-text-tatary)',
			},
			boxShadow: {
				'soft': '0 4px 24px rgba(92, 64, 51, 0.08)',
				'lift': '0 12px 40px rgba(92, 64, 51, 0.12)',
				'glass': '0 8px 32px rgba(92, 64, 51, 0.06)',
			},
			borderRadius: {
				'card': '16px',
				'button': '14px',
				'pill': '9999px',
				'xl': '20px',
			},
			transitionDuration: {
				'300': '300ms',
			},
			screens: {
				standalone: { raw: "(display-mode: standalone)" },
			},
			padding: {
				"safe-top": "env(safe-area-inset-top)",
				"safe-right": "env(safe-area-inset-right)",
				"safe-bottom": "env(safe-area-inset-bottom)",
				"safe-left": "env(safe-area-inset-left)",
			},
		},
	},
	plugins: [],
}
