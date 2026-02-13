<template>
	<section id="featured" class="py-12 sm:py-16 md:py-20 px-4 sm:px-6 md:px-8 max-w-[1400px] mx-auto">
		<!-- Section header -->
		<div class="text-center mb-10 md:mb-14">
			<h2 class="font-serif text-2xl sm:text-3xl md:text-4xl font-semibold text-chocolate">
				{{ sectionTitle || 'Cake Showcase' }}
			</h2>
			<p v-if="sectionSubtext" class="mt-3 text-chocolate-soft max-w-lg mx-auto font-sans text-base md:text-lg">
				{{ sectionSubtext }}
			</p>
		</div>

		<!-- Chef's Special carousel (first 4 only) -->
		<div v-if="!loading && products.length > 0" class="mb-12 md:mb-14">
			<p class="text-xs font-semibold text-chocolate-soft uppercase tracking-widest mb-4">Chef's Special</p>
			<div class="flex gap-4 sm:gap-5 overflow-x-auto pb-2 scroll-smooth snap-x snap-mandatory hide-scrollbar -mx-4 px-4 sm:-mx-6 sm:px-6 md:mx-0 md:px-0">
				<article
					v-for="product in products.slice(0, 4)"
					:key="product.name"
					class="flex-shrink-0 w-[260px] sm:w-[280px] md:w-[300px] snap-center rounded-2xl overflow-hidden bg-white shadow-soft cake-card-hover border border-cream-dark/80"
				>
					<router-link :to="{ name: 'ProductDetails', params: { name: product.name } }" class="block">
						<div class="aspect-[4/5] overflow-hidden bg-cream-dark relative">
							<div v-if="!productImage(product)" class="absolute inset-0 skeleton" />
							<img
								v-else
								:src="productImage(product)"
								:alt="productName(product)"
								class="w-full h-full object-cover transition-transform duration-400 hover:scale-105"
								loading="lazy"
							/>
							<span class="absolute top-3 left-3 px-2.5 py-1 rounded-pill bg-bakery-primary text-white text-xs font-semibold shadow-md">
								Chef's Special
							</span>
						</div>
						<div class="p-4">
							<h3 class="font-serif text-lg font-semibold text-chocolate truncate">{{ productName(product) }}</h3>
							<p class="mt-0.5 text-chocolate-soft text-sm">₹ {{ priceDisplay(product) }}</p>
						</div>
					</router-link>
				</article>
			</div>
		</div>

		<!-- Skeleton grid -->
		<div v-if="loading" class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4 sm:gap-6">
			<div v-for="i in 8" :key="i" class="rounded-2xl overflow-hidden bg-cream-dark/80">
				<div class="aspect-[4/5] skeleton" />
				<div class="p-4 space-y-2">
					<div class="h-4 w-3/4 rounded skeleton" />
					<div class="h-3 w-1/2 rounded skeleton" />
				</div>
			</div>
		</div>

		<!-- Grid: rest of products (skip first 4 to avoid duplicate with carousel) -->
		<div v-else-if="gridProducts.length > 0" class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4 sm:gap-6">
			<article
				v-for="product in gridProducts"
				:key="product.name"
				class="group relative bg-white rounded-2xl shadow-soft overflow-hidden cake-card-hover border border-cream-dark/60"
			>
				<div class="absolute top-2.5 left-2.5 z-10 flex flex-wrap gap-1.5">
					<span
						v-if="product.product_type === 'Eggless'"
						class="px-2 py-1 rounded-pill bg-blush-soft text-chocolate text-[10px] sm:text-xs font-medium"
					>
						Eggless
					</span>
					<span
						v-if="product.is_vegan"
						class="px-2 py-1 rounded-pill bg-green-100 text-green-800 text-[10px] sm:text-xs font-medium"
					>
						Vegan
					</span>
				</div>

				<router-link :to="{ name: 'ProductDetails', params: { name: product.name } }" class="block">
					<div class="aspect-[4/5] overflow-hidden bg-cream-dark relative">
						<div v-if="!productImage(product)" class="absolute inset-0 skeleton" />
						<img
							v-else
							:src="productImage(product)"
							:alt="productName(product)"
							class="w-full h-full object-cover transition-transform duration-400 group-hover:scale-105"
							loading="lazy"
						/>
					</div>
					<div class="p-4">
						<h3 class="font-serif text-base sm:text-lg font-semibold text-chocolate line-clamp-2">
							{{ productName(product) }}
						</h3>
						<p class="mt-1 text-chocolate-soft font-sans text-xs sm:text-sm line-clamp-2 min-h-[2.25rem]">
							{{ productDescription(product) }}
						</p>
						<p class="mt-1.5 font-serif text-base font-semibold text-bakery-primary">
							₹ {{ priceDisplay(product) }}
						</p>
					</div>
				</router-link>

				<div class="px-4 pb-4">
					<AddToCartBtn
						v-if="displayItem(product)"
						:product="displayItem(product)"
						:products="displayItemsList(product)"
						:option="displayOption(product)"
						class="w-full min-h-[40px]"
					/>
				</div>
			</article>
		</div>

		<div v-if="!loading && products.length === 0" class="text-center py-14 text-chocolate-soft">
			<p class="font-serif text-lg">No cakes to show yet. Check back soon!</p>
		</div>

		<div class="text-center mt-10 md:mt-12">
			<router-link
				to="/product-list/category/all"
				class="inline-flex items-center gap-2 px-6 py-3 sm:px-8 sm:py-4 rounded-pill border-2 border-chocolate/25 text-chocolate font-semibold text-sm sm:text-base hover:bg-chocolate/8 hover:border-chocolate/40 transition-all duration-300"
			>
				View all cakes
				<svg class="w-4 h-4 sm:w-5 sm:h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3" /></svg>
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
const gridProducts = computed(() => products.value.slice(4));

function productImage(p) {
	const img = p?.images?.[0]?.image || p?.image;
	return img || null;
}

function productName(p) {
	return p?.items?.[0]?.name1 || p?.product_name || 'Cake';
}

function productDescription(p) {
	return p?.items?.[0]?.description || 'Handcrafted with love. Perfect for every occasion.';
}

function priceDisplay(p) {
	const item = p?.items?.[0];
	if (item?.final_price != null) return Math.ceil(item.final_price);
	if (item?.price != null) return Math.ceil(item.price);
	if (p?.price != null) return Math.ceil(p.price);
	return '—';
}

function displayItem(p) {
	const hasItems = Array.isArray(p?.items) && p.items.length > 0;
	if (hasItems) return p.items[0];
	return {
		name: p?.name,
		parent: p?.name,
		name1: p?.product_name,
		price: p?.price,
		final_price: p?.price,
		count: 0,
	};
}

function displayItemsList(p) {
	const hasItems = Array.isArray(p?.items) && p.items.length > 0;
	if (hasItems) return p.items;
	return [displayItem(p)];
}

function displayOption(p) {
	const d = displayItem(p);
	return d?.name ?? p?.name;
}

onMounted(async () => {
	try {
		const res = await call('hrs.controllers.api.get_featured_products', { user: session?.user ?? '' });
		products.value = Array.isArray(res) ? res : [];
	} catch {
		try {
			const res = await call('hrs.controllers.api.get_event_by_product', { user: session?.user ?? '' });
			products.value = res ? Object.values(res).flat().slice(0, 12) : [];
		} catch {
			products.value = [];
		}
	} finally {
		loading.value = false;
	}
});
</script>

<style scoped>
.hide-scrollbar::-webkit-scrollbar {
  display: none;
}
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
