<template>
    <div class="relative">
        <label for="search" @click="dialog1 = true"> <p class="w-60 md:w-96 h-full rounded-md border-2 border-gray-400 cursor-pointer bg-white py-0.5 px-2 text-md">Search..</p> </label> 
        <Dialog v-model="dialog1">
            <template #body-title>
                <h3>Search All Products</h3>
            </template>
            <template #body-content>
                <div class="flex flex-col gap-2 relative">
                    <TextInput v-model="search" label="search" id="search" placeholder="Search.." />
                    <Spinner class="w-4 absolute top-1.5 right-1.5"/>
                </div>
                <div class="h-full min-h-72 md:h-48 md:min-h-48"></div>
            </template>
        </Dialog>
    </div>
</template>

<script>
import { ref, watch } from 'vue';
import { Dialog, Button, TextInput,Spinner } from 'frappe-ui';

export default {
    components: {
        Dialog,
        Button,
        TextInput,
        Spinner
    },
    setup() {
        const search = ref('');
        const searchResults = ref([]);
        const searchLoader = ref(false);
        const dialog1 = ref(false);

        const handleSearch = async () => {
            // if (searchValue.value) {
            //   searchLoader.value = true;
            //   try {
            //     const response = await fetch('hrms.api.mark_all_notifications_as_read', {
            //       method: 'POST',
            //     });
            //     const data = await response.json();
            //     searchResults.value = data?.data || [];
            //   } catch (error) {
            //     console.log(error.message);
            //   } finally {
            //     searchLoader.value = false;
            //   }
            // } else {
            //   searchResults.value = [];
            // }
        };

        const handleConfirm = () => {
            console.log('Confirmed!');
            dialog1.value = false; // Close the dialog after confirming
        };

        watch(search, handleSearch);

        return {
            search,
            searchResults,
            searchLoader,
            dialog1,
            handleSearch,
            handleConfirm,
        };
    },
};
</script>

<style scoped>
/* Add any additional styles here */
</style>