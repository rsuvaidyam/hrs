<template>
  <div class="carousel-container max-w-[1800px] mx-auto">
    <div class="w-full h-48 animate-pulse bg-gray-100" v-if="loader"></div>
    <div v-else>
      <Carousel 
      :autoplay="2000"
      :wrap-around="true"
      :dynamic-height="true"
    >
      <Slide v-for="el in carousel" :key="el.name">
        <img :src="el.image" :alt="el.mimetype" class="carousel__item h-24" />
      </Slide>

      <template #addons>
        <Pagination />
      </template>
    </Carousel>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, inject } from 'vue';
import { Carousel, Pagination, Slide } from 'vue3-carousel';
import 'vue3-carousel/dist/carousel.css';

const carousel = ref([]);
const call = inject('$call');
const loader = ref(false);

const getCategory = async () => {
  loader.value = true;
  try {
    const response = await call('hrs.controllers.api.get_carousel', {});
    carousel.value = response?.images || [];
    loader.value = false;
  } catch (error) {
    console.log(error);
    loader.value = false;
  }
};

// Trigger the function on component mount
onMounted(getCategory);
</script>

<style scoped>
.carousel__item {
  min-height: 200px;
  width: 100%;
  background-color: var(--vc-clr-primary);
  color: var(--vc-clr-white);
  font-size: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
