<template>
    <div class="w-full">
      <div class="w-full flex gap-3">
        <div
          v-for="item in data"
          :key="item"
          class="flex flex-col items-center gap-2"
        >
          <div class="md:w-32 bg-gray-100 w-16 md:h-32 h-16 rounded-full md:rounded-2xl border-2 md:border-0"></div>
          <div class="md:w-32 bg-gray-100 w-16 h-5 rounded-md"></div>
        </div>
      </div>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent } from 'vue';
  
  export default defineComponent({
    name: 'CategoryLoader',
    setup() {
      const data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  
      return {
        data,
      };
    },
  });
  </script>
  
  <style scoped>
  /* Add any component-specific styles here if needed */
  </style>
  