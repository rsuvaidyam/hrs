<template>
	<section class="relative w-full min-h-[85vh] md:min-h-[90vh] flex items-center justify-center overflow-hidden rounded-b-[2rem] md:rounded-b-[2.5rem]">
		<!-- Background image with overlay -->
		<div class="absolute inset-0 z-0">
			<img
				:src="heroImage"
				alt="Fresh pastries and cakes"
				class="w-full h-full object-cover scale-105"
			/>
			<div class="absolute inset-0 bg-chocolate/40 mix-blend-multiply" aria-hidden="true" />
			<div class="absolute inset-0 bg-gradient-to-b from-cream/20 via-transparent to-cream/60" aria-hidden="true" />
		</div>

		<!-- Content -->
		<div class="relative z-10 max-w-[1200px] mx-auto px-6 md:px-12 text-center pt-24 md:pt-32 pb-20">
			<p
				v-if="tagline"
				class="text-blush-soft font-sans text-sm md:text-base uppercase tracking-[0.2em] mb-4 md:mb-6 opacity-95"
				v-motion
				:initial="{ opacity: 0, y: 20 }"
				:visible="{ opacity: 1, y: 0 }"
				:delay="100"
			>
				{{ tagline }}
			</p>
			<h1
				class="font-serif text-4xl md:text-6xl lg:text-7xl font-semibold text-white drop-shadow-lg mb-4 md:mb-6 leading-tight"
				v-motion
				:initial="{ opacity: 0, y: 24 }"
				:visible="{ opacity: 1, y: 0 }"
				:delay="200"
			>
				{{ headline || 'Welcome' }}
			</h1>
			<p
				v-if="subtext"
				class="text-white/95 text-lg md:text-xl max-w-xl mx-auto mb-8 md:mb-10 font-sans font-light"
				v-motion
				:initial="{ opacity: 0, y: 20 }"
				:visible="{ opacity: 1, y: 0 }"
				:delay="350"
			>
				{{ subtext }}
			</p>
			<div
				class="flex flex-col sm:flex-row gap-4 justify-center items-center"
				v-motion
				:initial="{ opacity: 0, y: 20 }"
				:visible="{ opacity: 1, y: 0 }"
				:delay="450"
			>
				<router-link
					to="/product-list/category/all"
					class="inline-flex items-center justify-center px-8 py-4 rounded-button bg-bakery-primary hover:bg-bakery-primary-hover text-white font-medium shadow-soft transition-all duration-300 hover:shadow-lift hover:-translate-y-0.5 focus:outline-none focus-visible:ring-2 focus-visible:ring-bakery-primary focus-visible:ring-offset-2"
				>
					Order Now
				</router-link>
				<router-link
					to="/#featured"
					class="inline-flex items-center justify-center px-8 py-4 rounded-button bg-white/90 hover:bg-white text-chocolate font-medium shadow-soft backdrop-blur-sm border border-white/50 transition-all duration-300 hover:shadow-lift hover:-translate-y-0.5 focus:outline-none focus-visible:ring-2 focus-visible:ring-white"
				>
					Explore Menu
				</router-link>
			</div>
		</div>
	</section>
</template>

<script setup>
import { computed, inject } from 'vue';

const props = defineProps({
	tagline: { type: String, default: '' },
	headline: { type: String, default: '' },
	subtext: { type: String, default: '' },
	image: { type: String, default: '' },
});

const siteSettings = inject('siteSettings', {});
const heroImage = computed(() => {
	const img = props.image || (siteSettings && siteSettings.hero_image);
	if (img && typeof img === 'string' && img.startsWith('http')) return img;
	if (img) return img; // Frappe file URL
	return 'https://images.unsplash.com/photo-1509440159596-0249088772ff?w=1920&q=80';
});
</script>
