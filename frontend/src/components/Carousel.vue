<template>
    <div class="carousel-container">
      <Carousel
        :autoplay="2000"
        wrap-around="true"
        :dynamic-height="true"
      >
        <Slide v-for="el in carousel" :key="el._id">
          <img :src="el.image" :alt="el.mimetype" class="carousel__item h-24" />
        </Slide>
  
        <template #addons>
          <Pagination />
        </template>
      </Carousel>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted, watch,inject } from 'vue';
  import { Carousel, Pagination, Slide } from 'vue3-carousel';
  import 'vue3-carousel/dist/carousel.css';
  
  const carousel = ref([]);
  const call = inject('$call');

  const getCategory = async () => {
    try {
        const response = await call('hrs.controllers.api.get_carousel', {});
        carousel.value = response?.images || [];
    } catch (error) {
      console.log(error);
      
    }
  };
  
  watch(getCategory, { immediate: true });
  </script>
  
  <style scoped>
  .carousel__item {
    min-height: 200px;
    width: 100%;
    background-color: var(--vc-clr-primary);
    color: var(--vc-clr-white);
    font-size: 20px;
    border-radius: 8px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  </style>
  