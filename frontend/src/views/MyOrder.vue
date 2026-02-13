<template>

    <div class="w-full h-screen">

        <div class="h-14 bg-gray-200 shadow-sm flex w-full">
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
        <div class="flex w-full h-full bg-gray-100 justify-center items-center" v-if="loading">
            <Spinner class="w-16" />
        </div>
        <div class="w-full h-full" v-else>
            <div class="w-full pt-2 flex flex-col gap-2">
                <router-link :to="`/order/${item.name}`" v-for="item in order_list" :key="item.name"
                    class="w-full flex items-center justify-between gap-3 pb-3 px-2 min-h-24 border-b">
                    <div class="flex gap-3 items-center flex-1 min-w-0">
                        <img :src="item.images?.image" alt="" class="h-20 w-20 object-cover rounded">
                        <div class="flex flex-col gap-1 min-w-0">
                            <p class="text-lg font-medium">{{ item.creation?.split(' ')[0] }}</p>
                            <p class="text-chocolate-soft truncate">{{ item.product?.name1 }}</p>
                            <div class="flex flex-wrap items-center gap-2 text-sm">
                                <span v-if="item.total_amount != null" class="text-chocolate-soft">₹ {{ Math.ceil(item.total_amount) }}</span>
                                <span v-if="item.discount_amount > 0" class="text-green-600">− ₹ {{ Math.ceil(item.discount_amount) }} coupon</span>
                                <span v-if="item.amount_payable != null" class="font-semibold text-primary">Pay ₹ {{ Math.ceil(item.amount_payable) }}</span>
                            </div>
                        </div>
                    </div>
                    <FeatherIcon name="chevron-right" class="w-5 shrink-0" />
                </router-link>
            </div>
            <div class="block md:hidden">
                <Nav />
            </div>
        </div>
    </div>
</template>

<script setup>
import Nav from '../components/BottomNav/Nav.vue';
import { ref, inject, onMounted } from 'vue';
import { Spinner } from 'frappe-ui';
const store = inject('store');
const call = inject('$call')
const session = inject('$session');
const order_list = ref([]);
const loading = ref(false);
const count = ref(store.cart_count);

const get_order = async () => {
    loading.value = true
    const res = await call('hrs.controllers.api.get_order', { user: session.user })
    if (res) {
        order_list.value = res
        setTimeout(() => {
            loading.value = false
        }, 500)
    }
}
onMounted(() => {
    get_order()
})
</script>