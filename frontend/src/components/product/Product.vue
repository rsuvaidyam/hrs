<template>
    <div class="pt-12 md:pt-14 w-full h-full pb-3 max-w-[1600px] mx-auto">
      <!-- <Filter /> -->
      <Spinner v-if="loading" :loading="loading" />
      <div v-else>
        <template v-if="product.length >= 1">
          <div class="w-full h-full pt-2 px-2 md:px-8">
            <div class="w-full px-2 pt-1 rounded-md text-xl flex items-center gap-3 font-medium">
              <RiCake2Line class="text-3xl" />
              {{ location.category ? product[0]?.category?.name : product[0]?.event?.name }} Cake
            </div>
            <div class="grid pt-3 grid-cols-2 gap-x-2 md:gap-x-6 gap-y-4 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5">
              <router-link
                v-for="e in product"
                :key="e._id"
                :to="'/productdetails/' + e._id"
                target="_blank"
                class="border hover:shadow-xl cursor-pointer rounded-sm"
              >
                <img
                  class="rounded-t-sm p-0.5 max-h-44 w-full"
                  :src="e.images[0]?.url"
                  alt=""
                />
                <div class="w-full p-1 flex flex-col gap-2">
                  <p class="text-sm truncate">{{ e.name }}</p>
                  <div class="flex justify-between items-center">
                    <div class="flex items-center gap-1">
                      <span class="flex items-center">
                        <BiRupee class="text-lg" />{{ e.discounts ? Math.ceil((100 - e.discounts) / 100 * e.price) : e.price }}
                      </span>
                      <template v-if="e.discounts">
                        <del class="flex items-center text-sm text-gray-700">
                          <BiRupee class="text-md" />{{ e.price }}
                        </del>
                        <span class="text-primary text-sm font-medium">{{ e.discounts }}% off</span>
                      </template>
                    </div>
                    <div class="bg-primary rounded-sm px-1 text-sm text-white flex items-center gap-1">
                      4.3 <BsStarHalf class="text-xs" />
                    </div>
                  </div>
                  <div class="flex justify-between items-center">
                    <span class="text-xs font-medium">{{ e.category?.name }}</span>
                    <div class="text-xs text-gray-500">456 Reviews</div>
                  </div>
                </div>
              </router-link>
            </div>
          </div>
        </template>
        <DataNotFound v-else />
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { useRoute } from 'vue-router';
  import Spinner from '@/Components/Loader/Spinner.vue';
  import { BiRupee, BsStarHalf, RiCake2Line } from 'vue-icons';
  
  const route = useRoute();
  const location = route.params;
  const product = ref([]);
  const loading = ref(true);
  
  onMounted(async () => {
    try {
      let data = {};
      if (location.category) {
        data.category = location.category;
      } else if (location.event) {
        data.event = location.event;
      }
  
      const response = auth.isLoggedIn && await call('hrs.controllers.product.', { data:data });
  
      product.value = response?.data?.data;
      setTimeout(() => {
        loading.value = false;
      }, 1000);
    } catch (error) {
      toast.error(error.response?.data?.message);
    }
  });
  </script>
  
  <style scoped>
  /* Add any necessary styles here */
  </style>
  