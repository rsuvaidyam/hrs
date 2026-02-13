<template>
	<header
		class="fixed top-0 left-0 right-0 z-50 transition-all duration-300"
		:class="scrolled ? 'bg-cream/80 backdrop-blur-xl shadow-glass border-b border-white/20' : 'bg-transparent'"
	>
		<div class="max-w-[1800px] mx-auto px-4 md:px-8">
			<div class="flex items-center justify-between h-16 md:h-18">
				<!-- Logo -->
				<router-link
					to="/"
					class="font-serif text-2xl md:text-3xl font-semibold transition-colors"
					:class="scrolled ? 'text-chocolate' : 'text-white drop-shadow-md'"
				>
					{{ siteName || (siteSettings && siteSettings.site_name) || 'Store' }}
				</router-link>

				<!-- Center nav - desktop -->
				<nav class="hidden md:flex items-center gap-8" aria-label="Main navigation">
					<router-link
						to="/"
						class="text-sm font-medium transition-colors hover:opacity-90"
						:class="scrolled ? 'text-chocolate' : 'text-white/95'"
					>
						Home
					</router-link>
					<router-link
						to="/#featured"
						class="text-sm font-medium transition-colors hover:opacity-90"
						:class="scrolled ? 'text-chocolate' : 'text-white/95'"
					>
						Menu
					</router-link>
					<router-link
						to="/#categories"
						class="text-sm font-medium transition-colors hover:opacity-90"
						:class="scrolled ? 'text-chocolate' : 'text-white/95'"
					>
						Categories
					</router-link>
					<router-link
						to="/#about"
						class="text-sm font-medium transition-colors hover:opacity-90"
						:class="scrolled ? 'text-chocolate' : 'text-white/95'"
					>
						Why Us
					</router-link>
				</nav>

				<!-- Right: search, cart, profile -->
				<div class="flex items-center gap-3 md:gap-5">
					<div class="hidden lg:block w-64 xl:w-80">
						<GlobalSearch />
					</div>
					<router-link
						v-if="route.path !== '/cart'"
						to="/cart"
						class="relative p-2 rounded-xl transition-colors"
						:class="scrolled ? 'text-chocolate hover:bg-cream-dark' : 'text-white hover:bg-white/10'"
						aria-label="Cart"
					>
						<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
							<path stroke-linecap="round" stroke-linejoin="round" d="M15.75 10.5V6a3.75 3.75 0 1 0-7.5 0v4.5m11.356-1.993 1.263 12c.07.665-.45 1.243-1.119 1.243H4.25a1.125 1.125 0 0 1-1.12-1.243l1.264-12A1.125 1.125 0 0 1 5.513 7.5h12.974c.576 0 1.059.435 1.119 1.007Z" />
						</svg>
						<span
							v-if="count >= 1"
							class="absolute -top-0.5 -right-0.5 min-w-[1.25rem] h-5 px-1 flex items-center justify-center rounded-full bg-bakery-primary text-white text-xs font-bold"
						>
							{{ count }}
						</span>
					</router-link>
					<Dropdown
						v-if="auth.isLoggedIn"
						:options="dropdownOptions"
						:button="dropdownButton"
					/>
					<Login v-else />
				</div>
			</div>
			<!-- Mobile search -->
			<div class="block lg:hidden pb-3">
				<GlobalSearch />
			</div>
		</div>
	</header>
	<!-- Floating cart FAB on mobile when not on cart -->
	<router-link
		v-if="route.fullPath !== '/cart' && !['/cart', '/order'].includes(route.path) && count >= 1"
		to="/cart"
		class="fixed bottom-20 right-4 z-40 flex items-center justify-center w-14 h-14 rounded-2xl bg-bakery-primary text-white shadow-lift transition-transform hover:scale-105 focus:outline-none focus-visible:ring-2 focus-visible:ring-bakery-primary"
		aria-label="Go to cart"
	>
		<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-7 h-7">
			<path stroke-linecap="round" stroke-linejoin="round" d="M15.75 10.5V6a3.75 3.75 0 1 0-7.5 0v4.5m11.356-1.993 1.263 12c.07.665-.45 1.243-1.119 1.243H4.25a1.125 1.125 0 0 1-1.12-1.243l1.264-12A1.125 1.125 0 0 1 5.513 7.5h12.974c.576 0 1.059.435 1.119 1.007Z" />
		</svg>
		<span class="absolute -top-1 -right-1 min-w-[1.25rem] h-5 flex items-center justify-center rounded-full bg-chocolate text-cream text-xs font-bold">{{ count }}</span>
	</router-link>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch, inject } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import GlobalSearch from '../GlobalSearch.vue';
import Login from '../../pages/Login.vue';
import { Dropdown } from 'frappe-ui';

const route = useRoute();
const router = useRouter();
const store = inject('store');
const auth = inject('$auth');
const call = inject('$call');
const session = inject('$session');

const scrolled = ref(false);
const count = ref(0);
const siteName = ref('');
const siteSettings = inject('siteSettings', ref({}));

const dropdownOptions = [
	{ label: 'Profile', onClick: () => router.push({ name: 'Profile' }) },
	{ label: 'My Orders', onClick: () => router.push({ name: 'MyOrder' }) },
	{ label: 'Logout', onClick: () => auth.logout() },
];
const dropdownButton = {
	label: (auth && auth.cookie && auth.cookie.full_name ? auth.cookie.full_name.split(' ')[0][0] : 'U') || 'U',
	variant: 'outline',
	theme: 'gray',
	size: 'md',
};

function onScroll() {
	scrolled.value = window.scrollY > 60 || route.path !== '/';
}

async function getCart() {
	try {
		const res = auth.isLoggedIn ? await call('hrs.controllers.api.cart_count', { usr: session.user }) : 0;
		count.value = res || 0;
		store.cart_count = res;
	} catch {
		count.value = 0;
	}
}

watch(() => auth.isLoggedIn, getCart, { immediate: true });
watch(() => store.cart_count, (n) => { count.value = n; });
watch(() => route.path, () => { scrolled.value = route.path !== '/'; }, { immediate: true });

onMounted(() => {
	scrolled.value = route.path !== '/';
	window.addEventListener('scroll', onScroll, { passive: true });
	getCart();
	if (siteSettings && typeof siteSettings === 'object' && 'site_name' in siteSettings) {
		siteName.value = siteSettings.site_name || '';
	}
});
onUnmounted(() => window.removeEventListener('scroll', onScroll));
</script>
