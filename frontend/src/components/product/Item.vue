<template>
    <router-link :to="{ name: 'ProductDetails', params: { name: product?.name } }" class="block">
        <div class="w-full overflow-hidden rounded-t-sm relative">
            <div class="-top-0.5 -left-0.5 absolute " v-if="displayItem?.discounts">
                <svg width="34" height="30" viewBox="0 0 29 28" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path
                        d="M28.9499 0C28.3999 0 27.9361 1.44696 27.9361 2.60412V27.9718L24.5708 25.9718L21.2055 27.9718L17.8402 25.9718L14.4749 27.9718L11.1096 25.9718L7.74436 27.9718L4.37907 25.9718L1.01378 27.9718V2.6037C1.01378 1.44655 0.549931 0 0 0H28.9499Z"
                        fill="#538CEE"></path>
                </svg>
                <span v-if="displayItem?.discounts"
                    class="top-0.5 absolute rounded-br-md px-2 text-white text-[9px] font-medium flex flex-col">{{
                        displayItem?.discounts }}% <span>OFF</span></span>
            </div>
            <div class="max-h-36 min-h-36 flex item-center justify-center bg-cream">
                <img :src="productImage" alt="" class="carousel__item rounded-t-sm w-full object-cover" />
            </div>

        </div>
    </router-link>
    <div class="w-full p-2 flex flex-col gap-2">
        <p class="text-sm text-main">{{ displayItem?.name1 || product?.product_name }}</p>
        <ProductOption :product="productForOption" />
        <router-link :to="{ name: 'ProductDetails', params: { name: product?.name } }">
            <div class="flex justify-between items-end">
                <div class="flex flex-col gap-1">
                    <span class="flex gap-0.5 items-center text-sm text-secondary">
                        <span>₹</span>{{ Math.ceil(displayItem?.final_price ?? product?.price ?? 0) }}
                    </span>
                    <template v-if="displayItem?.discounts">
                        <div class="flex gap-0.5 items-center text-xs text-gray-700 text-tatary">
                            <span>₹</span> <del>{{ displayItem?.price }}</del>
                        </div>
                    </template>
                </div>
            </div>
        </router-link>
    </div>
    <div class="absolute bottom-1 right-2 w-16">
        <AddToCartBtn :product="displayItemWithCount" :products="displayItemsList" :option="displayOption" />
    </div>
</template>

<script setup>
import { computed } from 'vue';
import AddToCartBtn from '../AddToCartBtn.vue';
import ProductOption from '../product/ProductOption.vue';

const props = defineProps({
    product: {
        type: Object,
        required: true,
    }
});

// Support both schema: product with items[] (Product Option) or single product (product_name, price, image/images)
const hasItems = computed(() => Array.isArray(props.product?.items) && props.product.items.length > 0);

const displayItem = computed(() => {
    if (hasItems.value) return props.product.items[0];
    return {
        name: props.product?.name,
        name1: props.product?.product_name,
        price: props.product?.price,
        final_price: props.product?.price,
        parent: props.product?.name,
        count: 0,
    };
});

const displayItemWithCount = computed(() => ({ ...displayItem.value, count: 0 }));
const displayItemsList = computed(() => hasItems.value ? props.product.items : [displayItem.value]);
const displayOption = computed(() => displayItem.value?.name ?? props.product?.name);

const productImage = computed(() => {
    const p = props.product;
    if (p?.image) return p.image;
    const img = p?.images?.[0];
    return (img && (img.image || img.url)) || '';
});

// ProductOption expects product with .items; for simple product pass a normalized shape
const productForOption = computed(() => {
    if (hasItems.value) return props.product;
    return { ...props.product, items: [displayItem.value] };
});
</script>
