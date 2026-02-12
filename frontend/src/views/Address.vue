<template>
    <div class="pt-14">
        <div class="flex gap-3 px-3">
            <div class="flex flex-col gap-3 w-full">
                <FormControl :type="'text'" size="sm" variant="subtle" placeholder="Placeholder" :disabled="false"
                    label="Full Name" v-model="inputValue.name1" />
                <FormControl :type="'text'" size="sm" variant="subtle" placeholder="Placeholder" :disabled="false"
                    label="Phone Number" v-model="inputValue.phone_no" />
                <FormControl :type="'text'" size="sm" variant="subtle" placeholder="Placeholder" :disabled="false"
                    label="House Name" v-model="inputValue.house_name" />
                <FormControl :type="'text'" size="sm" variant="subtle" placeholder="Placeholder" :disabled="false"
                    label="Road Name" v-model="inputValue.road_name" />
            </div>
            <div class="w-full flex flex-col gap-3">
                <FormControl :type="'text'" size="sm" variant="subtle" placeholder="Placeholder" :disabled="false"
                    label="Land Mark" v-model="inputValue.land_mark" />
                <FormControl :type="'text'" size="sm" variant="subtle" placeholder="Placeholder" :disabled="false"
                    label="Pin Code" v-model="inputValue.pin_code" />
                <FormControl :type="'text'" size="sm" variant="subtle" placeholder="Placeholder" :disabled="false"
                    label="District" v-model="inputValue.district" />
            </div>
        </div>
        <div class="flex px-3 mt-5">
            <Button :variant="'solid'" theme="gray" size="sm" label="Submit" :loading="false" :disabled="false"
                class="w-28 bg-primary" @click="handleSubmit">
                Submit
            </Button>
        </div>
    </div>
</template>

<script setup>
import { ref, inject } from 'vue';
import { FormControl, Button } from 'frappe-ui';
import { useRouter } from 'vue-router';

const router = useRouter();
const call = inject('$call');
const session = inject('$session');

const inputValue = ref({
    name1: '',
    phone_no: '',
    house_name: '',
    road_name: '',
    land_mark: '',
    pin_code: '',
    district: '',
});

// Function to handle form submission with validation
const handleSubmit = async () => {
    const requiredFields = ['name1', 'phone_no', 'house_name', 'pin_code', 'district'];
    const emptyFields = requiredFields.filter(field => !inputValue.value[field]);

    if (emptyFields.length > 0) {
        alert(`Please fill in all mandatory fields:\n ${emptyFields.join(', ')}`);
        return;
    } else {
        try {
            const formData = inputValue.value;
            let res = await call('hrs.controllers.api.add_address', { data: { ...formData, user: session.user, default: 1 } });
            if (res.name) {
                router.push({ name: 'PlaceOrder' })
            }
        } catch (error) {
            console.log(error);

        }
    }
};
</script>
