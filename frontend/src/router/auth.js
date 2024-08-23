export default [
	{
		path: '/',
		name: 'Home',
		component: () =>
			import(/* webpackChunkName: "login" */ '../views/Home.vue'),
		meta: {
			isLoginPage: false
		},
		props: false
	}
]
