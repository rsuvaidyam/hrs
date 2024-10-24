<template>
  <Button v-if="product?.count == 0 && product.name == option" @click="add_to_cart(product.parent, 'plus',option)" :variant="'outline'" theme="blue"
    size="md" label="ADD" :loading="false" :loadingText="null" :disabled="false" :link="null" class="px-4 w-full">
    ADD
  </Button>
  <div v-else class="bg-primary rounded-[5px] w-full h-8 flex justify-around items-center text-white">
    <div class="w-2/5 flex justify-center cursor-pointer" @click="add_to_cart(product.parent, 'minus',option)">
      <FeatherIcon name="minus" class="w-3 text-white"/>
    </div>
    <span class="text-xs w-1/5 font-medium flex justify-center">{{ product?.count }}</span>
    <div class="w-2/5 flex justify-center cursor-pointer" @click="add_to_cart(product.parent, 'plus',option)">
      <FeatherIcon name="plus" class="w-3 text-white"/>
    </div>
  </div>
</template>
<script setup>
import { ref, watch, inject } from 'vue';
import { Button } from 'frappe-ui';
const call = inject('$call');
const store = inject('store');
const props = defineProps(['product', 'products','option']);
let product = ref(props.product);
let products = ref(props.products);
let option = ref(props.option);

watch(() => props.option, (newOption, oldOption) => {
  option = newOption;
});
watch(() => props.product, (newOption, oldOption) => {
  product = newOption;
});
watch(() => props.products, (newOption, oldOption) => {
  products = newOption; 
});

const add_to_cart = async (item, event,option) => {
  let originalCount;
  if (products.value?.length > 0) {
    products.value?.map((p) => {
      if (p?.parent == item && p.name == option) {
        originalCount = p.count;
        p.count = event === 'plus' ? p?.count + 1 : p?.count - 1;
      }
    });
  } 

  try {
    const response = await call('hrs.controllers.api.add_to_cart', { product: item, event: event,option:option });
    if (products.value?.length > 0) {
      products.value?.map((p) => {
        if (p.parent == item && p.name == option) {
          p.count = response?.data?.count ?? 0;
        }
      });
    } 
    updateCartCount()
  } catch (error) {
    if (products.value?.length > 0) {
      products.value?.map((p) => {
        if (p.parent == item && p.name == option) {
          p.count = originalCount;
        }
      });
    }  
  }
};

const updateCartCount = () => {
  let uniqueProductsCount = 0;
  if (products.value?.length > 0) {
    products.value?.map((p) => {
      if (p.count > 0) {
        uniqueProductsCount++;
      }
    });
  } 
  store.cart_count = uniqueProductsCount;
};



</script>