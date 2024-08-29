<template>
    <div class="w-full px-3 md:px-8 pt-6 max-w-[1800px] mx-auto flex flex-col gap-5">
        <div v-for="e in product" :key="e.name" class=" p-3">
            <div class="flex items-center justify-between">
                <p class="text-2xl font-medium text-main">
                    {{ e.name1 }} <span class="text-lg">({{ e.products.length }})</span>
                </p>
                <!-- :to="`/productlist/event/${e.name}`" -->
                <router-link to="/"
                    class="px-4 py-1 cursor-pointer text-primary font-bold ">
                    See all
                </router-link>
            </div>
            <div class="pt-3  overflow-x-auto scrollbar-thin flex gap-2 md:gap-3">
                <div class="border w-[16%] min-w-[160px] md:min-w-[180px] hover:shadow-xl cursor-pointer rounded-sm bg-white relative" v-for="product in e.products" :key="product.name">
                    <router-link 
                    :to="{ name: 'ProductDetails', params: { name: product.name } }" target="_blank"
                    >
                    <div class="w-full overflow-hidden rounded-t-sm relative">
                        <div class="-top-0.5 -left-0.5 absolute ">
                            <svg width="34" height="30" viewBox="0 0 29 28" fill="none"
                                xmlns="http://www.w3.org/2000/svg">
                                <path
                                    d="M28.9499 0C28.3999 0 27.9361 1.44696 27.9361 2.60412V27.9718L24.5708 25.9718L21.2055 27.9718L17.8402 25.9718L14.4749 27.9718L11.1096 25.9718L7.74436 27.9718L4.37907 25.9718L1.01378 27.9718V2.6037C1.01378 1.44655 0.549931 0 0 0H28.9499Z"
                                    fill="#538CEE"></path>
                            </svg>
                            <span v-if="product.discounts"
                                class="top-0.5 absolute rounded-br-md px-2 text-white text-[9px] font-medium flex flex-col">{{
                                    product.discounts }}% <span>OFF</span></span>
                        </div>
                        <div class="max-h-36 min-h-36 flex item-center justify-center">
                            <img :src="product?.images[0]?.url" alt=""
                            class="carousel__item rounded-t-sm w-full" />
                        </div>
                        
                    </div>
                    <div class="w-full p-2 flex flex-col gap-2">
                        <p class="text-sm text-main">{{ product.name1 }}</p>
                        <div class="flex justify-between items-end">
                            <div class="flex flex-col gap-1">
                                <span class="flex items-center text-secondary">
                                    <FeatherIcon name="dollar-sign" class="w-4 h-4" />{{ Math.ceil(product.final_price)
                                    }}
                                </span>
                                <template v-if="product.discounts">
                                    <del class="flex items-center text-sm text-gray-700 text-tatary">
                                        <FeatherIcon name="dollar-sign" class="w-3 h-3" />{{ product.price }}
                                    </del>
                                </template>
                            </div>
                        </div>
                        <!-- <span class="text-center py-0.5 bg-blue-100 text-xs text-main">{{ product.category }}</span> -->
                    </div>
                </router-link>
                <Button @click="add_to_cart(product.name)" :variant="'outline'" theme="blue" size="md" label="ADD" :loading="false" :loadingText="null"
                    :disabled="false" :link="null" class="px-4  absolute bottom-2 right-2">
                    ADD
                </Button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, inject } from 'vue';
import { Button } from 'frappe-ui'

const product = ref([]);
const call = inject('$call');
const getProducts = async () => {
    try {
        const response = await call('hrs.controllers.product.get_event_by_product', {});
        product.value = response;
    } catch (error) {
        console.log(error);

    }
};
const add_to_cart = async (item) => {
    try {
        const response = await call('hrs.controllers.api.add_to_cart', {product: item });
        console.log(response);
    } catch (error) {
        console.log(error);

    }
};

onMounted(() => {
    getProducts();
});
</script>