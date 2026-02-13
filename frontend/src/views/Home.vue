<template>
	<div class="min-h-screen bg-cream">
		<!-- Hero (full-width) -->
		<Hero
			:tagline="siteSettings.hero_tagline"
			:headline="siteSettings.hero_headline"
			:subtext="siteSettings.hero_subtext"
			:image="siteSettings.hero_image"
		/>

		<!-- Featured Products -->
		<FeaturedProducts />

		<!-- Categories -->
		<CategorySection />

		<!-- Why Choose Us -->
		<WhyChooseUs />

		<!-- Testimonials -->
		<Testimonials />

		<!-- Gallery strip -->
		<GalleryStrip />

		<!-- Footer -->
		<Footer
			:site-name="siteSettings.site_name"
			:store-hours="siteSettings.store_hours"
			:address="siteSettings.address"
			:tagline="siteSettings.footer_tagline"
		/>

		<!-- Mobile bottom nav -->
		<div :class="[store.cart_count > 0 ? 'pb-14' : '']" class="block md:hidden" aria-hidden="true" />
		<div class="block md:hidden">
			<Nav />
		</div>
	</div>
</template>

<script setup>
import { ref, inject } from 'vue';
import Hero from '../components/home/Hero.vue';
import FeaturedProducts from '../components/home/FeaturedProducts.vue';
import CategorySection from '../components/home/CategorySection.vue';
import WhyChooseUs from '../components/home/WhyChooseUs.vue';
import Testimonials from '../components/home/Testimonials.vue';
import GalleryStrip from '../components/home/GalleryStrip.vue';
import Footer from '../components/home/Footer.vue';
import Nav from '../components/BottomNav/Nav.vue';

const store = inject('store');
const siteSettings = inject('siteSettings', ref({}));
</script>
