<template>
    <div class="px-2 py-3 border-b-2">
        <div class="flex justify-between items-center cursor-pointer" @click="toggleDetails">
            <p class="text-sm font-medium">Cash on Delivery</p>
            <FeatherIcon :name="isOpen ? 'chevron-up' : 'chevron-down'" class="w-5" />
        </div>
        <transition name="fade">
            <div v-if="isOpen" class="w-full pt-2">
                <div class="w-full p-3 rounded-md bg-gray-100 flex flex-col gap-3">
                    <p class="text-sm text-gray-900">Pay ₹ {{ Math.ceil(totalPrice) }} on delivery</p>
                    <Button :ref_for="true" theme="gray" size="sm" label="Place Order" :loading="false" :loadingText="null"
                        :disabled="false" @click="placeOrder" class="w-full text-white bg-primary">
                        Place Order
                    </Button>
                </div>
            </div>
        </transition>
    </div>
</template>

<script setup>
import { ref, watch,inject } from 'vue';
import { Button } from 'frappe-ui';

const isOpen = ref(false);
const call = inject('$call');
const props = defineProps(['totalPrice','placeOrder']);
const totalPrice = ref(props.totalPrice);
const placeOrder = ref(props.placeOrder);

watch(() => props.totalPrice, (newTotalPrice, oldTotalPrice) => {
    totalPrice.value = newTotalPrice;
});
watch(() => props.placeOrder, (newProducts, oldProducts) => {
    placeOrder.value = newProducts;
});
function toggleDetails() {
    isOpen.value = !isOpen.value;
}
</script>

