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
const session = inject('$session');
const props = defineProps(['product', 'products','option']);
let product = ref(props.product);
let products = ref(props.products);
let option = ref(props.option);

watch(() => props.option, (newOption) => {
  option.value = newOption;
});
watch(() => props.product, (newVal) => {
  product.value = newVal;
});
watch(() => props.products, (newVal) => {
  products.value = newVal;
});

const add_to_cart = async (item, event, opt) => {
  let originalCount;
  if (products.value?.length > 0) {
    products.value?.forEach((p) => {
      if (p?.parent == item && p.name == opt) {
        originalCount = p.count;
        p.count = event === 'plus' ? (p?.count ?? 0) + 1 : Math.max(0, (p?.count ?? 0) - 1);
      }
    });
  }

  try {
    const response = await call('hrs.controllers.api.add_to_cart', { product: item, event: event, option: opt });
    if (products.value?.length > 0) {
      products.value?.forEach((p) => {
        if (p.parent == item && p.name == opt) {
          p.count = response?.data?.count ?? 0;
        }
      });
    }
    const count = await call('hrs.controllers.api.cart_count', { usr: session?.user });
    store.cart_count = count ?? 0;
  } catch (error) {
    if (products.value?.length > 0 && originalCount !== undefined) {
      products.value?.forEach((p) => {
        if (p.parent == item && p.name == opt) {
          p.count = originalCount;
        }
      });
    }
  }
};



</script>