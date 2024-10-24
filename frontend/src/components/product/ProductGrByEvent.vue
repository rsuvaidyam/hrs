<template>
    <div class="w-full px-1 md:px-5 max-w-[1800px] mx-auto flex flex-col">
        <div v-for="[event_name, products] in Object.entries(product)" :key="event_name" class=" p-3">
            <div class="flex items-center justify-between">
                <p class="text-2xl font-medium text-main">
                    {{ event_name }} <span class="text-lg">({{ products.length }})</span>
                </p>
                <router-link :to="`/product-list/event/${products[0].events}`" class="px-4 py-1 cursor-pointer text-primary font-bold ">
                    See all
                </router-link>
            </div>
            <div class="pt-3  overflow-x-auto scrollbar-thin flex gap-2 md:gap-3">
                <div class="border w-[16%] min-w-[160px] md:min-w-[180px] hover:shadow-xl cursor-pointer rounded-sm bg-white relative"
                    v-for="product in products" :key="product.name">
                    <Item :product="product" />
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, inject } from 'vue';
import Item from '../product/Item.vue';

const product = ref([]);
const call = inject('$call');
const getProducts = async () => {
    try {
        const response = await call('hrs.controllers.api.get_event_by_product', {});
        product.value = response;
    } catch (error) {
        console.log(error);

    }
};
onMounted(() => {
    getProducts();
});
</script>