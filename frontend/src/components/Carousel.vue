<template>
  <div class="carousel-container max-w-[1800px] mx-auto">
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
</template>

<script setup>
import { ref, onMounted, inject } from 'vue';
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
