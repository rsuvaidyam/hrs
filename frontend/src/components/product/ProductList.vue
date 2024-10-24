<template>
  <div class="pt-12 md:pt-14 w-full h-full pb-3 max-w-[1600px] mx-auto">
    <!-- <Filter /> -->
     <div class="w-full h-full flex justify-center items-center" v-if="loading">
      <div class="w-14" >
        <Spinner :loading="loading" />
      </div>
    </div>
    <div v-else class="h-full">
      <template v-if="products.length >= 1">
        <div class="w-full h-full pt-2 px-2 md:px-8">
          <div class="w-full px-2 pt-1 rounded-md text-xl flex items-center gap-3 font-medium">
            <!-- <FeatherIcon name="cake" class="text-3xl" /> -->
            <!-- {{ location.category ? product[0]?.category?.name : product[0]?.event?.name }} Cake -->
          </div>
          <div class="flex flex-wrap items-center gap-5">
            <div
              class="border w-[16%] min-w-[160px] md:min-w-[180px] hover:shadow-xl cursor-pointer rounded-sm bg-white relative"
              v-for="product in products" :key="product.name">
              <router-link :key="product.name" :to="'/productdetails/' + product.name">
                <div class="w-full overflow-hidden rounded-t-sm relative">
                  <div class="-top-0.5 -left-0.5 absolute " v-if="product.discounts">
                    <svg width="34" height="30" viewBox="0 0 29 28" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path
                        d="M28.9499 0C28.3999 0 27.9361 1.44696 27.9361 2.60412V27.9718L24.5708 25.9718L21.2055 27.9718L17.8402 25.9718L14.4749 27.9718L11.1096 25.9718L7.74436 27.9718L4.37907 25.9718L1.01378 27.9718V2.6037C1.01378 1.44655 0.549931 0 0 0H28.9499Z"
                        fill="#538CEE"></path>
                    </svg>
                    <span v-if="product.discounts"
                      class="top-0.5 absolute rounded-br-md px-2 text-white text-[9px] font-medium flex flex-col">{{
                        product.discounts }}% <span>OFF</span></span>
                  </div>
                  <div class="max-h-36 min-h-36 flex item-center justify-center">
                    <img :src="product?.images[0]?.url" alt="" class="carousel__item rounded-t-sm w-full" />
                  </div>

                </div>
                <div class="w-full p-2 flex flex-col gap-2">
                  <p class="text-sm text-main">{{ product.name1 }}</p>
                  <div class="flex justify-between items-end">
                    <div class="flex flex-col gap-1">
                      <span class="flex gap-0.5 items-center text-secondary">
                        <span>₹</span>{{ Math.ceil(product.final_price)
                        }}
                      </span>
                      <template v-if="product.discounts">
                        <div class="flex gap-0.5 items-center text-sm text-gray-700 text-tatary">
                          <span>₹</span> <del>{{ product.price }}</del>
                        </div>
                      </template>
                    </div>
                  </div>
                  <!-- <span class="text-center py-0.5 bg-blue-100 text-xs text-main">{{ product.category }}</span> -->
                </div>
              </router-link>
              <div class="absolute bottom-2 right-2 w-16">
                <AddToCartBtn :product="product" :products="products" />
              </div>
            </div>
          </div>
        </div>
      </template>
      <!-- <DataNotFound v-else /> -->
      <div v-else class="w-full h-full flex justify-center items-center">
        <p class="text-3xl text-gray-500">No products found</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, inject } from 'vue';
import { useRoute } from 'vue-router';
import { Spinner } from 'frappe-ui';
import AddToCartBtn from '../AddToCartBtn.vue';
const route = useRoute();
const location = route.fullPath.split('/');

const products = ref([]);
const loading = ref(true);
const call = inject('$call');
onMounted(async () => {
  try {
    let data = {};
    if (location[2] === 'category') {
      data.category = location[3];
    } else if (location[2] === 'event') {
      data.event = location[3];
    }

    const response = await call('hrs.controllers.product.products_list', { data: data });

    products.value = response;
    setTimeout(() => {
      loading.value = false;
    }, 1000);
  } catch (error) {
    console.log(error)
  }
});

</script>

<style scoped>
/* Add any necessary styles here */
</style>