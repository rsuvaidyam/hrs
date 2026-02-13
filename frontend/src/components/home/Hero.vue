<template>
	<section class="relative w-full min-h-[72vh] sm:min-h-[78vh] md:min-h-[88vh] flex items-end md:items-center justify-center overflow-hidden rounded-b-[1.5rem] sm:rounded-b-[2rem] md:rounded-b-[2.5rem] shadow-xl">
		<!-- Background image -->
		<div class="absolute inset-0 z-0">
			<img
				:src="heroImage"
				alt="Fresh pastries and cakes"
				class="w-full h-full object-cover object-center scale-[1.03] transition-transform duration-700"
			/>
			<!-- Stronger overlay for text readability -->
			<div class="absolute inset-0 bg-gradient-to-b from-black/55 via-black/35 to-black/60" aria-hidden="true" />
			<div class="absolute inset-0 bg-gradient-to-t from-chocolate/70 via-transparent to-transparent" aria-hidden="true" />
		</div>

		<!-- Floating badges -->
		<div class="absolute top-20 sm:top-24 left-4 right-4 md:left-10 md:right-auto z-10 flex flex-wrap gap-2 justify-center md:justify-start">
			<span class="glass-soft px-3.5 py-2 rounded-pill text-white text-xs md:text-sm font-medium shadow-lg border border-white/20">
				Eggless
			</span>
			<span class="glass-soft px-3.5 py-2 rounded-pill text-white text-xs md:text-sm font-medium shadow-lg border border-white/20">
				Best Seller
			</span>
			<span class="glass-soft px-3.5 py-2 rounded-pill text-white text-xs md:text-sm font-medium shadow-lg border border-white/20">
				Same Day Delivery
			</span>
		</div>

		<!-- Content -->
		<div class="relative z-10 max-w-[920px] mx-auto px-5 sm:px-8 md:px-12 text-center pb-16 sm:pb-20 md:pb-24 pt-28 sm:pt-32 md:pt-0">
			<p
				v-if="tagline"
				class="text-blush-soft font-sans text-xs sm:text-sm md:text-base uppercase tracking-[0.2em] mb-3 md:mb-4 opacity-95"
			>
				{{ tagline }}
			</p>
			<h1 class="font-serif text-3xl sm:text-4xl md:text-5xl lg:text-6xl xl:text-7xl font-semibold text-white drop-shadow-[0_2px_20px_rgba(0,0,0,0.4)] mb-4 md:mb-5 leading-[1.12] tracking-tight">
				{{ headline || 'Freshly Baked Happiness' }}
			</h1>
			<p class="text-white/95 text-base sm:text-lg md:text-xl max-w-lg mx-auto mb-8 md:mb-10 font-sans font-light leading-relaxed drop-shadow-sm">
				{{ subtext || 'Custom cakes made with love for every celebration.' }}
			</p>
			<router-link
				to="/product-list/category/all"
				class="inline-flex items-center justify-center px-8 py-3.5 sm:px-10 sm:py-4 md:px-12 md:py-5 rounded-pill bg-bakery-primary hover:bg-bakery-primary-hover text-white font-semibold text-sm sm:text-base md:text-lg shadow-xl transition-all duration-300 hover:shadow-[0_14px_40px_rgba(193,127,89,0.4)] hover:-translate-y-0.5 focus:outline-none focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-offset-2 focus-visible:ring-offset-chocolate"
			>
				Order Now
			</router-link>
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
	if (img) return img;
	return 'https://images.unsplash.com/photo-1509440159596-0249088772ff?w=1920&q=80';
});
</script>
