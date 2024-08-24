<!-- src/components/CartItem.vue -->
<template>
    <div class="lg:h-36 p-3 text-gray-800 relative border-b flex flex-col lg:flex-row justify-between">
      <input
        type="checkbox"
        class="absolute top-4 right-4"
        :checked="isSelected"
        @change="handleSelect"
      />
      <router-link :to="`/productdetails/${product.product._id}`" class="flex gap-2 lg:gap-4 group">
        <img class="h-20 lg:h-full rounded-md" :src="product.product.images[0]?.url" :alt="product.product.name" />
        <div class="flex flex-col gap-1 justify-between">
          <div class="flex flex-col gap-2">
            <p class="text-sm md:text-lg truncate group-hover:underline">{{ product.product.name }}</p>
            <p class="truncate text-sm">
              <span class="text-gray-500">Flavour : </span>
              <span class="bg-gray-100 rounded-md p-1 text-gray-700 font-medium text-xs">{{ product.product.category.name }}</span>
            </p>
          </div>
          <div class="flex items-center gap-2">
            <div class="bg-primary rounded-sm w-14 px-2.5 text-sm text-white flex items-center gap-1">
              4.3 
              <!-- <BsStarHalf class="text-xs" /> -->
            </div>
            <span class="flex items-center text-lg text-primary">
              <!-- <BiRupee class="text-md" /> -->
              {{ formattedPrice }}
            </span>
            <template v-if="product.product.discounts">
              <del class="flex items-center text-sm text-gray-700">
                <!-- <BiRupee class="text-base" /> -->
                {{ originalPrice }}
              </del>
              <span class="text-green-500 text-sm font-medium">{{ product.product.discounts }}% off</span>
            </template>
          </div>
        </div>
      </router-link>
      <div class="flex flex-row-reverse lg:flex-col items-center justify-between">
        <!-- <RiDeleteBin6Line class="text-xl text-red-500 cursor-pointer" @click="handleDelete" /> -->
        <div class="flex gap-2 items-center">
          <div class="flex bg-gray-100 text-sm px-1.5 py-0.5 rounded-sm">
            <button class="cursor-text text-sm">Qty :</button>
            <select v-model="count" class="outline-none cursor-pointer" @change="handleQuantityChange">
              <option v-for="n in [1, 2, 3]" :key="n" :value="n">{{ n }}</option>
            </select>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent, computed } from 'vue';
 
  
  export default defineComponent({
    name: 'CartItem',
    props: {
      product: {
        type: Object as () => Product,
        required: true,
      },
      isSelected: {
        type: Boolean,
        required: true,
      },
    },
    emits: ['delete', 'quantityChange', 'select'],
    setup(props, { emit }) {
      const count = computed(() => props.product.count);
  
      const handleDelete = () => emit('delete', props.product._id);
      const handleQuantityChange = () => emit('quantityChange', props.product._id, count.value);
      const handleSelect = () => emit('select', props.product._id);
  
      const originalPrice = computed(() => props.product.product.price * props.product.count);
      const formattedPrice = computed(() => {
        if (props.product.product.discounts) {
          return Math.ceil((100 - props.product.product.discounts) / 100 * props.product.product.price) * props.product.count;
        }
        return originalPrice.value;
      });
  
      return { count, handleDelete, handleQuantityChange, handleSelect, originalPrice, formattedPrice };
    },
    components: {  },
  });
  </script>
  
  <style scoped>
  /* Add your styles here */
  </style>
  