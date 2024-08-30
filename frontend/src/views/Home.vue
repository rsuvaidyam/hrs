<template>
	<LocationDitecter/>
	<Carousel />
	<Category />
	<!-- <div class="px-3 md:px-8 pt-6 max-w-[1800px] mx-auto w-full">
		<Event />
	</div> -->
	<div :class="[store.cart_count > 0 ? 'pb-14' : '']">
		<ProductGrByEvent />
	</div>
</template>

<script setup>
import { inject } from 'vue';
import Carousel from '../components/Carousel.vue';
import Category from '../components/Category.vue';
import LocationDitecter from '../components/LocationDitecter.vue';
// import Event from '../components/Event.vue';
const store = inject('store');
import ProductGrByEvent from '../components/product/ProductGrByEvent.vue';

</script>
