<template>
	<div class="h-screen w-full">
		<Navbar v-if="router.currentRoute.value.path!=='/place-order'"/>
		<div class="pt-12 md:pt-14 h-full">
			<!-- <PageTransition> -->
			<router-view />
			<!-- </PageTransition> -->
		</div>
	</div>
</template>

<script setup>
import Navbar from './components/Navbar.vue';
import { useRouter } from 'vue-router';
// import PageTransition from './components/PageTransition.vue';
import './style.css';

const router = useRouter(); 
</script>