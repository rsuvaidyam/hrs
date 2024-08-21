<template>
	<div>
	  <button v-if="$auth.isLoggedIn" @click="$auth.logout()">Logout</button>
	  <Navbar />
	  <!-- <router-view /> -->
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
  