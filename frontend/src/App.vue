<template>
	<div class="h-screen w-full">
		<Navbar v-if="!rou.includes(router.currentRoute.value.path.split('/')[1])"/>
		<div :class="!rou.includes(router.currentRoute.value.path.split('/')[1])?'pt-12 md:pt-14 h-full':''">
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
import { watch } from 'vue';

const router = useRouter(); 
console.log(router.currentRoute.value)
const rou= ['place-order','order','cart']
watch(() => router.currentRoute.value.path, (to, from) => {
	router.currentRoute.value.path = to;
})
</script>