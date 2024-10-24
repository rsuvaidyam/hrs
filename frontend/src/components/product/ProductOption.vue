<template>
    <div class="relative">
        <div v-if="product?.items.length > 1" @click="dialog1 = true"
            class="w-full border rounded-sm h-7 flex justify-between items-center px-2">
            <p class="text-xs font-light">{{ product?.items[0]?.qty }} {{ product?.items[0]?.unit }}</p>
            <FeatherIcon name="chevron-right" class="text-gray-500 w-4" />
        </div>
        <div class="text-xs font-light h-7 flex items-center" v-else>{{ product?.items[0]?.qty }} {{
            product?.items[0]?.unit }}
        </div>
        <Dialog v-model="dialog1">
            <template #body-title>
                <h3>Products Option</h3>
            </template>
            <template #body-content>
                <div class="flex flex-col justify-center gap-4">
                    <div class="w-full h-16 border rounded-sm flex justify-between items-center"
                        v-for="el in product?.items">
                        <img :src="product.images[0].image" class="h-full rounded-sm" alt="">
                        <p class="text-sm font-light">{{ el?.qty }} {{el?.unit }}</p>
                        <div class=" text-sm flex gap-2">
                            <p class="font-bold">₹ {{ Math.ceil(el.final_price) }}</p>
                            <del class="text-gray-600">₹ {{ el.price }}</del>
                        </div>
                        <div class="w-20 h-full flex items-center pr-2">
                            <AddToCartBtn :product="el" :products="product.items" :option="el.name" />
                        </div>
                    </div>
                </div>
            </template>
        </Dialog>
    </div>
</template>

<script>
import { ref } from 'vue';
import { Dialog, Button, TextInput, Spinner } from 'frappe-ui';
import AddToCartBtn from '../AddToCartBtn.vue';

export default {
    props: {
        product: {
            type: Object,
            required: true,
        }
    },
    components: {
        Dialog,
        AddToCartBtn,
        Button,
        TextInput,
        Spinner
    },
    setup() {
        const dialog1 = ref(false);
        return {
            dialog1,
        };
    },
};
</script>
