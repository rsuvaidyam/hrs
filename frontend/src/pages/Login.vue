<template>
  <div class="flex flex-col justify-around h-full">
    <Button :variant="'outline'" theme="gray" size="md" @click="signinpop = true" type="button">
      Login
    </Button>

    <Dialog v-model="signinpop">
      <template #body-title>
        <h3>Login to Hearthstone Bakery</h3>
      </template>
      <template #body-content>
        <div class="flex flex-col gap-2">
          <TextInput v-model="email" label="email" placeholder="example@mail.com" />
          <TextInput v-model="password" label="Password" placeholder="******" type="password" />
        </div>
      </template>
      <template #actions>
        <Button class="w-full" variant="outline" theme='gray' :loading="loading" size='md' :disabled="false"
          @click="login()">
          Login
        </Button>
      </template>
    </Dialog>

  </div>
</template>

<script setup>
import { ref, inject, onMounted } from 'vue';
import { TextInput, Button, Dialog } from 'frappe-ui';
import { useRouter } from 'vue-router';
import { useRoute } from 'vue-router';
const email = ref('samar@gmail.com');
const password = ref('Rahul@123');
const auth = inject('$auth');
const loading = ref(false);
const signinpop = ref(false);
const router = useRouter()
const route = useRoute()
const redirectRoute = ref(null);

onMounted(() => {
  if (route?.query?.route) {
    redirectRoute.value = route.query.route;
    router.replace({ query: null });
  }
});

const login = async () => {
  loading.value = true;
  if (email.value && password.value) {
    let res = await auth.login(email.value, password.value);
    if (res) {
      signinpop.value = false;
      loading.value = false;
      router.push(redirectRoute.value || { name: "Home" });
    }
  }
}

</script>
