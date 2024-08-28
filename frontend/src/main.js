import { createApp, reactive } from "vue";
import App from "./App.vue";

import router from './router';
import resourceManager from "./libs/resourceManager";
import call from "./libs/controllers/call";
import socket from "./libs/controllers/socket";
import Auth from "./libs/controllers/auth";
import { session } from "@/data/session";
import {FeatherIcon} from 'frappe-ui';
import { store } from './globalState';

const app = createApp(App);

// Provide the global state
app.provide('store', store);


// Plugins
app.use(router);
const auth = reactive(new Auth());
app.use(resourceManager);
app.component("FeatherIcon",FeatherIcon)

// Global Properties,
// components can inject this
app.provide("$session", session)
app.provide("$call", call);
app.provide("$auth", auth);
app.provide("$socket", socket);


// Configure route gaurds
router.beforeEach(async (to, from, next) => {
	// if (to.matched.some((record) => !record.meta.isLoginPage)) {
	// 	if (!auth.isLoggedIn) {
	// 		next({ name: 'Login', query: { route: to.path } });
	// 	} else {
	// 		next();
	// 	}
	// } else {
	// 	if (!auth.isLoggedIn) {
	// 		next({ name: 'Home' });
	// 	} else {
	// 	}
	// }
	next();
});

app.mount("#app");
