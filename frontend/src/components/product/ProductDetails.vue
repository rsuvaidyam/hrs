<template>
    <div class="min-h-screen bg-cream pt-14 md:pt-16 pb-20 md:pb-10">
        <div class="max-w-5xl mx-auto px-4" v-if="!loading && (products.name || selectedOption.name1)">
            <!-- Breadcrumb -->
            <nav class="text-sm text-chocolate-soft mb-4">
                <router-link to="/" class="hover:text-primary">Home</router-link>
                <span class="mx-2">/</span>
                <router-link :to="`/product-list/category/${products.category || 'all'}`" class="hover:text-primary">Products</router-link>
                <span class="mx-2">/</span>
                <span class="text-chocolate">{{ selectedOption.name1 || products.product_name }}</span>
            </nav>

            <div class="flex flex-col lg:flex-row gap-8 lg:gap-12">
                <!-- Images -->
                <div class="w-full lg:w-1/2">
                    <div class="rounded-2xl overflow-hidden bg-cream-dark shadow-soft">
                        <div class="aspect-square md:aspect-[4/3] flex items-center justify-center">
                            <img
                                v-if="mainImageUrl"
                                :src="mainImageUrl"
                                :alt="selectedOption.name1 || products.product_name"
                                class="w-full h-full object-cover"
                            />
                            <div v-else class="w-full h-full flex items-center justify-center text-chocolate-soft bg-blush-soft">
                                <span class="font-serif text-4xl">No image</span>
                            </div>
                        </div>
                        <div v-if="productImages.length > 1" class="flex gap-2 p-3 overflow-x-auto border-t border-blush-soft">
                            <button
                                v-for="(img, idx) in productImages"
                                :key="idx"
                                @click="setImageSelected(img)"
                                :class="{ 'ring-2 ring-primary ring-offset-2': imageSelected === img }"
                                class="shrink-0 w-16 h-16 rounded-lg overflow-hidden bg-cream border border-blush-soft"
                            >
                                <img :src="resolveImage(img)" alt="" class="w-full h-full object-cover" />
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Info -->
                <div class="w-full lg:w-1/2 flex flex-col">
                    <h1 class="font-serif text-3xl md:text-4xl font-semibold text-chocolate mb-2">
                        {{ selectedOption.name1 || products.product_name }}
                    </h1>
                    <p v-if="categoryName" class="text-sm text-chocolate-soft mb-4">{{ categoryName }}</p>

                    <!-- Price & Add to cart -->
                    <div class="flex flex-wrap items-center gap-4 mb-6">
                        <div class="flex items-baseline gap-2">
                            <span class="font-serif text-2xl md:text-3xl text-primary font-medium">
                                ₹ {{ Math.ceil(selectedOption.final_price ?? selectedOption.price ?? 0) }}
                            </span>
                            <template v-if="selectedOption.discounts">
                                <del class="text-base text-chocolate-soft">₹ {{ selectedOption.price }}</del>
                                <span class="text-sm font-medium text-primary">{{ selectedOption.discounts }}% off</span>
                            </template>
                        </div>
                        <div class="h-12 flex items-center">
                            <AddToCartBtn
                                :product="selectedOption"
                                :products="(products.items && products.items.length) ? products.items : [selectedOption]"
                                :option="selectedOption.name"
                            />
                        </div>
                    </div>

                    <!-- Dietary badges -->
                    <div class="flex flex-wrap gap-2 mb-6">
                        <span v-if="products.product_type" class="px-3 py-1 rounded-full text-xs font-medium bg-blush-soft text-chocolate">
                            {{ products.product_type }}
                        </span>
                        <span v-if="products.is_vegan" class="px-3 py-1 rounded-full text-xs font-medium bg-green-100 text-green-800">
                            Vegan
                        </span>
                        <span v-if="products.is_gluten_free" class="px-3 py-1 rounded-full text-xs font-medium bg-amber-100 text-amber-800">
                            Gluten Free
                        </span>
                    </div>

                    <!-- Description -->
                    <div v-if="selectedOption?.description" class="mb-6">
                        <h2 class="font-serif text-lg font-semibold text-chocolate mb-2">Description</h2>
                        <p class="text-chocolate-soft text-sm leading-relaxed">{{ selectedOption.description }}</p>
                    </div>
                    <div v-else class="mb-6">
                        <h2 class="font-serif text-lg font-semibold text-chocolate mb-2">Description</h2>
                        <p class="text-chocolate-soft text-sm italic">No description added yet.</p>
                    </div>

                    <!-- Product details (key features) -->
                    <div v-if="selectedOption?.key_features" class="mb-6">
                        <h2 class="font-serif text-lg font-semibold text-chocolate mb-2">Product Details</h2>
                        <div class="text-sm text-chocolate-soft prose prose-sm max-w-none" v-html="selectedOption.key_features" />
                    </div>

                    <!-- Unit selector (when multiple options) -->
                    <div v-if="products?.items?.length > 1" class="mb-6">
                        <h2 class="font-serif text-lg font-semibold text-chocolate mb-2">Select unit</h2>
                        <div class="flex flex-wrap gap-2">
                            <button
                                v-for="(item, index) in products.items"
                                :key="item?.name || index"
                                @click="selectedOption = item"
                                :class="selectedOption === item ? 'border-primary bg-blush-soft text-chocolate' : 'border-blush-soft'"
                                class="px-4 py-2 rounded-xl border-2 text-sm font-medium transition-colors"
                            >
                                {{ item.qty }} {{ item.unit }} — ₹ {{ Math.ceil(item.final_price) }}
                            </button>
                        </div>
                    </div>

                    <div v-if="products?.owner" class="mt-auto pt-6 border-t border-blush-soft text-sm text-chocolate-soft">
                        Seller: {{ products.owner }}
                    </div>
                </div>
            </div>
        </div>

        <!-- Loading -->
        <div v-if="loading" class="flex items-center justify-center min-h-[60vh]">
            <Spinner class="w-12 h-12 text-primary" />
        </div>

        <!-- Not found -->
        <div v-if="!loading && !products.name && !selectedOption.name1 && !error" class="flex flex-col items-center justify-center min-h-[60vh] text-chocolate-soft">
            <p class="font-serif text-xl">Product not found.</p>
            <router-link to="/" class="mt-4 text-primary font-medium hover:underline">Back to home</router-link>
        </div>
        <div v-if="error" class="flex flex-col items-center justify-center min-h-[60vh] text-chocolate-soft">
            <p class="font-serif text-xl">Something went wrong.</p>
            <router-link to="/" class="mt-4 text-primary font-medium hover:underline">Back to home</router-link>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, inject, computed } from 'vue';
import { Spinner } from 'frappe-ui';
import { useRoute } from 'vue-router';
import AddToCartBtn from '../AddToCartBtn.vue';

const route = useRoute();
const products = ref({});
const imageSelected = ref(null);
const selectedOption = ref({});
const loading = ref(true);
const error = ref(null);
const call = inject('$call');

function resolveImage(img) {
    if (!img) return '';
    const url = typeof img === 'string' ? img : (img.image || img.url);
    if (!url) return '';
    if (url.startsWith('http')) return url;
    return window.location.origin + (url.startsWith('/') ? url : '/' + url);
}

const productImages = computed(() => {
    const p = products.value;
    const imgs = p?.images;
    if (Array.isArray(imgs) && imgs.length) return imgs;
    if (p?.image) return [{ image: p.image }];
    return [];
});

const mainImageUrl = computed(() => {
    const sel = imageSelected.value;
    const first = productImages.value[0];
    if (sel) return resolveImage(sel);
    if (first) return resolveImage(first);
    return '';
});

const categoryName = computed(() => {
    const p = products.value;
    if (p?.category_name) return p.category_name;
    const c = p?.category;
    return typeof c === 'string' ? c : (c?.name ?? '');
});

onMounted(async () => {
    loading.value = true;
    error.value = null;
    try {
        const raw = await call('hrs.controllers.api.get_product_details', { name: route.params.name });
        const response = raw?.message ?? raw;
        if (!response || !response.doctype) {
            loading.value = false;
            return;
        }
        const images = response.images ?? (response.image ? [{ image: response.image }] : []);
        const imagesList = Array.isArray(images) ? images : [];
        products.value = { ...response, images: imagesList };
        imageSelected.value = imagesList[0] ?? null;

        const items = response.items;
        if (Array.isArray(items) && items.length > 0) {
            selectedOption.value = items[0];
        } else {
            selectedOption.value = {
                name: response.name,
                parent: response.name,
                name1: response.product_name,
                price: response.price,
                final_price: response.price,
                discounts: 0,
                description: response.description ?? '',
                key_features: response.key_features ?? '',
            };
        }
    } catch (e) {
        console.error(e);
        error.value = e;
    } finally {
        loading.value = false;
    }
});

function setImageSelected(img) {
    imageSelected.value = img;
}
</script>
