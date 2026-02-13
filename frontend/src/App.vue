<template>
	<div class="min-h-screen w-full bg-cream">
		<GlassNavbar v-if="!rou.includes(router.currentRoute.value.path.split('/')[1])" />
		<div :class="!rou.includes(router.currentRoute.value.path.split('/')[1]) ? 'pt-16 md:pt-18 h-full' : ''">
			<router-view />
		</div>
	</div>
</template>

<script setup>
import GlassNavbar from './components/home/GlassNavbar.vue';
import { useRouter } from 'vue-router';
import { ref, onMounted, provide, inject } from 'vue';
import './style.css';

const router = useRouter();
const rou = ['place-order', 'order', 'cart'];

const siteSettings = ref({
	site_name: '',
	hero_tagline: '',
	hero_headline: '',
	hero_subtext: '',
	hero_image: '',
	featured_title: '',
	featured_subtext: '',
	categories_title: '',
	categories_subtext: '',
	store_hours: '',
	address: '',
	footer_tagline: '',
	meta_title: '',
});
provide('siteSettings', siteSettings);

const call = inject('$call', null);
onMounted(async () => {
	if (call) {
		try {
			const res = await call('hrs.controllers.api.get_site_settings', {});
			if (res && typeof res === 'object') {
				Object.assign(siteSettings.value, res);
				const title = res.meta_title || res.site_name;
				if (title && typeof document !== 'undefined') document.title = title;
			}
		} catch {
			// keep empty
		}
	}
});
</script>