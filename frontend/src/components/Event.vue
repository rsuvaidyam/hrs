<template>
    <div class="bg-white md:rounded-md shadow-md p-3 w-full h-full">
      <p class="text-2xl pt-2 pb-3 font-medium text-main truncate">Celebrate with Bakery Favorites</p>
      <OccasionsLoader v-if="loader" />
      <div v-else class="w-full flex flex-col md:flex-row gap-3">
        <router-link
          v-for="occasion in occasions"
          :key="occasion.name"
          :to="`/product-list/event/${occasion.name}`"
          class="w-full md:w-1/2"
        >
          <div class="w-full cursor-pointer overflow-hidden rounded-t-md">
            <img
              class="rounded-t-md h-full w-full transition-all duration-200 hover:scale-105"
              :src="occasion.image"
              :alt="occasion.name1"
            />
          </div>
          <p class="text-center font-semibold text-main pt-2">{{ occasion.name1 }}</p>
        </router-link>
      </div>
    </div>
  </template>
  
  <script >
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
        } catch (error) {
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
  
