<template>
    <div class="pt-10 lg:pt-2 w-full h-full max-w-[1060px] mx-auto relative">
        <div class="w-full h-full flex justify-center items-center" v-if="loading">
            <Spinner class="w-14" />
        </div>
        <div v-else class="flex flex-col gap-x-5 md:flex-row h-full">
            <div class="w-full md:w-1/2 md:h-full md:p-2">
                <div class="hidden md:block">
                    <div class="w-full h-auto md:h-full flex gap-2">
                        <div class="w-20 h-full flex flex-col gap-1">
                            <div v-for="(image, index) in products.images" :key="index" @click="setImageSelected(image)"
                                :class="{ 'border-2 border-gray-950': imageSelected?.name === image.name }"
                                class="px-0.5 md:px-0 overflow-hidden cursor-pointer">
                                <img class="h-full md:h-auto w-auto md:w-full" :src="image?.image" alt="" />
                            </div>
                        </div>
                        <div class="w-full h-full flex flex-col gap-3">
                            <img class="w-full"
                                :src="imageSelected?.image || (products?.images && products?.images[0]?.image)"
                                alt="" />
                        </div>
                    </div>
                </div>
                <div class="block md:hidden">
                    <Carousel :autoplay="2000" :wrap-around="true">
                        <Slide v-for="(image, index) in products.images" :key="index">
                            <img :src="image?.image" alt="" class="carousel__item rounded-t-sm max-h-64 w-full" />
                        </Slide>
                        <template #addons>
                            <Pagination />
                        </template>
                    </Carousel>
                </div>
            </div>
            <div class="w-full border-l md:w-1/2 h-full px-3 lg:pl-5 pb-14 md:pb-0 flex flex-col gap-2 relative">
                <p class="text-3xl border-b pb-2">{{ selectedOption.name1 }}</p>
                <div class="flex items-center gap-2 relative">
                    <span class="flex gap-0.5 text-3xl font-normal text-secondary">
                        <span>₹</span>
                        {{ Math.ceil(selectedOption.final_price) }}
                    </span>
                    <template v-if="selectedOption">
                        <del class="flex gap-0.5 items-center text-base text-tatary">
                            <span>₹</span>
                            {{ selectedOption.price }}
                        </del>
                        <span class="text-primary text-base font-medium">{{ selectedOption.discounts }}% off</span>
                    </template>
                    <div class="w-20 absolute right-1 top-0 h-14">
                        <AddToCartBtn :product="selectedOption" :products="products.items"
                            :option="selectedOption.name" />
                    </div>
                </div>
                <div class="flex items-center gap-2">
                    <div class="w-5 h-5 border-2 border-green-500 flex items-center justify-center">
                        <div class="w-3 h-3 rounded-full bg-green-500"></div>
                    </div>
                    <span class="text-main">100% vegetarian</span>
                </div>
                <div class="flex items-center gap-2">
                    <p class="font-light text-sm">Fresh Cake & delicious</p>
                </div>
                <div class="" v-if="products?.items?.length > 1">
                    <p class="pb-2 text-md">Select Unit</p>
                    <div class="flex gap-2">
                        <div v-for="(item, index) in products?.items" :key="index"
                            class="truncate px-4 cursor-pointer py-2 rounded-md border-2 flex flex-col gap-1 items-center justify-center text-[11px] font-medium"
                            :class="{ 'border-yellow-900 border-2 shadow-sm bg-amber-50': selectedOption === item }"
                            @click="selectOption(item)">
                            <p>{{ item.qty }} {{ selectedOption.unit }}</p>
                            <div class="flex gap-1">
                                <p class="flex items-center text-xs gap-0.5 font-semibold">
                                    ₹ {{ Math.ceil(item.final_price) }}
                                </p>
                                <del v-if="item.discounts > 0" class="flex items-center text-xs gap-0.5 font-light">
                                    ₹ {{ item.price }}
                                </del>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="w-full" >
                    <p class="text-md font-medium to-gray-700 py-2">Description</p>
                    <p class="text-sm border-b">{{ selectedOption?.description?.substring(0, 200) }}{{
                        selectedOption?.description?.length >
                            200 ? '...'
                            : '' }}</p>
                </div>
                <div class="w-full">
                    <p class="font-medium text-md to-gray-700" v-if="selectedOption?.key_features">Product Details</p>
                    <div class="text-xs list-disc pl-6" v-html="selectedOption.key_features" />
                </div>
                <div class="w-full">
                    <p class="font-medium text-tatary text-sm">Seller : {{ products?.owner }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, inject } from 'vue';
import { Spinner } from 'frappe-ui';
import { useRoute, useRouter } from 'vue-router';
import { Button } from 'frappe-ui';
import { Carousel, Pagination, Slide } from 'vue3-carousel'
import 'vue3-carousel/dist/carousel.css'
import AddToCartBtn from '../AddToCartBtn.vue';

const route = useRoute();
const router = useRouter();

const products = ref({});
const imageSelected = ref({});
const selectedOption = ref({});
const loading = ref(true);
const cart_loading = ref(false);
const call = inject('$call');

onMounted(async () => {
    try {
        const response = await call('hrs.controllers.api.get_product_details', { name: route.params.name });
        products.value = { ...response, image: response.images };
        imageSelected.value = response.images[0];
        selectedOption.value = products.value.items[0];
        setTimeout(() => {
            loading.value = false;
        }, 1000);
    } catch (error) {
        console.log(error);
    }
});

const addToCart = async (item, event) => {
    cart_loading.value = true;
    try {
        const response = await call('hrs.controllers.api.add_to_cart', { product: item, event: event });
        cart_loading.value = false;
    } catch (error) {
        console.log(error);
    }
};
const setImageSelected = (image) => {
    imageSelected.value = image;
};
const selectOption = (option) => {
    selectedOption.value = option;
};
</script>
