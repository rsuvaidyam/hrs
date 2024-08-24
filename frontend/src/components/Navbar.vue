<template>
  <div class="w-full fixed top-0 h-12 md:h-14 z-40 bg-gray-200 shadow-sm">
    <div class="px-3 md:px-8 flex justify-between items-center h-full max-w-[1600px] mx-auto w-full">
      <router-link to="/" class="text-xl font-medium text-secondary cursor-pointer">HRS</router-link>
      
      <div class="flex items-center gap-3 md:gap-6">
        <GlobalSearch />
        <router-link v-if="userDetails?.role === 'SELLER' || userDetails?.role === 'ADMIN'" to="/dashboard"
          class="border px-5 py-[7px] font-medium text-sm hidden md:block bg-white hover:bg-primary hover:text-white transition-all">
          Dashboard
        </router-link>
        <Dropdown v-if="$auth.isLoggedIn" :options="[
          {
            label: 'Profile',
            onClick: () => { },
          },
          {
            label: 'Logout',
            onClick: () => { $auth.logout() },
          },

        ]" :button="{
            label: $auth.cookie.full_name?.split(' ')[0].split('')[0],
            variant: 'outline',
            theme: 'gray',
            size: 'md',
          }" />
        <SingIn v-else />


        <router-link v-if="route.path !== '/cart'" to="/cart" class="order-1 md:order-2 relative">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
            stroke="currentColor" class="size-6">
            <path stroke-linecap="round" stroke-linejoin="round"
              d="M15.75 10.5V6a3.75 3.75 0 1 0-7.5 0v4.5m11.356-1.993 1.263 12c.07.665-.45 1.243-1.119 1.243H4.25a1.125 1.125 0 0 1-1.12-1.243l1.264-12A1.125 1.125 0 0 1 5.513 7.5h12.974c.576 0 1.059.435 1.119 1.007ZM8.625 10.5a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm7.5 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Z" />
          </svg>
          <span  v-if="count >= 1"
            class="w-4 h-4 rounded-full absolute -top-1 -right-2 flex items-center justify-center bg-primary text-xs font-bold text-gray-700">{{
            count }}</span>
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

  inject: ['$auth'],
  components: {
    Button,
    GlobalSearch,
    SingIn,
    Dropdown,
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
      // try {
      //   const response = await fetch('/your-api-endpoint'); // Replace with your actual API call
      //   const data = await response.json();
      //   count.value = data?.count || 0;
      // } catch (error) {
      //   console.error(error);
      //   count.value = 0;
      // }
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