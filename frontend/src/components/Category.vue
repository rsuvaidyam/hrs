<template>
    <div class="px-2 md:px-8 py-2 flex flex-wrap items-center gap-3 md:gap-5">
      <CategoryLoader v-if="loader" />
      <div v-else v-for="category in categoryList" :key="category.name">
        <!-- :to="`/productlist/category/${category.name}`" -->
        <router-link to="/" class="flex flex-col items-center cursor-pointer">
          <div class="md:w-28 w-16 h-20 md:h-28 bg-blue-100 rounded-md ">
            <!-- <img class="w-full h-full" :src="category?.image" alt="" /> -->
          </div>
          <p class="text-xs md:text-lg pt-2 truncate text-main font-medium">{{ category.name1 }}</p>
        </router-link>
      </div>
    </div>
  </template>
  
  <script >
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
        } catch (error) {
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
  