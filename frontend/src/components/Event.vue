<template>
    <div class="bg-white md:rounded-md shadow-md p-3 w-full h-full">
      <p class="text-2xl pt-2 pb-3 font-medium text-main truncate">Celebrate Special Occasions</p>
      <OccasionsLoader v-if="loader" />
      <div v-else class="w-full flex flex-col md:flex-row gap-3">
        <router-link
          v-for="occasion in occasions"
          :key="occasion.name"
          :to="`/productlist/event/${occasion.name}`"
          class="w-full md:w-1/2"
        >
          <div class="w-full cursor-pointer overflow-hidden rounded-t-md">
            <img
              v-if="occasion.name1 === 'Happy Birthday'"
              class="rounded-t-md h-full w-full transition-all duration-200 hover:scale-105"
              src="https://www.fnp.com/assets/images/custom/cakes_23/special_occasion/Birthday_web.jpg"
              alt=""
            />
            <img
              v-else
              class="rounded-t-md h-full w-full transition-all duration-200 hover:scale-105"
              src="https://www.fnp.com/assets/images/custom/cakes_23/special_occasion/Anniversary_web.jpg"
              alt=""
            />
          </div>
          <p class="text-center font-semibold text-main pt-2">{{ occasion.name1.split(' ')[1] }}</p>
        </router-link>
      </div>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent, ref, onMounted,inject } from 'vue';
  import OccasionsLoader from '@/components/Loader/EventLoader.vue'; // Adjust the path as necessary
  
  export default defineComponent({
    name: 'Occasion',
    components: {
      OccasionsLoader,
    },
    setup() {
      const occasions = ref([]);
      const loader = ref(true);
      const call = inject('$call');
  
      const getOccasion = async () => {
        loader.value = true;
        try {
          const response = await call('hrs.controllers.api.get_event', {});
          occasions.value = response;
          setTimeout(() => {
            loader.value = false;
          }, 1000);
        } catch (error: any) {
          console.log(error);
          
        }
      };
  
      onMounted(() => {
        getOccasion();
      });
  
      return {
        occasions,
        loader,
      };
    },
  });
  </script>
  
  <style scoped>
  /* Add any component-specific styles here if needed */
  </style>
  