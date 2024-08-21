<template>
    <div class="w-full fixed top-0 h-12 md:h-14 z-40 bg-gray-200 shadow-sm">
      <div class="px-3 md:px-8 flex justify-between items-center h-full max-w-[1600px] mx-auto w-full">
        <router-link to="/" class="text-xl font-medium text-secondary cursor-pointer">HRS</router-link>
        <!-- <GlobalSearch /> -->
  
        <div class="flex items-center gap-3 md:gap-6">
          <router-link 
            v-if="userDetails?.role !== 'SELLER'" 
            to="/becomeseller" 
            class="border hidden md:block px-3 py-[7px] font-medium text-sm hover:bg-primary hover:text-white transition-all truncate"
          >
            BECOME A SELLER
          </router-link>
          
          <router-link 
            v-if="userDetails?.role === 'SELLER' || userDetails?.role === 'ADMIN'" 
            to="/dashboard" 
            class="border px-5 py-[7px] font-medium text-sm hidden md:block bg-white hover:bg-primary hover:text-white transition-all"
          >
            Dashboard
          </router-link>
          
          <div v-if="userDetails?.name">
            <Menu as="div" class="relative inline-block text-left">
              <Menu.Button class="inline-flex justify-center items-center gap-1.5 rounded-full md:rounded-none hover:bg-primary hover:text-white md:px-3 md:py-[7px] text-sm font-semibold text-secondary">
                <p v-if="userDetails?.name" class="hidden md:block">
                  <span class="flex gap-1 items-center">{{ firstName }}
                    <!-- <BiChevronDown class="text-xl" /> -->
                </span>
                </p>
                <div class="w-10 h-10 block md:hidden">
                  <!-- <img :src="userDetails.gender === 'FEMALE' ? avatarF : avatarM" alt="" class="rounded-full" /> -->
                </div>
              </Menu.Button>
              <Transition 
                enter="transition ease-out duration-100"
                enterFrom="transform opacity-0 scale-95"
                enterTo="transform opacity-100 scale-100"
                leave="transition ease-in duration-75"
                leaveFrom="transform opacity-100 scale-100"
                leaveTo="transform opacity-0 scale-95"
              >
                <Menu.Items class="absolute right-0 z-10 mt-2 w-48 origin-top-right rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
                  <div class="py-1">
                    <Menu.Item>
                      <router-link to="/profile/personal" class="hover:bg-gray-100 text-gray-700 hidden md:block w-full px-4 py-2 text-left text-sm">Profile</router-link>
                    </Menu.Item>
                    <Menu.Item>
                      <router-link to="/profile" class="hover:bg-gray-100 text-gray-700 md:hidden block w-full px-4 py-2 text-left text-sm">Profile</router-link>
                    </Menu.Item>
                    <Menu.Item>
                      <button type="submit" class="hover:bg-red-600 hover:text-white hover:font-semibold block w-full px-4 py-2 text-left text-red-500 text-sm" @click="signOut">Sign out</button>
                    </Menu.Item>
                  </div>
                </Menu.Items>
              </Transition>
            </Menu>
          </div>
          
          <button 
            v-else 
            @click="toggleLogin" 
            class="hover:bg-primary px-1 md:px-4 py-1 order-2 md:order-1 hover:text-white text-sm md:text-base"
          >
            Sign In
          </button>
          
          <router-link v-if="pathname !== '/cart'" to="/cart" class="order-1 md:order-2 relative">
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
// import { IoMdBasket } from 'vue-icons/io';
// import { BiChevronDown } from 'vue-icons/bi';
// import { Menu, Transition } from '@headlessui/vue';
// import Http from '../Services/Http';
// import GlobalSearch from './GlobalSearch/GlobalSearch';
// import avatarM from '../Assets/UserImage/avatarm.png';
// import avatarF from '../Assets/UserImage/avatarf.jpeg';

export default {
    // components: { IoMdBasket, BiChevronDown, GlobalSearch },
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
                const response = await createResource({
                    url: "hrms.api.mark_all_notifications_as_read",
                    onSuccess() {
                        notifications.reload()
                    },
                })
                count.value = response?.data?.data || 0;
            } catch (error) {
                console.error(error.response?.data?.message);
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
            firstName,
            // avatarM,
            // avatarF,
        };
    },
};
</script>

<style scoped>
/* Add your styles here */
</style>