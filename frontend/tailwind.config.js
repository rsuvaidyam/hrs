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
			backgroundColor: {
				'primary': 'var(--color-bg-primary)',
				'secondary': 'var(--color-bg-secondary)',
				'tatary': 'var(--color-bg-tatary)',
				'btn-primary': 'var(--color-bg-btn-primary)',
				'btn-secondary': 'var(--color-bg-btn-secondary)',
			},
			textColor:{
			  'primary': 'var(--color-text-primary)',
			  'secondary': 'var(--color-text-secondary)',
			  'tatary': 'var(--color-text-tatary)',
			},
			screens: {
				standalone: {
					raw: "(display-mode: standalone)",
				},
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
