<template>
	<div class="h-screen w-full">
		<Navbar v-if="!rou.includes(router.currentRoute.value.path)"/>
		<div :class="!rou.includes(router.currentRoute.value.path)?'pt-12 md:pt-14 h-full':''">
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
const rou= ['/place-order','/order','/cart']
</script>