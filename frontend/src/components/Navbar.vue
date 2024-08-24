<template>
  <div class="w-full fixed top-0 h-12 md:h-14 z-40 bg-[#982B1C] shadow-sm">
    <div class="px-3 md:px-8 flex justify-between items-center h-full max-w-[1800px] mx-auto w-full">
      <router-link to="/" class="text-xl font-medium text-secondary cursor-pointer">HRS</router-link>
      
      <div class="flex items-center gap-3 md:gap-6">
        <GlobalSearch />
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
        <Login v-else />
        <router-link v-if="route.path !== '/cart'" to="/cart" class="order-1 md:order-2 text-white relative">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
            stroke="currentColor" class="size-7">
            <path stroke-linecap="round" stroke-linejoin="round"
              d="M15.75 10.5V6a3.75 3.75 0 1 0-7.5 0v4.5m11.356-1.993 1.263 12c.07.665-.45 1.243-1.119 1.243H4.25a1.125 1.125 0 0 1-1.12-1.243l1.264-12A1.125 1.125 0 0 1 5.513 7.5h12.974c.576 0 1.059.435 1.119 1.007ZM8.625 10.5a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm7.5 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Z" />
          </svg>
          <span  v-if="count >= 1"
            class="w-4 h-4 rounded-full bg-white border border-gray-900 absolute -top-1 -right-2 flex items-center justify-center bg-primary text-xs font-bold text-gray-700">{{
            count }}</span>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, watch, computed,inject } from 'vue';
import { useRoute } from 'vue-router';
import GlobalSearch from './GlobalSearch.vue';
import Login from '../pages/Login.vue';
import { Button, Dropdown } from 'frappe-ui';

export default {

  inject: ['$auth','$call'],
  components: {
    Button,
    GlobalSearch,
    Login,
    Dropdown,
  },
  setup() {
    const count = ref(0);
    const isRender = ref(false);
    const logInPage = ref(false);
    const route = useRoute();

    const signOut = () => {
      sessionStorage.clear();
      isRender.value = !isRender.value;
    };

    const call = inject('$call');
    const session = inject('$session');
    const auth = inject('$auth');
    const getCart = async () => {
      try {
        
        const response = auth.isLoggedIn && await call('hrs.controllers.cart.cart_count',{usr:session.user});  
        count.value = response || 0;
      } catch (error) {
        console.error(error);
        count.value = 0;
      }
    };

    watch(isRender, getCart, { immediate: true });

    return {
      count,
      signOut,
      route,
    };
  },
};
</script>

<style scoped>
/* Add your styles here */
</style>