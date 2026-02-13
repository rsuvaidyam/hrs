<template>
	<div class="w-full min-h-screen pt-14 pb-20 bg-gray-100">
		<div class="max-w-[1800px] mx-auto px-4 py-6">
			<div class="bg-white rounded-lg shadow-sm p-6 mb-4">
				<div class="flex items-center gap-4 mb-6">
					<div class="w-16 h-16 rounded-full bg-primary flex items-center justify-center text-white text-2xl font-bold">
						{{ userInitial }}
					</div>
					<div>
						<h1 class="text-xl font-semibold text-gray-800">{{ auth?.cookie?.full_name || 'User' }}</h1>
						<p class="text-sm text-gray-500">{{ session?.user || 'Not logged in' }}</p>
					</div>
				</div>
				<div class="border-t pt-4 space-y-2">
					<router-link to="/order" class="flex items-center justify-between py-3 px-2 rounded hover:bg-gray-50">
						<span class="flex items-center gap-2">
							<FeatherIcon name="shopping-bag" class="w-5 text-gray-600" />
							My Orders
						</span>
						<FeatherIcon name="chevron-right" class="w-5 text-gray-400" />
					</router-link>
					<router-link to="/address" class="flex items-center justify-between py-3 px-2 rounded hover:bg-gray-50">
						<span class="flex items-center gap-2">
							<FeatherIcon name="map-pin" class="w-5 text-gray-600" />
							Addresses
						</span>
						<FeatherIcon name="chevron-right" class="w-5 text-gray-400" />
					</router-link>
					<button
						class="w-full flex items-center justify-between py-3 px-2 rounded hover:bg-gray-50 text-left text-red-600"
						@click="auth.logout()"
					>
						<span class="flex items-center gap-2">
							<FeatherIcon name="log-out" class="w-5" />
							Logout
						</span>
					</button>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { computed, inject } from 'vue';
import { FeatherIcon } from 'frappe-ui';

const auth = inject('$auth');
const session = inject('$session');

const userInitial = computed(() => {
	const name = auth?.cookie?.full_name || session?.user || 'U';
	return name.trim().charAt(0).toUpperCase();
});
</script>
