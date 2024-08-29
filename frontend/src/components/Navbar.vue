<template>
  <div class="w-full fixed top-0 h-12 md:h-14 z-40 bg-primary shadow-sm">
    <div class="px-3 pt-2 md:pt-0 md:px-8 flex justify-between items-center h-full max-w-[1800px] mx-auto w-full">
      <router-link to="/" class="text-xl font-medium text-white cursor-pointer">HRS</router-link>
      <div class="text-white cursor-pointer">
        <div class="flex items-center border px-2 py-0.5 rounded-md" @click="store.openpop = true">
          <p v-if="store.location_ditecter" class="text-sm font-medium">New Delhi, Delhi 841311, India</p>
          <p v-else class="text-sm">Select Location</p>
          <FeatherIcon name="chevron-down" class="w-5 h-5" />
        </div>
      </div>
      <div class="flex items-center gap-3 md:gap-6">
        <div class="hidden md:block w-96">
          <GlobalSearch />
        </div>
        <Dropdown v-if="$auth.isLoggedIn" :options="dropdownOptions" :button="dropdownButton" />
        <Login v-else />
        <router-link v-if="route.path !== '/cart'" to="/cart"
          class="order-1 md:order-2 hidden md:block text-white relative">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
            stroke="currentColor" class="size-7">
            <path stroke-linecap="round" stroke-linejoin="round"
              d="M15.75 10.5V6a3.75 3.75 0 1 0-7.5 0v4.5m11.356-1.993 1.263 12c.07.665-.45 1.243-1.119 1.243H4.25a1.125 1.125 0 0 1-1.12-1.243l1.264-12A1.125 1.125 0 0 1 5.513 7.5h12.974c.576 0 1.059.435 1.119 1.007ZM8.625 10.5a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm7.5 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Z" />
          </svg>
          <span v-if="count >= 1"
            class="w-4 h-4 rounded-full bg-white border border-gray-900 absolute -top-1 -right-2 flex items-center justify-center bg-primary text-xs font-bold text-gray-700">{{
            count }}</span>
        </router-link>
      </div>
    </div>
    <div class="block md:hidden bg-primary w-full px-4 h-10">
      <GlobalSearch />
    </div>
  </div>
  <div v-if="route.fullPath == '/'" class="w-full block md:hidden text-white">
    <router-link v-if="route.path !== '/cart'" to="/cart"
      class="w-[90%] left-[5%] z-20 fixed bottom-4 bg-primary py-2 px-4 rounded-md flex justify-between items-center">
      <div class="relative">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
          class="size-12">
          <path stroke-linecap="round" stroke-linejoin="round"
            d="M15.75 10.5V6a3.75 3.75 0 1 0-7.5 0v4.5m11.356-1.993 1.263 12c.07.665-.45 1.243-1.119 1.243H4.25a1.125 1.125 0 0 1-1.12-1.243l1.264-12A1.125 1.125 0 0 1 5.513 7.5h12.974c.576 0 1.059.435 1.119 1.007ZM8.625 10.5a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm7.5 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Z" />
        </svg>
        <span v-if="count >= 1"
          class="w-6 h-6 rounded-full absolute top-2 border-[3px] border-white left-7 flex items-center justify-center bg-primary text-md font-bold ">{{
          count }}</span>
      </div>
      <div class="flex items-center">
        <p class="text-xl font-medium">View Cart</p>
        <FeatherIcon name="chevron-right" class="w-5 h-5" />
      </div>
    </router-link>
  </div>
</template>

<script>
import { ref, onMounted, watch, computed, inject } from 'vue';
import { useRoute } from 'vue-router';
import GlobalSearch from './GlobalSearch.vue';
import Login from '../pages/Login.vue';
import { Dropdown } from 'frappe-ui';
export default {
  inject: ['$auth', '$call', '$session', '$socket', 'store'],
  components: {
    GlobalSearch,
    Login,
    Dropdown,
  },
  setup() {
    const count = ref(0);
    const store = inject('store');
    const route = useRoute();
    const auth = inject('$auth');
    const call = inject('$call');
    const session = inject('$session');

    const getCart = async () => {
      try {
        const response = auth.isLoggedIn ? await call('hrs.controllers.cart.cart_count', { usr: session.user }) : 0;
        count.value = response || 0;
      } catch (error) {
        console.error(error);
        count.value = 0;
      }
    };

    watch(() => auth.isLoggedIn, getCart, { immediate: true });

    const dropdownOptions = [
      {
        label: 'Profile',
        onClick: () => { /* Profile functionality */ },
      },
      {
        label: 'Logout',
        onClick: () => { auth.logout(); },
      },
    ];

    const dropdownButton = {
      label: auth.cookie.full_name?.split(' ')[0][0],
      variant: 'outline',
      theme: 'gray',
      size: 'md',
    };

    onMounted(() => {
      console.log('Component mounted...');
      // Optional: Setup socket events if needed
    });

    return {
      count,
      route,
      store,
      dropdownOptions,
      dropdownButton,
    };
  },
};
</script>

<style scoped>
/* Add your styles here */
</style>
