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
                    <div class="flex gap-2 mb-3">
                        <input
                            v-model="couponCode"
                            type="text"
                            placeholder="Coupon code"
                            class="flex-1 px-3 py-2 border rounded-button text-sm"
                        />
                        <button
                            type="button"
                            @click="applyCoupon"
                            :disabled="couponApplying"
                            class="px-4 py-2 rounded-button bg-chocolate text-white text-sm font-medium disabled:opacity-60"
                        >
                            {{ couponApplying ? 'Applying...' : 'Apply' }}
                        </button>
                    </div>
                    <p v-if="couponMessage" class="text-sm mb-2" :class="couponValid ? 'text-green-600' : 'text-red-600'">{{ couponMessage }}</p>
                    <div v-if="couponDiscount > 0" class="w-full p-3 mb-3 bg-green-100 rounded-md flex justify-between items-center">
                        <p>Discount (coupon)</p>
                        <p class="font-bold">- ₹ {{ couponDiscount }}</p>
                    </div>
                    <div class="w-full p-3 mb-3 bg-primary/10 rounded-md flex justify-between items-center">
                        <p>Amount to pay</p>
                        <p class="text-2xl font-bold">₹ {{ Math.ceil(Math.max(0, totalPrice - couponDiscount)) }}</p>
                    </div>
                </div>
                <!-- UPI -->
                <Upi />
                <!-- Card -->
                <CardPay />
                <!-- Cash on Delivery (amount to pay after coupon) -->
                <Cash :totalPrice="Math.max(0, totalPrice - couponDiscount)" :placeOrder="placeOrder" />
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
const couponCode = ref('');
const couponDiscount = ref(0);
const couponMessage = ref('');
const couponValid = ref(false);
const couponApplying = ref(false);
const cartCategory = ref('');
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
    try {
        const response = await call('hrs.controllers.api.get_cart', { usr: session.user });
        if (response && response.length) {
            let total = 0;
            response.forEach((item) => {
                total += (item.product?.final_price ?? item.product?.price ?? 0) * (item.count ?? 0);
            });
            totalPrice.value = total;
            cartCategory.value = response[0]?.product?.category || '';
            products.value = response.map((item) => ({
                item: item.product?.name,
                product: item.product?.parent,
                count: item.count,
                user: session.user,
                address: address.value?.default_address?.name,
                p_mode: 'Cash',
            }));
        }
    } finally {
        loader.value = false;
    }
}
async function applyCoupon() {
    if (!couponCode.value.trim()) {
        couponMessage.value = 'Enter a coupon code';
        couponValid.value = false;
        return;
    }
    couponApplying.value = true;
    couponMessage.value = '';
    try {
        const raw = await call('hrs.controllers.api.validate_coupon', {
            code: couponCode.value.trim(),
            total: totalPrice.value,
            category: cartCategory.value || undefined,
        });
        // call() returns data.message from API; payload is { valid, discount, message }. Don't use raw.message when it's the string (e.g. "Applied").
        const res = (raw && typeof raw === 'object' && 'valid' in raw) ? raw : (raw?.message && typeof raw.message === 'object' && 'valid' in raw.message) ? raw.message : raw;
        couponValid.value = !!res?.valid;
        couponMessage.value = res?.message || (res?.valid ? 'Applied' : 'Invalid coupon');
        couponDiscount.value = res?.valid ? (Number(res.discount) || 0) : 0;
    } catch (e) {
        couponValid.value = false;
        couponMessage.value = 'Could not validate coupon';
        couponDiscount.value = 0;
    } finally {
        couponApplying.value = false;
    }
}

let placeOrder = async () => {
    if (!address.value?.default_address?.name) {
        router.push({ name: 'Address' });
        return;
    }
    loader.value = true;
    try {
        await call('hrs.controllers.api.place_order', {
            data: products.value,
            coupon_code: (couponValid.value && couponCode.value) ? String(couponCode.value).trim() : '',
            coupon_discount: (couponValid.value && couponDiscount.value > 0) ? Number(couponDiscount.value) : 0,
        });
        order_success.value = true;
        setTimeout(() => router.push('/'), 4000);
    } catch (e) {
        console.error(e);
    } finally {
        loader.value = false;
    }
}
onMounted(async () => {
    await address_list();
    await OrderProduct();
    if (!products.value.length) {
        router.push('/cart');
    }
});
</script>