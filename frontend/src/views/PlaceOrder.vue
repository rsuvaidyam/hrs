<template>
    <div class="w-full h-screen">
        <Order_success v-if="order_success" />
        <div v-else class="w-full h-full">
            <div class="h-12 flex w-full">
                <div class="flex items-center gap-2 justify-between w-full px-2">
                    <router-link to="/cart" class="flex items-center gap-1 ">
                        <FeatherIcon name="arrow-left" class="w-5" />
                        <span>Payments</span>
                    </router-link>
                    <div class="bg-gray-300 rounded-sm text-sm p-1 animate-pulse">100 % secure</div>
                </div>
            </div>
            <div v-if="loader" class="w-full h-full flex justify-center items-center">
                <Spinner class="w-16" />
            </div>
            <div class="w-full md:w-1/2" v-else>
                <div class="w-full px-2">
                    <div class="w-full p-3 mb-3 bg-blue-200 rounded-md flex justify-between items-center">
                        <p>Total Amount</p>
                        <p class="text-2xl font-bold">₹ {{ Math.ceil(totalPrice) }}</p>
                    </div>
                </div>
                <!-- UPI -->
                <Upi />
                <!-- Card -->
                <CardPay />
                <!-- Cash on Delivery -->
                <Cash :totalPrice="totalPrice" :placeOrder="placeOrder" />
                <div class="absolute bottom-2 w-full">
                    <SelectAddress :address="address" />
                </div>
            </div>
            <div class="w-full md:w-1/2"></div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, inject } from 'vue';
import SelectAddress from '../components/SelectAddress.vue';
import FeatherIcon from 'frappe-ui/src/components/FeatherIcon.vue';
import Upi from '../components/Payments/Upi.vue';
import CardPay from '../components/Payments/CardPay.vue';
import Cash from '../components/Payments/Cash.vue';
import Order_success from '../components/Payments/Order_success.vue';
import { Spinner } from 'frappe-ui';
import { useRouter } from 'vue-router';

const router = useRouter();
const address = ref({});
const products = ref([]);
let totalPrice = ref(0);
let order_success = ref(false);
let loader = ref(false);
const call = inject('$call');
const session = inject('$session');

const address_list = async () => {
    const response = await call('hrs.controllers.api.get_address', { user: session.user });
    if (response) {
        address.value = response;
    }
}
const OrderProduct = async () => {
    loader.value = true;
    const response = await call('hrs.controllers.api.get_cart', { usr: session.user });
    response?.map((item) => {
        totalPrice.value += item.product.final_price * item.product.count;
        setTimeout(() => {
            loader.value = false;
        }, 500);
    });
    products.value = response.map((item) => {
        return {
            item: item.product.name,
            product: item.product.parent,
            count: item.product.count,
            user: session.user,
            address: address.value.default_address.name,
            p_mode: 'Cash',
        }
    });
}
let placeOrder = () => {
    loader.value = true
    let response = call('hrs.controllers.api.place_order', { data: products.value });
    if (response) {
        setTimeout(() => {
            loader.value = false
            order_success.value = true;
        }, 2000);
        setTimeout(() => {
            router.push('/');
        }, 4000);
    }
}
onMounted(() => {
    address_list();
    OrderProduct();
});
</script>