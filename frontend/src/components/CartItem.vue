<template>
  <div class="lg:h-28 py-3 relative border-b flex transition-transform duration-1000 gap-4">
    <img class="h-20 w-20 lg:h-full rounded-md" :src="product?.images[0]?.image"
      :alt="product?.product?.name" />
    <div class="flex flex-col gap-1 justify-around">
      <div class="flex flex-col gap-2">
        <router-link :to="`/productdetails/${product?.product?.name}`" >
          <p class="text-sm font-light md:text-lg group-hover:underline">{{ product?.product?.name1 }}</p>
        </router-link>
        <!-- <p class="truncate text-sm">
          <span class="text-gray-500">Flavour : </span>
          <span class="bg-gray-100 rounded-md p-1 text-gray-700 font-medium text-xs">{{ product?.product?.category
            }}</span>
        </p> -->
      </div>
      <p class="text-sm font-extralight">{{ product?.product.qty }} {{ product.product.unit }}</p>
      <div class="flex gap-2 font-normal">
        <p class="flex items-center gap-0.5 text-primary">
          <span>₹</span>
          {{ formattedPrice }}
        </p>
        <template v-if="product.product.discounts">
          <del class="flex items-center gap-0.5 text-sm text-gray-700">
            <span>₹</span>
            {{ originalPrice }}
          </del>
        </template>
      </div>
    </div>
    <div v-if="product?.product?.discounts != 0"
      class="absolute flex flex-col items-center justify-center text-white top-0 right-0">
      <div class="relative flex h-8 w-8">
        <span class="absolute inline-flex h-full w-full">
          <svg width="34" height="30" viewBox="0 0 29 28" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path
              d="M28.9499 0C28.3999 0 27.9361 1.44696 27.9361 2.60412V27.9718L24.5708 25.9718L21.2055 27.9718L17.8402 25.9718L14.4749 27.9718L11.1096 25.9718L7.74436 27.9718L4.37907 25.9718L1.01378 27.9718V2.6037C1.01378 1.44655 0.549931 0 0 0H28.9499Z"
              fill="#538CEE"></path>
          </svg>
        </span>
        <div class="relative inline-flex items-center justify-center px-1">
          <span class="text-xs font-medium">{{ product?.product?.discounts }}%</span>
        </div>
      </div>
    </div>
    <div class="absolute bottom-2 right-2">
      <div class="bg-primary rounded-[5px] w-16 h-8 flex justify-around items-center text-white">
        <FeatherIcon name="minus" class="w-3 text-white cursor-pointer"
          @click="add_to_cart(product?.product.parent, 'minus',product?.product.name)" />
        <span class="text-xs font-medium">{{ product.count }}</span>
        <FeatherIcon name="plus" class="w-3 text-white cursor-pointer"
          @click="add_to_cart(product?.product.parent, 'plus',product?.product.name)" />
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, computed, inject } from 'vue';
import { Select, FormControl } from 'frappe-ui';

export default defineComponent({
  name: 'CartItem',
  props: {
    product: {
      type: Object,
      required: true,
    },
  },
  setup(props) {
    const call = inject('$call');  
    const store = inject('store'); 
    const originalPrice = computed(() => props.product.product.price * props.product.count);
    const formattedPrice = computed(() => {
      if (props.product.product.discounts) {
        return Math.ceil(props.product.product.final_price) * props.product.count;
      }
      return originalPrice.value;
    });

    const add_to_cart = async (item, event,option) => {
      let originalCount = props.product.count;
      if (event === 'plus') {
        props.product.count++;
      } else if (event === 'minus' && props.product.count > 0) {
        props.product.count--;
      }

      try {
        const response = await call('hrs.controllers.api.add_to_cart', { product: item, event: event,option:option });
        props.product.count = response?.data?.count ?? 0;
        updateCartCount();
      } catch (error) {
        props.product.count = originalCount;
        console.log(error);
      }
    };
    const updateCartCount = () => {
      let uniqueProductsCount = 0;
        if (props.product.count > 0) {
          uniqueProductsCount++;
        }
      store.cart_count = uniqueProductsCount;
    };

    return { originalPrice, formattedPrice, add_to_cart };
  },
  components: { Select, FormControl },
});
</script>

<style scoped>
/* Add your styles here */
</style>
