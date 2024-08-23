<template>
    <div class="w-full fixed top-0 h-12 md:h-14 z-40 bg-gray-200 shadow-sm">
      <div class="px-3 md:px-8 flex justify-between items-center h-full max-w-[1600px] mx-auto w-full">
        <router-link to="/" class="text-xl font-medium text-secondary cursor-pointer">HRS</router-link>
        <GlobalSearch />
  
        <div class="flex items-center gap-3 md:gap-6">
          <router-link 
            v-if="userDetails?.role !== 'SELLER'" 
            to="/becomeseller" 
            class="border hidden md:block px-3 py-[7px] font-medium text-sm hover:bg-primary hover:text-white transition-all truncate"
          >
            <Button
              variant="outline"
              theme="gray"
              size="md"
              label="BECOME A SELLER"
            />
          </router-link>
          
          <router-link 
            v-if="userDetails?.role === 'SELLER' || userDetails?.role === 'ADMIN'" 
            to="/dashboard" 
            class="border px-5 py-[7px] font-medium text-sm hidden md:block bg-white hover:bg-primary hover:text-white transition-all"
          >
            Dashboard
          </router-link>
          <Dropdown v-if="userDetails?.name"
          :options="[
            {
              label: 'Profile',
              onClick: () => {},
            },
            {
              label: 'Logout',
              onClick: () => {},
            },
           
          ]"
          :button="{
            label: userDetails?.name,
            variant:'outline',
            theme:'gray',
            size:'md',
          }"
        />
        <SingIn v-else/>
         
  
          <router-link v-if="route.path !== '/cart'" to="/cart" class="order-1 md:order-2 relative">
            <!-- <IoMdBasket class="text-2xl text-gray-600 cursor-pointer" /> -->
            <span v-if="count >= 1" class="w-4 h-4 rounded-full absolute -top-1 -right-2 flex items-center justify-center bg-primary text-xs font-bold text-white">{{ count }}</span>
          </router-link>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, onMounted, watch, computed } from 'vue';
  import { useRoute } from 'vue-router';
  import GlobalSearch from './GlobalSearch.vue';
  import SingIn from '../pages/SingIn.vue';
  import { Button, Dropdown } from 'frappe-ui';
  
  export default {
    components: { 
      Button,
      GlobalSearch,
      SingIn,
      Dropdown
    },
    setup() {
      const count = ref(0);
      const isRender = ref(false);
      const logInPage = ref(false);
      const userDetails = ref(JSON.parse(sessionStorage.getItem('userDetails') || '{}'));
      const route = useRoute();
  
      const signOut = () => {
        sessionStorage.clear();
        isRender.value = !isRender.value;
      };
  
      const toggleLogin = () => {
        logInPage.value = !logInPage.value;
      };
  
      const getCart = async () => {
        try {
          const response = await fetch('/your-api-endpoint'); // Replace with your actual API call
          const data = await response.json();
          count.value = data?.count || 0;
        } catch (error) {
          console.error(error);
          count.value = 0;
        }
      };
  
      watch(isRender, getCart, { immediate: true });
  
      onMounted(() => {
        userDetails.value = JSON.parse(sessionStorage.getItem('userDetails') || '{}');
      });
  
      const firstName = computed(() => userDetails.value?.name?.split(' ')[0]);
  
      return {
        count,
        signOut,
        toggleLogin,
        userDetails,
        route,
        firstName
      };
    },
  };
  </script>
  
  <style scoped>
  /* Add your styles here */
  </style>
  