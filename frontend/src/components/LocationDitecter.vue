<template>
    <div v-if="!pinCodes.includes(store.location_ditecter) || store.openpop"
        class="w-full h-screen md:px-10 pt-16 bg-black bg-opacity-40 top-0 fixed z-50">
        <div class="bg-white h-3/5 fixed bottom-0 md:static md:h-auto rounded-t-lg md:rounded-lg shadow-lg p-4 md:p-6 max-w-xl w-full md:text-center md:animate-vibrate">
            <FeatherIcon v-if="pinCodes.includes(store.location_ditecter)" name="x" class="w-6 h-6 md:w-5 md:h-5 text-gray-500 cursor-pointer absolute top-4 md:top-[70px] md:left-12 right-4"
                @click="store.openpop = false" />
            <h2 class="text-xl font-semibold text-main text-center">Welcome to <span class="text-primary">HRS</span></h2>
            <p class="mt-4 text-sm hidden md:block text-secondary">
                Please provide your delivery location to see products at a nearby store
            </p>
            <p class="mt-4 text-xl font-bold block md:hidden text-secondary">
                Select your Location            
            </p>
            <div class="mt-6 flex flex-col md:flex-row md:items-center justify-center gap-4">
                <Button @click="detectLocation" class="order-3 md:order-1"label="Detect my location" :variant="'outline'" theme="blue" size="md"
                    :loading="false" :loadingText="'Getting..'" :disabled="false" :link="null">
                    Detect my location
                </Button>
                <span class="text-gray-400 text-sm text-center order-2 md:order-2">OR</span>
                <select v-model="selectedPinCode" @change="setPinCode"
                    class="border order-1 md:order-3  border-gray-300 rounded-md py-1 px-7 focus:ring-2 focus:ring-blue-500 focus:outline-none">
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

watch(() => store.location_ditecter, (newValue) => {
    store.location_ditecter = localStorage.getItem('location_ditecter');
});


</script>
<style scoped>
</style>