<template>
    <div class="w-full ">
        <div class="h-14 bg-gray-100 shadow-sm flex w-full">
            <div class="flex items-center gap-2 justify-between w-full px-3">
                <router-link to="/" class="flex items-center gap-1 ">
                    <FeatherIcon name="arrow-left" class="w-5" />
                    <span>My Order</span>
                </router-link>
                <router-link to="/cart" class=" text-black relative">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                        stroke="currentColor" class="size-6">
                        <path stroke-linecap="round" stroke-linejoin="round"
                            d="M15.75 10.5V6a3.75 3.75 0 1 0-7.5 0v4.5m11.356-1.993 1.263 12c.07.665-.45 1.243-1.119 1.243H4.25a1.125 1.125 0 0 1-1.12-1.243l1.264-12A1.125 1.125 0 0 1 5.513 7.5h12.974c.576 0 1.059.435 1.119 1.007ZM8.625 10.5a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm7.5 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Z" />
                    </svg>
                    <span v-if="count >= 1"
                            class="w-4 h-4 rounded-full bg-white border border-gray-900 absolute -top-1 -right-2 flex items-center justify-center bg-primary text-xs font-bold text-gray-700">{{
                            count }}</span>
                </router-link>
            </div>
        </div>
        <div class="w-full px-2 pt-2 flex flex-col gap-2">
            <div v-for="item in order_list" :key="item.name" class="w-full h-20 rounded-md bg-gray-50">
                {{ item.item }}
            </div>
        </div>
        <div class="block md:hidden">
            <Nav />
        </div>
    </div>
</template>

<script setup>
import Nav from '../components/BottomNav/Nav.vue';
import { ref ,inject,onMounted} from 'vue';

const store = inject('store');
const call = inject('$call')
const session = inject('$session');
const order_list = ref([]);
const count = ref(store.cart_count);

const get_order=async()=>{
    const res = await call('hrs.controllers.api.get_order', { user: session.user })
    if(res){
        order_list.value = res
    }
}
onMounted(()=>{
    get_order()
})
</script>