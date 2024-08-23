<template>

  <div class="flex flex-col justify-around h-full">
    <Button :variant="'outline'" theme="gray" size="md" label="SingIn"
      @click="singinpop = true" />
    <Dialog :options="{
      title: 'Confirm',
      message: 'Are you sure you want to confirm this action?',
      size: 'xl',
      actions: [{ label: 'Confirm', variant: 'solid', onClick: handleConfirm }],
    }" v-model="singinpop" />
  </div>
</template>

<script>
import { ref } from 'vue';
import { TextInput, Button, Dialog } from 'frappe-ui';

export default {
  components: {
    TextInput, Button, Dialog
  },
  setup() {

    const formValues = ref({
      username: '6201521438',
      password: 'Rahul@123',
    });
    const singinpop = ref(false);

    const handleConfirm = () => {
      console.log('Confirmed!');
      singinpop.value = false; // Close the dialog after confirming
    };

    return {
      singinpop,
      handleConfirm,
      formValues,
    };
  },
};
</script>

<style scoped>
/* Add your styles here */
</style>