<template>
	<Carousel />
	<Category />
	<div class="px-3 md:px-8 pt-6 max-w-[1800px] mx-auto w-full">
		<Event />
	</div>
	<ProductGrByEvent />
</template>

<script setup>
import Carousel from '../components/Carousel.vue';
import Category from '../components/Category.vue';
import Event from '../components/Event.vue';
import ProductGrByEvent from '../components/product/ProductGrByEvent.vue';

</script>
