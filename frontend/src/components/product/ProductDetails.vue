<template>
    <div class="md:pt-14 w-full h-full max-w-[1060px] mx-auto relative">
        <Spinner v-if="false" />
        <div v-else class="flex flex-col gap-x-5 md:flex-row h-full">
            <div class="w-full md:w-1/2 md:h-full md:p-2">
                <div class="hidden md:block">
                    <div class="w-full h-auto md:h-full flex gap-2">
                        <div class="w-20 h-full flex flex-col gap-1">
                            <div v-for="(image, index) in products.images" :key="index" @click="setImageSelected(image)"
                                :class="{ 'border-2 border-gray-950': imageSelected?.name === image.name }"
                                class="px-0.5 md:px-0 overflow-hidden cursor-pointer">
                                <img class="h-full md:h-auto w-auto md:w-full" :src="image.url" alt="" />
                            </div>
                        </div>
                        <div class="w-full h-full flex flex-col gap-3">
                            <img class="w-full" :src="imageSelected?.url || (products?.images && products?.images[0]?.url)" alt="" />
                            <div class="hidden md:block">
                                <div class="w-full items-center flex gap-4 left-0 px-2 md:px-0">
                                    <Button @click="addToCart(products.name)" :loading="cart_loading"
                                        class="uppercase w-full font-medium h-[45px] text-white bg-primary">
                                        Add to Cart
                                    </Button>
                                    <Button @click="buyNow(products.name)" :disabled="cart_loading"
                                        class="uppercase w-full font-medium h-[45px] text-white bg-secondary">
                                        Buy Now
                                    </Button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="block md:hidden">
                    <Carousel :autoplay="2000" :wrap-around="true">
                        <Slide v-for="(image, index) in products.images" :key="index">
                            <img :src="image.url" alt="" class="carousel__item rounded-t-sm max-h-56 w-full" />
                        </Slide>
                        <template #addons>
                            <Pagination />
                        </template>
                    </Carousel>
                </div>
            </div>
            <div
                class="w-full md:w-1/2 h-full md:overflow-y-scroll md:scrollbar-none p-2 pb-14 md:pb-0 flex flex-col gap-2 relative">
                <p class="text-xl">{{ products.name1 }}</p>
                <div class="flex items-center gap-2">
                    <div class="bg-primary px-1 font-medium rounded-sm text-sm text-white flex items-center gap-1">
                        4.3
                        <FeatherIcon name="star" class="w-3 h-3"/>
                    </div>
                    <div class="text-xs text-primary font-normal">456 Reviews</div>
                </div>
                <div class="flex items-center gap-2">
                    <span class="flex text-3xl font-normal text-secondary">
                         <FeatherIcon name="dollar-sign" class="w-5 h-5"/>
                        {{ products.discounts ? Math.ceil((100 - products.discounts) / 100 * products.price) : products.price }}
                    </span>
                    <template v-if="products.discounts">
                        <del class="flex items-center text-base text-tatary">
                            <FeatherIcon name="dollar-sign" class="w-4 h-4"/>
                            {{ products.price }}
                        </del>
                        <span class="text-primary font-medium">{{ products.discounts }}% off</span>
                    </template>
                </div>
                <div class="flex items-center gap-2">
                    <div class="w-5 h-5 border-2 border-green-500 flex items-center justify-center">
                        <div class="w-3 h-3 rounded-full bg-green-500"></div>
                    </div>
                    100% vegetarian
                </div>
                <div class="flex items-center gap-2">
                    <p class="font-light text-sm">Fresh Cake & delicious</p>
                </div>
                <div class="">
                    <p class="font-bold">Weight</p>
                    <div class="flex gap-2">
                        <div class="px-2 h-10 rounded-lg border flex items-center justify-center text-sm">1 Kg</div>
                        <div class="px-2 h-10 rounded-lg border flex items-center justify-center text-sm">1.5 Kg</div>
                    </div>
                </div>
                <div class="w-full">
                    <p class="text-lg font-medium to-gray-700">Description</p>
                    <p class="text-sm">{{ products?.description?.substring(0, 200) }}{{ products?.description?.length > 200 ? '...' : '' }}</p>
                </div>
                <div class="w-full">
                    <p class="font-medium to-gray-700">Product Details</p>
                    <div class="text-xs list-disc pl-6" v-html="products.key_features" />
                </div>
                <div class="w-full">
                    <p class="font-medium text-tatary text-sm">Seller : {{ products.created_by?.name }}</p>
                </div>
                <div class="block md:hidden">
                    <div
                        class="w-full bg-[#982B1C] fixed md:sticky bottom-0 h-14 items-center flex gap-4 left-0 px-2 md:px-0 z-10">
                        <button @click="addToCart(products.name)"
                            class="uppercase w-full font-medium h-10 text-white bg-primary">
                            Add to Cart
                        </button>
                        <button @click="buyNow(products.name)"
                            class="uppercase w-full font-medium h-10 bg-secondary">
                            Buy Now
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, inject } from 'vue';
import {Spinner} from 'frappe-ui';
import { useRoute, useRouter } from 'vue-router';
import {Button} from 'frappe-ui';
import { Carousel, Pagination, Slide } from 'vue3-carousel'
import 'vue3-carousel/dist/carousel.css'

const isRender = inject('isRender');
const setIsRender = inject('setIsRender');
const setLogInPage = inject('setLogInPage');
const route = useRoute();
const router = useRouter();

const products = ref({});
const imageSelected = ref({});
const loading = ref(true);
const cart_loading = ref(false);
const call = inject('$call');

onMounted(async () => {
    try {
        const response = await call('hrs.controllers.product.get_product_details', { name: route.params.name });
        products.value = { ...response, image: response.images };
        imageSelected.value = response.images;
        setTimeout(() => {
            loading.value = false;
        }, 1000);
    } catch (error) {
        console.log(error);
    }
});

const addToCart = async (item) => {
    cart_loading.value = true;
    try {
        const response = await call('hrs.controllers.api.add_to_cart', { product: item });

        if (response.code === 200) {
            cart_loading.value = false;
            router.push('/cart');
        } else {
            setTimeout(() => {
                router.push('/cart');
            }, 2000);
        }
    } catch (error) {
       console.log(error);
    }
};

const buyNow = async (item) => {
    // Handle buy now logic
    console.log(item);
};

const setImageSelected = (image) => {
    imageSelected.value = image;
};
</script>

<style scoped>
/* Add your component styles here */
</style>
