<!-- src/components/CartAlert.vue -->
<template>
    <div class="pt-8 pb-2 w-full h-4/5 px-0 md:px-10 flex justify-center">
      <div class=" w-full md:w-4/5 rounded-md border-0 md:border md:bg-gray-50 md:shadow-md h-full flex flex-col gap-3 items-center justify-center">
        <p class="font-normal text-2xl">Your cart is empty!</p>
        <p class="text-xs">Add items to it now.</p>
        <router-link to="/" class="px-10 py-2 text-sm bg-primary border bg-white rounded-sm">Shop now</router-link>
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
  