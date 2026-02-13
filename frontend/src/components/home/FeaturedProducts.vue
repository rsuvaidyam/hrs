<template>
	<section id="featured" class="py-16 md:py-24 px-4 md:px-8 max-w-[1800px] mx-auto">
		<div class="text-center mb-12 md:mb-16">
			<h2 class="font-serif text-3xl md:text-4xl lg:text-5xl font-semibold text-chocolate">{{ sectionTitle || 'Featured' }}</h2>
			<p v-if="sectionSubtext" class="mt-4 text-chocolate-soft max-w-xl mx-auto font-sans">{{ sectionSubtext }}</p>
		</div>

		<div v-if="loading" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6 md:gap-8">
			<div v-for="i in 4" :key="i" class="rounded-card bg-cream-dark animate-pulse h-80" />
		</div>

		<div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6 md:gap-8">
			<article
				v-for="product in products"
				:key="product.name"
				class="group relative bg-white rounded-card shadow-soft overflow-hidden transition-all duration-300 hover:shadow-lift hover:-translate-y-2 focus-within:ring-2 focus-within:ring-bakery-primary focus-within:ring-offset-2"
			>
				<!-- Badges -->
				<div class="absolute top-3 left-3 z-10 flex flex-wrap gap-2">
					<span
						v-if="product.badge === 'Best Seller'"
						class="px-2.5 py-1 rounded-lg bg-bakery-primary text-white text-xs font-medium shadow-soft"
					>
						Best Seller
					</span>
					<span
						v-if="product.badge === 'New'"
						class="px-2.5 py-1 rounded-lg bg-chocolate text-white text-xs font-medium shadow-soft"
					>
						New
					</span>
					<span
						v-if="product.product_type === 'Eggless'"
						class="px-2.5 py-1 rounded-lg bg-blush-soft text-chocolate text-xs font-medium"
					>
						Eggless
					</span>
				</div>

				<router-link :to="{ name: 'ProductDetails', params: { name: product.name } }" class="block">
					<div class="aspect-[4/5] overflow-hidden bg-cream-dark">
						<img
							:src="productImage(product)"
							:alt="product.items?.[0]?.name1 || product.product_name"
							class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
						/>
					</div>
					<div class="p-5 md:p-6">
						<h3 class="font-serif text-xl font-semibold text-chocolate truncate">
							{{ product.items?.[0]?.name1 || product.product_name }}
						</h3>
						<p class="mt-1 text-chocolate-soft font-sans text-sm">
							₹ {{ priceDisplay(product) }}
						</p>
					</div>
				</router-link>

				<!-- Quick add to cart -->
				<div class="absolute bottom-5 left-5 right-5 opacity-0 group-hover:opacity-100 transition-opacity duration-300">
					<AddToCartBtn
						v-if="product.items?.[0]"
						:product="product.items[0]"
						:products="product.items"
						:option="product.items[0].name"
						class="w-full"
					/>
				</div>
			</article>
		</div>

		<div v-if="!loading && products.length === 0" class="text-center py-12 text-chocolate-soft">
			<p>No featured products yet. Check back soon!</p>
		</div>

		<div class="text-center mt-10">
			<router-link
				to="/product-list/category/all"
				class="inline-flex items-center gap-2 px-6 py-3 rounded-button border-2 border-chocolate/20 text-chocolate font-medium hover:bg-chocolate/5 hover:border-chocolate/40 transition-colors"
			>
				View all products
				<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3" /></svg>
			</router-link>
		</div>
	</section>
</template>

<script setup>
import { ref, onMounted, inject, computed } from 'vue';
import AddToCartBtn from '../AddToCartBtn.vue';

const call = inject('$call');
const session = inject('$session');
const siteSettings = inject('siteSettings', {});
const sectionTitle = computed(() => siteSettings?.featured_title ?? '');
const sectionSubtext = computed(() => siteSettings?.featured_subtext ?? '');

const products = ref([]);
const loading = ref(true);

function productImage(p) {
	const img = p?.images?.[0]?.image || p?.items?.[0]?.image || p?.image;
	return img || 'https://images.unsplash.com/photo-1558961363-fa8fdf82db35?w=400&q=80';
}

function priceDisplay(p) {
	const item = p?.items?.[0];
	if (item?.final_price != null) return Math.ceil(item.final_price);
	if (item?.price != null) return Math.ceil(item.price);
	return '—';
}

onMounted(async () => {
	try {
		const res = await call('hrs.controllers.api.get_featured_products', { user: session?.user ?? '' });
		products.value = Array.isArray(res) ? res : [];
	} catch {
		// Fallback: fetch first page of products
		try {
			const res = await call('hrs.controllers.api.get_event_by_product', { user: session?.user ?? '' });
			const flat = res ? Object.values(res).flat().slice(0, 8) : [];
			products.value = flat;
		} catch {
			products.value = [];
		}
	} finally {
		loading.value = false;
	}
});
</script>
