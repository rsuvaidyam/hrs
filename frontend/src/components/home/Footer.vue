<template>
	<footer class="bg-bakery-footer text-footer-text">
		<div class="max-w-[1800px] mx-auto px-4 md:px-8 py-16 md:py-20">
			<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 md:gap-16">
				<!-- Brand -->
				<div class="lg:col-span-1">
					<h2 class="font-serif text-2xl md:text-3xl font-semibold text-white">{{ props.siteName || siteName || 'Store' }}</h2>
					<p v-if="props.tagline || props.siteName" class="mt-4 text-footer-muted text-sm md:text-base max-w-xs">
						{{ props.tagline || '' }}
					</p>
				</div>

				<!-- Quick links -->
				<div>
					<h3 class="font-sans text-sm uppercase tracking-widest text-white/80 mb-4">Quick Links</h3>
					<ul class="space-y-2">
						<li><router-link to="/" class="text-footer-muted hover:text-white transition-colors">Home</router-link></li>
						<li><router-link to="/#featured" class="text-footer-muted hover:text-white transition-colors">Menu</router-link></li>
						<li><router-link to="/#categories" class="text-footer-muted hover:text-white transition-colors">Categories</router-link></li>
						<li><router-link to="/cart" class="text-footer-muted hover:text-white transition-colors">Cart</router-link></li>
						<li><router-link to="/order" class="text-footer-muted hover:text-white transition-colors">My Orders</router-link></li>
					</ul>
				</div>

				<!-- Store hours & contact -->
				<div>
					<h3 class="font-sans text-sm uppercase tracking-widest text-white/80 mb-4">Store Hours</h3>
					<p class="text-footer-muted text-sm whitespace-pre-line">{{ props.storeHours || storeHours }}</p>
					<p class="mt-4 text-footer-muted text-sm">{{ props.address || address }}</p>
				</div>

				<!-- Newsletter -->
				<div>
					<h3 class="font-sans text-sm uppercase tracking-widest text-white/80 mb-4">Newsletter</h3>
					<p class="text-footer-muted text-sm mb-4">Get updates on new bakes and offers.</p>
					<form @submit.prevent="subscribe" class="flex flex-col sm:flex-row gap-2">
						<input
							v-model="email"
							type="email"
							placeholder="Your email"
							class="flex-1 min-w-0 px-4 py-3 rounded-button bg-white/10 border border-white/20 text-white placeholder-white/50 focus:outline-none focus:ring-2 focus:ring-bakery-primary focus:border-transparent"
							required
						/>
						<button
							type="submit"
							class="px-6 py-3 rounded-button bg-bakery-primary text-white font-medium hover:bg-bakery-primary-hover transition-colors focus:outline-none focus-visible:ring-2 focus-visible:ring-bakery-primary"
						>
							Subscribe
						</button>
					</form>
					<p v-if="newsletterMessage" class="mt-2 text-sm" :class="newsletterSuccess ? 'text-green-400' : 'text-amber-400'">
						{{ newsletterMessage }}
					</p>
					<!-- Social -->
					<div class="mt-6 flex gap-4">
						<a
							v-for="s in socialLinks"
							:key="s.name"
							:href="s.url"
							target="_blank"
							rel="noopener noreferrer"
							class="text-footer-muted hover:text-white transition-colors"
							:aria-label="s.name"
						>
							<FeatherIcon :name="s.icon" class="w-5 h-5" />
						</a>
					</div>
				</div>
			</div>

			<div class="mt-16 pt-8 border-t border-white/10 text-center text-footer-muted text-sm">
				<p>&copy; {{ new Date().getFullYear() }} {{ props.siteName || siteName || 'Store' }}. All rights reserved.</p>
			</div>
		</div>
	</footer>
</template>

<script setup>
import { ref, inject } from 'vue';
import { FeatherIcon } from 'frappe-ui';

const props = defineProps({
	siteName: { type: String, default: '' },
	storeHours: { type: String, default: '' },
	address: { type: String, default: '' },
	tagline: { type: String, default: '' },
});

const call = inject('$call', null);
const siteName = ref('');
const storeHours = ref('');
const address = ref('');
const email = ref('');
const newsletterMessage = ref('');
const newsletterSuccess = ref(false);

const socialLinks = [
	{ name: 'Instagram', url: 'https://instagram.com', icon: 'instagram' },
	{ name: 'Facebook', url: 'https://facebook.com', icon: 'facebook' },
	{ name: 'Twitter', url: 'https://twitter.com', icon: 'twitter' },
];

async function subscribe() {
	newsletterMessage.value = '';
	try {
		if (call) {
			await call('hrs.controllers.api.newsletter_subscribe', { email: email.value });
			newsletterSuccess.value = true;
			newsletterMessage.value = 'Thank you for subscribing!';
			email.value = '';
		} else {
			newsletterSuccess.value = true;
			newsletterMessage.value = 'Thank you for subscribing!';
			email.value = '';
		}
	} catch {
		newsletterSuccess.value = false;
		newsletterMessage.value = 'Something went wrong. Please try again.';
	}
}
</script>
