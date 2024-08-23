<template>

  <div class="flex flex-col justify-around h-full">
    <Button :variant="'outline'" theme="gray" size="md" @click="singinpop = true">
      Login
    </Button>
    <Dialog v-model="singinpop">
      {{ OTPScreen }}
      <template #body-title>
        <h3>Login to Sweetkart</h3>
      </template>
      <template #body-content>
        <div class="flex flex-col gap-2" v-if="OTPScreen">
          <TextInput v-model="formValues.otp" label="otp" placeholder="otp" />
        </div>
        <div class="flex flex-col gap-2" v-else>
          <TextInput v-model="formValues.username" label="Username" placeholder="example@mail.com" />
        </div>
      </template>
      <template #actions>
        <Button class="w-full" variant="solid" @click="handleConfirm">
          Login
        </Button>
      </template>
    </Dialog>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { TextInput, Button, Dialog } from 'frappe-ui';
const formValues = ref({
  username: '',
  otp: '',
});
const singinpop = ref(false);
const OTPScreen = ref(false);
const handleConfirm = () => {
  OTPScreen.value = true
};
</script>

<style scoped>

</style>