<template>
	<div class="min-h-screen bg-cream">
		<Hero
			:tagline="siteSettings.hero_tagline"
			:headline="siteSettings.hero_headline"
			:subtext="siteSettings.hero_subtext"
			:image="siteSettings.hero_image"
		/>

		<FeaturedProducts />
		<CategorySection />
		<CustomCakeBanner />
		<WhyChooseUs />
		<Testimonials />
		<GalleryStrip />
		<Footer
			:site-name="siteSettings.site_name"
			:store-hours="siteSettings.store_hours"
			:address="siteSettings.address"
			:tagline="siteSettings.footer_tagline"
		/>

		<div class="block md:hidden h-16 flex-shrink-0" aria-hidden="true" />
		<div class="block md:hidden fixed bottom-0 left-0 right-0 z-30">
			<Nav />
		</div>
	</div>
</template>

<script setup>
import { ref, inject } from 'vue';
import Hero from '../components/home/Hero.vue';
import FeaturedProducts from '../components/home/FeaturedProducts.vue';
import CategorySection from '../components/home/CategorySection.vue';
import CustomCakeBanner from '../components/home/CustomCakeBanner.vue';
import WhyChooseUs from '../components/home/WhyChooseUs.vue';
import Testimonials from '../components/home/Testimonials.vue';
import GalleryStrip from '../components/home/GalleryStrip.vue';
import Footer from '../components/home/Footer.vue';
import Nav from '../components/BottomNav/Nav.vue';

const store = inject('store');
const siteSettings = inject('siteSettings', ref({}));
</script>
