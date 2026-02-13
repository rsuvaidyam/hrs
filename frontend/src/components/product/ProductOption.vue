<template>
    <div class="relative">
        <div v-if="hasMultipleOptions" @click="dialog1 = true"
            class="w-full border rounded-sm h-7 flex justify-between items-center px-2">
            <p class="text-xs font-light">{{ product?.items[0]?.qty }} {{ product?.items[0]?.unit }}</p>
            <FeatherIcon name="chevron-right" class="text-gray-500 w-4" />
        </div>
        <div class="text-xs font-light h-7 flex items-center" v-else-if="optionLabel">{{ optionLabel }}</div>
        <Dialog v-model="dialog1">
            <template #body-title>
                <h3>{{ product?.items?.[0]?.name1 }}</h3>
            </template>
            <template #body-content>
                <div class="flex flex-col justify-center gap-3">
                    <div class="w-full h-[70px] border shadow-sm rounded-sm flex justify-between items-center"
                        v-for="el in product?.items" :key="el?.name">
                        <img :src="productImage" class="h-full rounded-sm object-cover" alt="">
                        <p class="text-sm font-light">{{ el?.qty }} {{ el?.unit }}</p>
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
import { ref, computed } from 'vue';
import { Dialog } from 'frappe-ui';
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
    },
    setup(props) {
        const dialog1 = ref(false);
        const hasMultipleOptions = computed(() => Array.isArray(props.product?.items) && props.product.items.length > 1);
        const optionLabel = computed(() => {
            const first = props.product?.items?.[0];
            if (!first) return '';
            if (first.qty != null && first.unit) return `${first.qty} ${first.unit}`;
            return '1 pc';
        });
        const productImage = computed(() => {
            const p = props.product;
            const img = p?.images?.[0];
            return (img && (img.image || img.url)) || p?.image || '';
        });
        return {
            dialog1,
            hasMultipleOptions,
            optionLabel,
            productImage,
        };
    },
};
</script>
