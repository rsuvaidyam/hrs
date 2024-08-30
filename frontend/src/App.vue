<template>
	<div class="h-screen w-full">
		<Navbar />
		<div class="pt-12 md:pt-14 h-full">
			<!-- <PageTransition> -->
			<router-view />
			<!-- </PageTransition> -->
		</div>
	</div>
</template>

<script>
import Navbar from './components/Navbar.vue';
// import PageTransition from './components/PageTransition.vue';
import './style.css';

export default {
	components: {
		Navbar,
	},
};
</script>