<template>
    <div class="relative w-full">
        <div v-if="address.default_address"
            class="w-full border-b-2 bg-white rounded-sm h-9 flex justify-between items-center px-2">
            <p class="text-xs font-light">Deliver to : {{ address.default_address.name1 }} - {{
                address.default_address.house_name }} , {{
                    address.default_address.road_name }} , {{ address.default_address.district }} - {{
                    address.default_address.pin_code }}</p>
            <div class="flex cursor-pointer" @click="dialog1 = true">
                <p class="text-xs font-semibold text-gray-900">Change</p>
                <FeatherIcon name="chevron-right" class="text-gray-900 w-4" />
            </div>
        </div>
        <Dialog v-model="dialog1">
            <template #body-title>
                <h3>Select Address</h3>
            </template>
            <template #body-content>
                <div class="flex flex-col justify-center gap-3">
                    <div class="w-full px-2 py-1 border relative shadow-sm rounded-sm flex flex-col"
                        v-for="el in address.address_list">
                        <p>Deliver to : {{ el.name1 }} - {{ el.house_name }} , {{ el.district }} - {{ el.pin_code }}</p>
                        <p>{{ el.road_name }} {{ el.land_mark }}</p>
                        <Checkbox size="sm" :value="el.default" v-model="el.default"
                            :checked="selectedAddressId === el.name" class="absolute right-1 top-1"
                            @change="setDefaultAddress(el)" />
                    </div>
                </div>
            </template>
            <template #footer>
                <Button label="Confirm" @click="confirmAddressChange" />
            </template>
        </Dialog>
    </div>
</template>

<script setup>
import { ref, inject, watch } from 'vue';
import { Dialog, Button, TextInput, Spinner, Checkbox } from 'frappe-ui';
const call = inject('$call');
const dialog1 = ref(false);

const props = defineProps(['address']);
let address = ref(props.address);

watch(() => props.address, (newVal) => {
    address.value = newVal;
});


// const change_address = async (address) => {
//     const response = await call('hrs.controllers.api.change_address', { user: session.user, address: address });
//     console.log(response)
// };
</script>
