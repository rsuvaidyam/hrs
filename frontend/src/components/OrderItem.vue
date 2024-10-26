<template>

    <div class="w-full h-screen">
        <div class="h-14 bg-gray-100 shadow-sm flex w-full">
            <div class="flex items-center gap-2 justify-between w-full px-3">
                <router-link to="/order" class="flex items-center gap-1 ">
                    <FeatherIcon name="arrow-left" class="w-5" />
                    <span>Order Details</span>
                </router-link>
                <router-link to="/order" class=" text-black relative">
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
        <div class="flex w-full h-screen bg-gray-200 justify-center items-center" v-if="loading">
            <Spinner class="w-16" />
        </div>
        <div class="w-full h-full" v-else>
            <div class=" border-b pb-3">
                <div class="px-2 flex items-center h-8 bg-gray-50">
                    <p>Order ID - {{ order_item.name }} </p>
                </div>
                <div class="flex justify-between px-2 pt-3">
                    <p class="text-xl">{{ order_item?.product?.name1 }}</p>
                    <img :src="order_item?.images?.image" alt="" class="w-16 rounded-sm shadow-sm">
                </div>
                <div class="flex gap-5 items-center pt-2">
                    <p class="px-2 text-xl font-semibold">₹ {{ Math.ceil(order_item?.product?.final_price) }}</p>
                    <p class="px-2 text-xl">{{ order_item?.product?.qty }} {{ order_item?.product?.unit }}</p>
                </div>
            </div>
            <!-- steper -->
            <div class="">
                <OrderTracking />
            </div>
            <div class="w-full px-4 h-10">
                <Button label="Cancel Order"></Button>
            </div>
            <!-- shipping -->
            <div class="w-full shadow-md my-2">
                <p class=" border-b text-xl p-2">Shipping Details</p>
                <p class="px-2 text-2xl font-medium pt-2">{{ order_item?.address?.name1 }}</p>
                <div class="flex  flex-col px-2 pb-2">
                    <p>{{ order_item?.address?.road_name }}, {{ order_item?.address?.house_name }}</p>
                    <p>District - {{ order_item?.address?.district }}</p>
                    <p>Pin Code - {{ order_item?.address?.pin_code }}</p>
                    <p>Phone Number - {{ order_item?.address?.phone_no }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, inject, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import OrderTracking from './OrderTracking.vue';
import { Button, Spinner } from 'frappe-ui';

const router = useRouter();
const store = inject('store');
const call = inject('$call')
const order_item = ref({});
const loading = ref(false);
const count = ref(store.cart_count);

const get_order = async () => {
    loading.value = true
    const res = await call('hrs.controllers.api.get_order_details', { item: router.currentRoute.value?.params?.name })
    if (res) {
        order_item.value = res
        setTimeout(() => {
            loading.value = false
        }, 500);
    }
}
onMounted(() => {
    get_order()
})
</script>