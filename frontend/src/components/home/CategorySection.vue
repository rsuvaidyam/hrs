<template>
	<section id="categories" class="py-12 sm:py-16 md:py-20 px-4 sm:px-6 md:px-8 bg-gradient-to-b from-cream-dark/40 to-cream">
		<div class="max-w-[1400px] mx-auto">
			<div class="text-center mb-10 md:mb-12">
				<h2 class="font-serif text-2xl sm:text-3xl md:text-4xl font-semibold text-chocolate">
					{{ sectionTitle || 'Browse by Occasion' }}
				</h2>
				<p v-if="sectionSubtext" class="mt-2 text-chocolate-soft font-sans text-base md:text-lg">{{ sectionSubtext }}</p>
			</div>

			<div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-3 sm:gap-4 md:gap-5 mb-10 md:mb-12">
				<router-link
					v-for="occasion in occasions"
					:key="occasion.name"
					:to="occasion.to"
					class="group flex flex-col items-center rounded-2xl bg-white/90 p-4 sm:p-5 md:p-6 shadow-soft transition-all duration-300 hover:shadow-lift hover:-translate-y-1.5 focus:outline-none focus-visible:ring-2 focus-visible:ring-bakery-primary focus-visible:ring-offset-2"
				>
					<div class="w-16 h-16 sm:w-20 sm:h-20 md:w-24 md:h-24 rounded-full overflow-hidden bg-cream-dark mb-3 ring-2 ring-blush-soft/60 group-hover:ring-blush/80 transition-all duration-300 group-hover:scale-105 flex-shrink-0">
						<img
							:src="occasion.image"
							:alt="occasion.label"
							class="w-full h-full object-cover"
						/>
					</div>
					<h3 class="font-serif text-sm sm:text-base font-semibold text-chocolate text-center group-hover:text-bakery-primary transition-colors leading-tight">
						{{ occasion.label }}
					</h3>
				</router-link>
			</div>

			<template v-if="loading">
				<div class="grid grid-cols-2 md:grid-cols-4 gap-4">
					<div v-for="i in 4" :key="i" class="rounded-2xl bg-white/80 h-32 md:h-36 skeleton" />
				</div>
			</template>
			<template v-else-if="categoryList.length">
				<p class="text-center text-chocolate-soft font-medium text-sm mb-4">Shop by category</p>
				<div class="grid grid-cols-2 md:grid-cols-4 gap-4">
					<router-link
						v-for="cat in categoryList"
						:key="cat.name"
						:to="`/product-list/category/${cat.name}`"
						class="group block rounded-2xl bg-white/90 p-4 md:p-5 shadow-soft transition-all duration-300 hover:shadow-lift hover:-translate-y-1 focus:outline-none focus-visible:ring-2 focus-visible:ring-bakery-primary focus-visible:ring-offset-2"
					>
						<div class="aspect-square rounded-xl overflow-hidden bg-cream mb-3">
							<img
								:src="cat.image || placeholderImage"
								:alt="cat.name1"
								class="w-full h-full object-cover transition-transform duration-300 group-hover:scale-105"
							/>
						</div>
						<h3 class="font-serif text-base font-semibold text-chocolate text-center group-hover:text-bakery-primary transition-colors">
							{{ cat.name1 }}
						</h3>
					</router-link>
				</div>
			</template>
			<div v-else class="text-center py-6 text-chocolate-soft text-sm">
				<p>{{ emptyMessage }}</p>
			</div>
		</div>
	</section>
</template>

<script setup>
import { ref, onMounted, inject, computed } from 'vue';

const call = inject('$call');
const siteSettings = inject('siteSettings', {});
const categoryList = ref([]);
const loading = ref(true);
const placeholderImage = ref('https://images.unsplash.com/photo-1509440159596-0249088772ff?w=400&q=80');
const sectionTitle = computed(() => siteSettings?.categories_title ?? '');
const sectionSubtext = computed(() => siteSettings?.categories_subtext ?? '');
const emptyMessage = ref('No categories yet. Add categories from the admin.');

const occasions = [
	{ name: 'birthday', label: 'Birthday Cakes', to: '/product-list/category/all', image: 'https://images.unsplash.com/photo-1558305801-3e9f43c2a68a?w=200&q=80' },
	{ name: 'wedding', label: 'Wedding Cakes', to: '/product-list/category/all', image: 'https://images.unsplash.com/photo-1535254973040-607b474cb50d?w=200&q=80' },
	{ name: 'anniversary', label: 'Anniversary', to: '/product-list/category/all', image: 'https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=200&q=80' },
	{ name: 'designer', label: 'Designer Cakes', to: '/product-list/category/all', image: 'https://images.unsplash.com/photo-1488477181946-6428a0291777?w=200&q=80' },
	{ name: 'cupcakes', label: 'Cupcakes', to: '/product-list/category/all', image: 'https://images.unsplash.com/photo-1614707267537-b85aaf00c4b7?w=200&q=80' },
];

onMounted(async () => {
	try {
		const res = await call('hrs.controllers.api.get_category', {});
		categoryList.value = Array.isArray(res) ? res : [];
	} catch {
		categoryList.value = [];
	} finally {
		loading.value = false;
	}
});
</script>
