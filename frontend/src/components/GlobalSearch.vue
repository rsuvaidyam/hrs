<template>
    <div class="w-3/5 md:w-3/6 relative">
        <Button :variant="'outline'" theme="gray" size="md" label="Search.." class="text-start w-96"
            @click="dialog1 = true" />
        <Dialog :options="{
            title: 'Confirm',
            message: 'Are you sure you want to confirm this action?',
            size: 'xl',
            actions: [{ label: 'Confirm', variant: 'solid', onClick: handleConfirm }],
        }" v-model="dialog1" />
    </div>
</template>

<script>
import { ref, watch } from 'vue';
import { Dialog, Button } from 'frappe-ui';

export default {
    components: {
        Dialog,
        Button,
    },
    setup() {
        const searchValue = ref('');
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

        watch(searchValue, handleSearch);

        return {
            searchValue,
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