<template>
    <router-link :to="{ name: 'ProductDetails', params: { name: product?.name } }" class="block">
        <div class="w-full overflow-hidden rounded-t-sm relative">
            <div class="-top-0.5 -left-0.5 absolute " v-if="product?.items[0]?.discounts">
                <svg width="34" height="30" viewBox="0 0 29 28" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path
                        d="M28.9499 0C28.3999 0 27.9361 1.44696 27.9361 2.60412V27.9718L24.5708 25.9718L21.2055 27.9718L17.8402 25.9718L14.4749 27.9718L11.1096 25.9718L7.74436 27.9718L4.37907 25.9718L1.01378 27.9718V2.6037C1.01378 1.44655 0.549931 0 0 0H28.9499Z"
                        fill="#538CEE"></path>
                </svg>
                <span v-if="product?.items[0]?.discounts"
                    class="top-0.5 absolute rounded-br-md px-2 text-white text-[9px] font-medium flex flex-col">{{
                        product?.items[0]?.discounts }}% <span>OFF</span></span>
            </div>
            <div class="max-h-36 min-h-36 flex item-center justify-center">
                <img :src="product?.images[0]?.image" alt="" class="carousel__item rounded-t-sm w-full" />
            </div>

        </div>
    </router-link>
    <div class="w-full p-2 flex flex-col gap-2">
        <p class="text-sm text-main">{{ product?.items[0]?.name1 }}</p>
        <ProductOption :product="product" />
        <router-link :to="{ name: 'ProductDetails', params: { name: product?.name } }">
            <div class="flex justify-between items-end">
                <div class="flex flex-col gap-1">
                    <span class="flex gap-0.5 items-center text-sm text-secondary">
                        <span>₹</span>{{ Math.ceil(product?.items[0]?.final_price)
                        }}
                    </span>
                    <template v-if="product?.items[0]?.discounts">
                        <div class="flex gap-0.5 items-center text-xs text-gray-700 text-tatary">
                            <span>₹</span> <del>{{ product?.items[0]?.price }}</del>
                        </div>
                    </template>
                </div>
            </div>
        </router-link>
    </div>
    <div class="absolute bottom-1 right-2 w-16">
        <AddToCartBtn :product="product.items[0]" :products="product.items" :option="product.items[0].name" />
    </div>
</template>

<script setup>
import AddToCartBtn from '../AddToCartBtn.vue';
import ProductOption from '../product/ProductOption.vue';
const props = defineProps({
    product: {
        type: Object,
        required: true,
    }
});
</script>