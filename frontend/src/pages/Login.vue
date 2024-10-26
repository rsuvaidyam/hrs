<template>
  <div class="flex flex-col justify-around h-full">
    <Button :variant="'outline'" theme="gray" size="md" @click="signinpop = true" type="button">
      Login
    </Button>

    <Dialog v-model="signinpop">
      <template #body-title>
        <h3>Login to Sweetkart</h3>
      </template>
      <template #body-content>
        <div class="flex flex-col gap-2">
          <TextInput v-model="email" label="email" placeholder="example@mail.com" />
          <TextInput v-model="password" label="Password" placeholder="******" type="password" />
        </div>
      </template>
      <template #actions>
        <Button class="w-full" variant="outline" theme='gray' :loading="loading" size='md' :disabled="false" @click="login()">
          Login
        </Button>
      </template>
    </Dialog>

  </div>
</template>

<script>
import { ref, watch } from 'vue';
import { TextInput, Button, Dialog } from 'frappe-ui';

export default {
  components: {
    Button,
    TextInput,
    Dialog,
  },
  data() {
    return {
      email: 'samar@gmail.com',
      password: 'Rahul@123',
    };
  },
  setup() {
    const signinpop = ref(false);
    const loading = ref(false);
    return {
      signinpop,
      loading
    };
  },
  inject: ["$auth"],
  async mounted() {
    if (this.$route?.query?.route) {
      this.redirect_route = this.$route.query.route;
      this.$router.replace({ query: null });
    }
  },
  methods: {
    async login() {
      this.loading = true;
      if (this.email && this.password) {
        let res = await this.$auth.login(this.email, this.password);
        if (res) {
          this.signinpop = false;
          this.loading = false;
          this.$router.push({ name: "Home" });
        }
      }
    },
  },
};
</script>

<style scoped>
/* Add any scoped styles here */
</style>
