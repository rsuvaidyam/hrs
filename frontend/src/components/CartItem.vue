<!-- src/components/CartItem.vue -->
<template>
  <div class="lg:h-36 p-3 text-gray-800 relative border-b flex flex-col lg:flex-row justify-between">
    <FormControl
    type="checkbox"
    size="sm"
    variant="subtle"
    placeholder="Placeholder"
    :disabled="false"
    label=""
    v-model="isSelected"
    @change="handleSelect"
    class="absolute top-2 right-2"
  />
    <router-link :to="`/productdetails/${product?.product?.name}`" class="flex gap-2 lg:gap-4 group">
      <img class="h-20 w-20 lg:h-full rounded-md" :src="product?.product?.images[0]?.image"
        :alt="product?.product?.name1" />
      <div class="flex flex-col gap-1 justify-between">
        <div class="flex flex-col gap-2">
          <p class="text-sm md:text-lg truncate group-hover:underline">{{ product?.product?.name1 }}</p>
          <p class="truncate text-sm">
            <span class="text-gray-500">Flavour : </span>
            <span class="bg-gray-100 rounded-md p-1 text-gray-700 font-medium text-xs">{{ product?.product?.category
              }}</span>
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
            <span class="text-green-500 text-sm font-medium">{{ product?.product?.discounts }}% off</span>
          </template>
        </div>
      </div>
    </router-link>
    <div class="flex flex-row-reverse lg:flex-col items-center pt-2 lg:pt-0 justify-between">
       <FeatherIcon name="trash-2" class="w-5 text-red-500 cursor-pointer" @click="handleDelete" />
      <div class="flex gap-2 items-center">
        <div class="flex bg-gray-100 text-sm px-1.5  rounded-sm">
          <button class="cursor-text text-sm">Qty :</button>

          <Select class="pr-7" v-model="count" :options="[
            {
              label: '1',
              value: '1',
            },
            {
              label: '2',
              value: '2',
            },
            {
              label: '3',
              value: '3',
            },

          ]" @change="handleQuantityChange" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, computed } from 'vue';
import { Select,FormControl } from 'frappe-ui';

export default defineComponent({
  name: 'CartItem',
  props: {
      product: {
        type: Object,
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

    const handleDelete = () => emit('delete', props.product.name);
    const handleQuantityChange = () => emit('quantityChange', props.product.name, count.value);
    const handleSelect = () => emit('select', props.product.name);

    const originalPrice = computed(() => props.product.product.price * props.product.count);
    const formattedPrice = computed(() => {
      if (props.product.product.discounts) {
        return Math.ceil(props.product.product.final_price) * props.product.count;
      }
      return originalPrice.value;
    });

    return { count, handleDelete, handleQuantityChange, handleSelect, originalPrice, formattedPrice };
  },
  components: { Select,FormControl },
});
</script>

<style scoped>
/* Add your styles here */
</style>