<template>
	<div class="h-screen w-full">
		<Navbar />
		<div class="pt-12 md:pt-14 h-full">
			<router-view />
		</div>
	</div>
</template>

<script>
import Navbar from './components/Navbar.vue';
import './style.css';

export default {
	components: {
		Navbar,
	},
};
</script>