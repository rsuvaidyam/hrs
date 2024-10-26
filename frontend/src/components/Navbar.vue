<template>
  <div class="w-full fixed top-0 h-12 md:h-14 z-40 bg-primary shadow-sm">
    <div class="px-3 pt-2 md:pt-0 md:px-8 flex justify-between items-center h-full max-w-[1800px] mx-auto w-full">
      <router-link to="/" class="text-xl font-medium text-white cursor-pointer">HRS</router-link>
      <div class="text-white cursor-pointer">
        <div class="flex items-center px-2 py-0.5 rounded-md" @click="store.openpop = true">
          <p v-if="store.location_ditecter" class="font-medium truncate md:w-auto w-56 ">{{ store.address }}</p>
          <p v-else class="text-sm">Select Location</p>
          <FeatherIcon name="chevron-down" class="w-5 h-5" />
        </div>
      </div>
      <div class="flex items-center gap-3 md:gap-6">
        <div class="hidden lg:block w-96">
          <GlobalSearch />
        </div>
        <Dropdown v-if="$auth.isLoggedIn" :options="dropdownOptions" :button="dropdownButton" />
        <Login v-else />
        <router-link v-if="route.path !== '/cart'" to="/cart"
          class="order-1 md:order-2 hidden lg:block text-white relative">
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
    <div class="block lg:hidden bg-primary w-full px-4 h-10">
      <GlobalSearch />
    </div>
  </div>
  <div v-if="route.fullPath != '/cart'" class="w-full block text-white">
    <router-link v-if="!['/cart','/order'].includes(route.path)  && count >= 1" to="/cart"
      class="w-fit z-20 fixed bottom-16 right-4 bg-primary py-3 px-3 rounded-md flex justify-between items-center transition-opacity duration-500">
      <div class="relative">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
          class="size-8">
          <path stroke-linecap="round" stroke-linejoin="round"
            d="M15.75 10.5V6a3.75 3.75 0 1 0-7.5 0v4.5m11.356-1.993 1.263 12c.07.665-.45 1.243-1.119 1.243H4.25a1.125 1.125 0 0 1-1.12-1.243l1.264-12A1.125 1.125 0 0 1 5.513 7.5h12.974c.576 0 1.059.435 1.119 1.007ZM8.625 10.5a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm7.5 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Z" />
        </svg>
        <span v-if="count >= 1"
          class="w-5 h-5 rounded-full absolute top-0 border-[3px] border-white left-5 flex items-center justify-center bg-primary text-xs font-bold ">{{
          count }}</span>
      </div>
    </router-link>
  </div>
</template>

<script>
import { ref, onMounted, watch, computed, inject } from 'vue';
import { useRoute,useRouter } from 'vue-router';
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
    const router = useRouter();
    const auth = inject('$auth');
    const call = inject('$call');
    const session = inject('$session');

    if(store.cart_count){
      count.value = store.cart_count;
    }

    const getCart = async () => {
      try {
        const response = auth.isLoggedIn ? await call('hrs.controllers.api.cart_count', { usr: session.user }) : 0;
        count.value = response || 0;
        store.cart_count = response;
      } catch (error) {
        console.error(error);
        count.value = 0;
      }
    };

    // watch(() => store.address, { immediate: true });
    watch(() => auth.isLoggedIn, getCart, { immediate: true });
    watch(() => store.cart_count, getCart);



    const dropdownOptions = [
      {
        label: 'Profile',
        onClick: () => { /* Profile functionality */ },
      },
      {
        label: 'My Orders',
        onClick: () => { router.push({name:'MyOrder'}); },
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
