<template>
    <div class="w-full md:px-8 flex flex-col gap-5">
      <Occasion />
      <div v-for="e in product" :key="e.event.name" class="bg-white md:rounded-sm shadow-md p-3">
        <div class="flex items-center justify-between">
          <p class="text-2xl font-medium">
            {{ e.event.name }} <span class="text-lg">({{ e.products.length }})</span>
          </p>
          <router-link
            :to="`/productlist/event/${e.event.name}`"
            class="px-4 py-1 cursor-pointer text-sm font-medium bg-primary text-white"
          >
            View All
          </router-link>
        </div>
        <div class="pt-3 overflow-x-auto scrollbar-thin flex gap-2 md:gap-3">
          <router-link
            v-for="product in e.products"
            :key="product.name"
            :to="`/productdetails/${product.name}`"
            target="_blank"
            class="border w-1/5 min-w-[200px] md:min-w-[220px] hover:shadow-xl cursor-pointer rounded-sm bg-white"
          >
            <div class="w-full overflow-hidden rounded-t-sm">
              <img
                :src="product.images"
                alt=""
                class="rounded-t-sm max-h-44 w-full transition-all duration-200 hover:scale-105"
              />
            </div>
            <div class="w-full p-1 flex flex-col gap-2">
              <p class="text-sm truncate">{{ product.name }}</p>
              <div class="flex justify-between items-center">
                <div class="flex items-center gap-1">
                  <span class="flex items-center">
                    <BiRupee class="text-lg" />{{ product.discounts ? Math.ceil((100 - product.discounts) / 100 * product.price) : product.price }}
                  </span>
                  <template v-if="product.discounts">
                    <del class="flex items-center text-sm text-gray-700">
                      <BiRupee class="text-md" />{{ product.price }}
                    </del>
                    <span class="text-primary text-sm font-medium">{{ product.discounts }}% off</span>
                  </template>
                </div>
                <div class="bg-primary rounded-sm px-1 text-sm text-white flex items-center gap-1">
                  4.3 <BsStarHalf class="text-xs" />
                </div>
              </div>
              <div class="flex justify-between items-center">
                <span class="text-xs font-medium">{{ product.category }}</span>
                <div class="text-xs text-gray-500">456 Reviews</div>
              </div>
            </div>
          </router-link>
        </div>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref, onMounted } from 'vue';
  import Occasion from '../Occasion/Occasion.vue';
  
  const product = ref([]);
  
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
  