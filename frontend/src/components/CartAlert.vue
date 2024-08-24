<!-- src/components/CartAlert.vue -->
<template>
    <div class="pt-8 pb-2 w-full h-1/2 px-0 md:px-10 flex justify-center">
      <div class=" w-full md:w-4/5 border-0 md:border md:bg-gray-50 md:shadow-md h-full flex flex-col gap-3 items-center justify-center">
        <p class="font-medium">Your cart is empty!</p>
        <p class="text-xs">Add items to it now.</p>
        <router-link to="/" class="px-10 py-1.5 bg-primary border bg-white rounded-md">Shop now</router-link>
      </div>
    </div>
  </template>
  
  <script >
  export default {
    name: 'CartAlert',
  };
  </script>
  
  <style scoped>
  /* Add any scoped styles here if needed */
  </style>
  