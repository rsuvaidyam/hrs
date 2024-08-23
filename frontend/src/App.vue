<template>
	<div>
	  <Navbar />
	  <router-view />
	</div>
  </template>
  
  <script>
  import Navbar from './components/Navbar.vue';
  import './style.css';
  
  export default {
	inject: ['$auth'],
	components: {
	  Navbar,
	},
  };
  </script>
  