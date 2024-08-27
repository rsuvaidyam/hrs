<template>
    <div class="px-2 md:px-8 py-2 flex items-center gap-3 md:gap-5 overflow-x-scroll scrollbar-thin">
      <CategoryLoader v-if="loader" />
      <div v-else v-for="category in categoryList" :key="category.name">
        <router-link :to="`/productlist/category/${category.name}`" class="flex flex-col items-center cursor-pointer">
          <div class="md:w-28 w-16 rounded-full md:rounded-2xl border-2 ">
            <img class="rounded-full md:rounded-3xl" :src="category?.image" alt="" />
          </div>
          <p class="text-xs md:text-lg truncate text-main font-medium">{{ category.name1 }}</p>
        </router-link>
      </div>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent, ref, onMounted,computed ,inject} from 'vue';
  import CategoryLoader from '@/components/Loader/CategoryLoader.vue';
  
  export default defineComponent({
    name: 'CategoryList',
    components: {
      CategoryLoader,
    },
    setup() {
      const categoryList = ref([]);
      const loader = ref(true);
     const call = inject('$call');
      const getCategory = async () => {
        loader.value = true;
        try {
          const response = await call('hrs.controllers.api.get_category', {});
          setTimeout(() => {
            loader.value = false;
          }, 1000);
          categoryList.value = response;
        } catch (error: any) {
          console.log(error);
          
        }
      };
  
      onMounted(() => {
        getCategory();
      });
  
      return {
        categoryList,
        loader,
      };
    },
  });
  </script>
  