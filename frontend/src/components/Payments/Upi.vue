<template>
    <div class="px-2 py-3 border-b-2">
        <div class="flex justify-between items-center">
            <p class="text-sm font-medium">UPI</p>
            <FeatherIcon name="chevron-down" class="w-5" />
        </div>
        <div class="w-full pt-2 ">
            <div class="w-full p-3 rounded-md bg-gray-100 flex flex-col gap-3">
                <div class="flex justify-between bg-white p-2 rounded-md">
                    <div class="flex items-center gap-2">
                        <input type="radio" name="upi" id="">
                        <p>Paytm</p>
                    </div>
                    <img src="https://cdn-icons-png.flaticon.com/512/2111/2111646.png" class="w-6 h-6" />
                </div>
                <div class="flex justify-between bg-white p-2 rounded-md">
                    <div class="flex items-center gap-2">
                        <input type="radio" name="upi" id="">
                        <p>PhonePe</p>
                    </div>
                    <img src="https://cdn-icons-png.flaticon.com/512/2111/2111646.png" class="w-6 h-6" />
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { Button, FormControl } from 'frappe-ui';
</script>