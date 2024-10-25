<template>
    <div class=" px-2 py-3 border-t-2 border-b-2 bg-gray-100">
        <div class="flex justify-between items-center " @click="toggleDetails">
            <p class="text-sm font-medium">Credit / Debit / ATM Card</p>
            <FeatherIcon name="chevron-down" class="w-5" />
        </div>
        <transition name="fade">
            <div v-if="isOpen" class="w-full pt-2 ">
                <div class="w-full p-3 bg-white rounded-md flex flex-col gap-3">
                    <FormControl type="card_nubmer" label="Card Number">
                        <template #suffix>
                            <FeatherIcon class="w-4" name="credit-card" />
                        </template>
                    </FormControl>
                    <div class="flex gap-2">
                        <FormControl type="vaild" label="Vaild Thru">
                        </FormControl>
                        <FormControl type="cvv" label="CVV">
                            <template #suffix>
                                <FeatherIcon class="w-4" name="help-circle" />
                            </template>
                        </FormControl>
                    </div>
                    <Button :ref_for="true" theme="gray" size="sm" label="Place Order" :loading="false"
                        :loadingText="null" :disabled="false" :link="null" class="w-full text-white bg-primary">
                        Pay ₹ 1199
                    </Button>
                </div>
            </div>
        </transition>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { Button, FormControl } from 'frappe-ui';
const isOpen = ref(false);

function toggleDetails() {
    isOpen.value = !isOpen.value;
}
</script>