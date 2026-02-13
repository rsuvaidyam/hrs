<template>
  <div class="pt-12 md:pt-14 w-full h-full pb-3 max-w-[1600px] mx-auto">
    <ProductFilters v-model="filters" @update:modelValue="fetchProducts" />
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
              <Item :product="product" />
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
import { ref, onMounted, watch, inject } from 'vue';
import { useRoute } from 'vue-router';
import { Spinner } from 'frappe-ui';
import Item from './Item.vue';
import ProductFilters from './ProductFilters.vue';

const route = useRoute();
const location = route.fullPath.split('/');

const products = ref([]);
const loading = ref(true);
const filters = ref({});
const call = inject('$call');

async function fetchProducts() {
  loading.value = true;
  try {
    const data = { ...filters.value };
    if (location[2] === 'category') data.category = location[3];
    else if (location[2] === 'event') data.event = location[3];
    const response = await call('hrs.controllers.api.products_list', { data });
    const list = Array.isArray(response) ? response : (response && response.message) ? response.message : [];
    products.value = list || [];
  } catch (e) {
    console.error(e);
    products.value = [];
  } finally {
    loading.value = false;
  }
}

onMounted(fetchProducts);
watch(() => route.fullPath, fetchProducts);

</script>

<style scoped>
/* Add any necessary styles here */
</style>