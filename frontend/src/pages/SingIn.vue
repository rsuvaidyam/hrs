<template>
  <div class="flex flex-col justify-around h-full">
    <Button :variant="'outline'" theme="gray" size="md" @click="signinpop = true" type="button">
      Login
    </Button>
    <form @submit.prevent="login">
    <Dialog v-model="signinpop">
      <template #body-title>
        <h3>Login to Sweetkart</h3>
      </template>
      <template #body-content>
        <div class="flex flex-col gap-2">
          <TextInput v-model="email" label="email" placeholder="example@mail.com" />
          <TextInput v-model="password" label="Password" placeholder="******" type="password"/>
        </div>
      </template>
      <template #actions>
        <Button class="w-full" variant="solid" type="submit">
          Login
        </Button>
      </template>
    </Dialog>
  </form>
  </div>
</template>

<script >
import { ref } from 'vue';
import { TextInput, Button, Dialog } from 'frappe-ui';

export default {
  components: { 
      Button,
      TextInput,
      Dialog,
    },
  data() {
	return {
	  email: null,
	  password: null,
	};
  },
  setup(){
    const signinpop = ref(false);
    return {
      signinpop
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
	  if (this.email && this.password) {
		let res = await this.$auth.login(this.email, this.password);
		if (res) {
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
