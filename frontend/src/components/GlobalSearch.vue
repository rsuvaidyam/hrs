<template>
    <div class="relative">
        <label for="search" @click="dialog1 = true">
            <p class="w-full h-full rounded-md border-2 border-gray-400 cursor-pointer bg-white py-0.5 px-2 text-md">
                Search..</p>
        </label>
        <Dialog v-model="dialog1">
            <template #body-title>
                <h3>Search All Products</h3>
            </template>
            <template #body-content>
                <div class="flex flex-col gap-2 relative">
                    <TextInput v-model="search" @onchnage="handleSearch()" label="search" id="search"
                        placeholder="Search.." />
                    <Spinner class="w-4 absolute top-1.5 right-1.5" />
                </div>
                <div class="h-full min-h-72 md:h-48 md:min-h-48">
                    <div class="flex flex-col">
                        <div class="p-3 h-14 border-b flex justify-between" v-for="item in searchResults" :key="item.name">
                            <div class="flex gap-2 items-center">
                                <img :src="item.images[0].image" alt="" class="h-full rounded-sm w-10">
                                <p class="truncate text-xl">{{ item.items[0].name1 }}</p>
                            </div>
                            <FeatherIcon name="chevron-right" class="w-6" />
                        </div>
                    </div>
                </div>
            </template>
        </Dialog>
    </div>
</template>

<script setup>
import { ref, watch, inject } from 'vue';
import { Dialog, Button, TextInput, Spinner } from 'frappe-ui';

const search = ref('');
const searchResults = ref([]);
const searchLoader = ref(false);
const dialog1 = ref(false);
const call = inject('$call');
const handleSearch = async () => {
    
};
watch(() => search.value, async(newProducts) => {
    let res = await call('hrs.controllers.api.product_search', { key_word: newProducts })
    searchResults.value = res;
})

watch(search, handleSearch);

</script>
