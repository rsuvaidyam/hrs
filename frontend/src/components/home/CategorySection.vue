<template>
	<section id="categories" class="py-16 md:py-24 px-4 md:px-8 bg-cream-dark/50">
		<div class="max-w-[1800px] mx-auto">
			<div class="text-center mb-12 md:mb-16">
				<h2 class="font-serif text-3xl md:text-4xl lg:text-5xl font-semibold text-chocolate">{{ sectionTitle || 'Categories' }}</h2>
				<p v-if="sectionSubtext" class="mt-2 text-chocolate-soft font-sans">{{ sectionSubtext }}</p>
			</div>

			<div v-if="loading" class="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-6">
				<div v-for="i in 4" :key="i" class="rounded-card bg-white h-36 md:h-44 animate-pulse" />
			</div>

			<div v-else-if="categoryList.length" class="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-6">
				<router-link
					v-for="cat in categoryList"
					:key="cat.name"
					:to="`/product-list/category/${cat.name}`"
					class="group block rounded-card bg-white p-6 shadow-soft transition-all duration-300 hover:shadow-lift hover:-translate-y-1 focus:outline-none focus-visible:ring-2 focus-visible:ring-bakery-primary focus-visible:ring-offset-2"
				>
					<div class="aspect-square rounded-xl overflow-hidden bg-cream mb-4">
						<img
							:src="cat.image || placeholderImage"
							:alt="cat.name1"
							class="w-full h-full object-cover transition-transform duration-300 group-hover:scale-105"
						/>
					</div>
					<h3 class="font-serif text-lg font-semibold text-chocolate text-center group-hover:text-bakery-primary transition-colors">
						{{ cat.name1 }}
					</h3>
				</router-link>
			</div>

			<!-- Empty state when no categories from API -->
			<div v-else class="text-center py-12 text-chocolate-soft">
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
