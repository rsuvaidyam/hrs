<template>
	<div>
	  <Navbar />
	  <div class="pt-12 md:pt-14">
		<Carousel />
	  <router-view />
	  </div>
	</div>
  </template>
  
  <script>
  import Navbar from './components/Navbar.vue';
  import Carousel from './components/Carousel.vue';
  import './style.css';
  
  export default {
	inject: ['$auth'],
	components: {
	  Navbar,
	  Carousel
	},
  };
  </script>
  