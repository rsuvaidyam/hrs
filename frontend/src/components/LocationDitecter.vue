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

const store = inject('store');
const selectedPinCode = ref('');
const pinCodes = ['821115', '823003', '400001', '560001'];

function detectLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(successCallback, errorCallback);
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}

function successCallback(position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;
    console.log('latitude',latitude,'longitude',longitude)
    // Use reverse geocoding API to get pin code from latitude and longitude
    getPinCodeFromCoordinates(latitude, longitude);
}

function errorCallback(error) {
    console.error('error',error);
    alert(`Error detecting location: ${error.message}`);
}

async function getPinCodeFromCoordinates(latitude, longitude) {
    try {
        const response = await fetch(
            `https://api.opencagedata.com/geocode/v1/json?q=${latitude}+${longitude}&key=b3dfb1982c2345f2acabc73933dc6a56`
        );
        const data = await response.json();
        if (data.status.code === 200) {
            const addressComponents = data.results[0].components;
            localStorage.setItem('address', data.results[0].formatted ?? selectedPinCode.value);
            const postalCode = addressComponents.postcode;

            if (postalCode) {
                const detectedPinCode = postalCode;
                console.log("%cpostalCode %c" + postalCode, "color: blue; font-size: 14px;", "color: green; font-size: 20px;");
                localStorage.setItem('location_ditecter', detectedPinCode);
                store.location_ditecter = detectedPinCode;
                store.openpop = false;
            } else {
                alert("Could not detect the pin code for your location.");
            }
        } else {
            console.error('error',data.status.message)
            alert(`Geocoding error: ${data.status.message}`);
        }
    } catch (error) {
        alert(`Error fetching pin code: ${error.message}`);
    }
}


function setPinCode() {
    if (selectedPinCode.value) {
        localStorage.setItem('location_ditecter', selectedPinCode.value);
        store.location_ditecter = selectedPinCode.value;
        store.openpop = false;
    }
}

watch(() => store.location_ditecter, (newValue) => {
    store.location_ditecter = localStorage.getItem('location_ditecter');
});
</script>

<style scoped>
</style>