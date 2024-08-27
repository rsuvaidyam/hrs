<template>
    <div class="w-full px-3 md:px-8 pt-6 max-w-[1800px] mx-auto flex flex-col gap-5">
        <div v-for="e in product" :key="e.name" class="bg-white md:rounded-sm shadow-md p-3">
            <div class="flex items-center justify-between">
                <p class="text-2xl font-medium text-main">
                    {{ e.name1 }} <span class="text-lg">({{ e.products.length }})</span>
                </p>
                <router-link :to="`/productlist/event/${e.name}`"
                    class="px-4 py-1 cursor-pointer text-sm font-medium bg-primary text-white">
                    View All
                </router-link>
            </div>
            <div class="pt-3 overflow-x-auto scrollbar-thin flex gap-2 md:gap-3">
                <router-link v-for="product in e.products" :key="product.name" :to="{ name: 'ProductDetails', params: { name: product.name } }"
                    target="_blank"
                    class="border w-1/5 min-w-[200px] md:min-w-[220px] hover:shadow-xl cursor-pointer rounded-sm bg-white">
                    <div class="w-full overflow-hidden rounded-t-sm">
                        <Carousel :autoplay="2000" :wrap-around="true">
                            <Slide v-for="image in product.images" :key="image.name">
                                <img :src="image.url" alt=""
                                    class="carousel__item rounded-t-sm max-h-44 w-full" />
                            </Slide>

                            <template #addons>
                                <Pagination />
                            </template>
                        </Carousel>
                    </div>
                    <div class="w-full p-1 flex flex-col gap-2">
                        <p class="text-sm truncate text-main">{{ product.name1 }}</p>
                        <div class="flex justify-between items-center">
                            <div class="flex items-center gap-1">
                                <span class="flex items-center text-secondary">
                                    <FeatherIcon name="dollar-sign" class="w-4 h-4"/>{{ Math.ceil(product.final_price) }}
                                </span>
                                <template v-if="product.discounts">
                                    <del class="flex items-center text-sm text-gray-700 text-tatary">
                                        <FeatherIcon name="dollar-sign" class="w-3 h-3"/>{{ product.price }}
                                    </del>
                                    <span class="text-primary text-sm font-medium">{{ product.discounts }}% off</span>
                                </template>
                            </div>
                            <div class="bg-primary rounded-sm px-1 text-sm text-white flex items-center gap-1">
                                4.3
                                <BsStarHalf class="text-xs" />
                            </div>
                        </div>
                        <div class="flex justify-between items-center">
                            <span class="text-xs font-medium text-main">{{ product.category }}</span>
                            <div class="text-xs text-primary">456 Reviews</div>
                        </div>
                    </div>
                </router-link>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted, inject } from 'vue';
import { Carousel, Pagination, Slide } from 'vue3-carousel'
import 'vue3-carousel/dist/carousel.css'

const product = ref([]);
const call = inject('$call');
const getProducts = async () => {
    try {
        const response = await call('hrs.controllers.product.get_event_by_product', {});
        product.value = response;
    } catch (error: any) {
        console.log(error);

    }
};

onMounted(() => {
    getProducts();
});
</script>