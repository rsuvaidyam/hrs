<template>
  <Button v-if="product?.count == 0" @click="add_to_cart(product.name, 'plus')" :variant="'outline'" theme="blue"
    size="md" label="ADD" :loading="false" :loadingText="null" :disabled="false" :link="null" class="px-4 w-full">
    ADD
  </Button>
  <div v-else class="bg-primary rounded-[5px] w-full h-8 flex justify-around items-center text-white">
    <div class="w-2/5 flex justify-center cursor-pointer" @click="add_to_cart(product.name, 'minus')">
      <FeatherIcon name="minus" class="w-3 text-white"/>
    </div>
    <span class="text-xs w-1/5 font-medium flex justify-center">{{ product?.count }}</span>
    <div class="w-2/5 flex justify-center cursor-pointer" @click="add_to_cart(product.name, 'plus')">
      <FeatherIcon name="plus" class="w-3 text-white"/>
    </div>
  </div>
</template>
<script setup>
import { ref, onMounted, inject } from 'vue';
import { Button } from 'frappe-ui';
const call = inject('$call');
const store = inject('store');
const props = defineProps(['product', 'products']);
const product = ref(props.product);
const products = ref(props.products);
const add_to_cart = async (item, event) => {
 
  let originalCount;
  if (products?.value?.length > 0) {
    products?.value?.map((p) => {
      if (p?.name == item) {
        originalCount = p.count;
        p.count = event === 'plus' ? p?.count + 1 : p?.count - 1;
      }
    });
  } else {
    if (products.value.name == item) {
      originalCount = products.value.count;
      products.value.count = event === 'plus' ? products.value.count + 1 : products.value.count - 1;
    }
  }

  try {
    const response = await call('hrs.controllers.api.add_to_cart', { product: item, event: event });
    if (products?.value?.length > 0) {
      products?.value?.map((p) => {
        if (p.name == item) {
          p.count = response?.data?.count ?? 0;
        }
      });
    } else {
      products.value.count = response?.data?.count ?? 0;
    }
    updateCartCount()
  } catch (error) {
    if (products?.value?.length > 0) {
      products?.value?.map((p) => {
        if (p.name == item) {
          p.count = originalCount;
        }
      });
    } else {
      products.value.count = originalCount;
    }
  }
};
const updateCartCount = () => {
  let uniqueProductsCount = 0;
  if (products?.value?.length > 0) {
    products?.value?.map((p) => {
      if (p.count > 0) {
        uniqueProductsCount++;
      }
    });
  } else {
    if (products.value.count > 0) {
      uniqueProductsCount++;
    }
  }
  store.cart_count = uniqueProductsCount;
};



</script>