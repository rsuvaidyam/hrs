<template>
    <div v-if="!pinCodes.includes(store.location_ditecter) || store.openpop"
        class="w-full h-screen md:px-10 py-5 bg-black bg-opacity-40 fixed z-50">
        <div class="bg-white rounded-lg shadow-lg p-6 max-w-xl w-full text-center animate-vibrate">
            <h2 class="text-xl font-semibold text-main">Welcome to <span class="text-primary">HRS</span></h2>
            <p class="mt-4 text-sm text-secondary">
                Please provide your delivery location to see products at a nearby store
            </p>
            <div class="mt-6 flex items-center justify-center gap-4">
                <Button @click="detectLocation" label="Detect my location" :variant="'outline'" theme="blue" size="md"
                    :loading="false" :loadingText="'Getting..'" :disabled="false" :link="null">
                    Detect my location
                </Button>
                <span class="text-gray-400 text-sm">OR</span>
                <select v-model="selectedPinCode" @change="setPinCode"
                    class="border border-gray-300 rounded-lg py-1 px-7 focus:ring-2 focus:ring-blue-500 focus:outline-none">
                    <option disabled value="">Select your pin code</option>
                    <option v-for="pin in pinCodes" :key="pin" :value="pin">{{ pin }}</option>
                </select>
            </div>
            <div class="px-10 flex flex-col justify-center items-center text-center mt-10"
                v-if="!pinCodes.includes(store.location_ditecter) && store.location_ditecter">
                <img class="w-32 mb-4" src="../assets/not_found.webp" alt="Not Found">
                <p class="text-main mb-2">Oops!</p>
                <p class="text-sm text-main">HRS is not available at the moment. Please select a different location.</p>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, watch ,inject} from 'vue';
import { Button } from 'frappe-ui';
const store=inject('store')
const selectedPinCode = ref('');


const pinCodes = ['841311', '110001', '400001', '560001'];

function detectLocation() {
   localStorage.setItem('location_ditecter', '841711');
   store.location_ditecter = 841711
   store.openpop =  false
}

function setPinCode() {
    if (selectedPinCode.value) {
        localStorage.setItem('location_ditecter', selectedPinCode.value);
        store.location_ditecter =  selectedPinCode.value
        store.openpop =  false
    }
}selectedPinCode

watch(store.location_ditecter, (newValue) => {
    store.location_ditecter = localStorage.getItem('location_ditecter');
});

</script>
