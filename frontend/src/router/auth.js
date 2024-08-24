export default [
	{
		path: '/cart',
		name: 'Cart',
		component: () =>
			import('../views/Cart.vue'),
		meta: {
			isLoginPage: false
		},
		props: false
	}
]
