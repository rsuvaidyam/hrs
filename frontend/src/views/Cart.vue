<!-- src/components/Cart.vue -->
<template>
	<div class="pt-10 lg:pt-0 h-full mx-auto max-w-[1800px]" 
	v-motion :initial="{ opacity: 0, scale: 0.8 }" :enter="{ opacity: 1, scale: 1 }"
		:leave="{ opacity: 0, scale: 0.8 }"
	>
		<div class="w-full h-full flex items-center justify-center" v-if="loading">
			<CartLoader />
		</div>
		<CartAlert v-else-if="!products.length" />
		<div v-else class=" pb-12 w-full h-full px-0 lg:px-4 bg-gray-100 relative">
			<div
				class="flex flex-col px-2 pb-2 md:flex-row gap-3 h-full pt-1 md:pt-3 overflow-y-auto md:overscroll-y-none scrollbar-thin">
				<div
					class="w-full md:w-[70%] md:overflow-y-auto px-2 rounded-md shadow-md md:shadow-none md:scrollbar-thin md:border h-auto md:h-full flex flex-col bg-white">
					<CartItem v-for="item in products" :key="item.name" :product="item" />
				</div>
				<div class="w-full md:w-[30%]">
					<div class="md:border rounded-md bg-white h-auto shadow-md md:shadow-none">
						<p class="text-lg text-gray-600 h-12 border-b flex items-center px-4">PRICE DETAILS</p>
						<div class="flex flex-col gap-5 p-4 border-b">
							<p class="flex justify-between items-center">Price <span class="flex gap-0.5 items-center">
									<span>₹</span>
									{{ totalPrice }}</span></p>
							<p class="flex justify-between items-center">Discounts <span
									class="flex items-center text-primary">-
									<span>₹</span>
									{{ totalDiscounts }}</span></p>
							<p class="flex justify-between items-center">Delivery Charge <del
									class="flex items-center gap-0.5 text-gray-500">
									<span>₹</span>
									40</del></p>
						</div>
						<p class="flex justify-between px-4 py-2 font-medium">Total Price <span
								class="flex items-center gap-0.5">
								<span>₹</span>
								{{ totalPriceWithDiscount }}</span></p>
					</div>
				</div>
			</div>
			<div
				class="fixed w-full left-0 bg-white h-12 z-50 bottom-2 px-2 md:px-16 flex justify-between items-center">
				<p class="text-xl text-gray-700 flex items-end gap-1">Total <span class="text-lg flex items-center">
						<span>₹</span>
						{{ totalPriceWithDiscount }}
					</span></p>
				<router-link to="/buy" class="text-white rounded-sm bg-primary py-1 px-8">PLACE ORDER</router-link>
			</div>
		</div>
	</div>
</template>

<script>
import { defineComponent, ref, computed, onMounted, watch, inject } from 'vue';
import CartItem from '../components/CartItem.vue';
import CartAlert from '../components/CartAlert.vue';
import CartLoader from '../components/Loader/CartLoader.vue';
export default defineComponent({
	name: 'Cart',
	components: { CartItem, CartAlert, CartLoader },
	setup() {
		const products = ref([]);
		const loading = ref(true);
		const call = inject('$call');
		const session = inject('$session');
		const fetchCart = async () => {
			try {
				const response = await call('hrs.controllers.cart.get_cart', { usr: session.user });
				products.value = response;
				loading.value = false;

			} catch (error) {
				// Handle error, e.g., show a toast or redirect to login
				console.error(error);
			}
		};

		const totalPrice = computed(() => {
			return products.value.reduce((total, product) => {
				return total + (product.product.discounts ? Math.ceil((100 - product.product.discounts) / 100 * product.product.price) * product.count : product.product.price * product.count);
			}, 0);
		});

		const totalDiscounts = computed(() => {
			return products.value.reduce((total, product) => {
				return total + (product.product.discounts ? (product.product.price * product.count - (Math.ceil((100 - product.product.discounts) / 100 * product.product.price) * product.count)) : 0);
			}, 0);
		});

		const totalPriceWithDiscount = computed(() => totalPrice.value - totalDiscounts.value);
		watch(() => products.value, (newProducts) => {
			newProducts.forEach(product => {
				if (product.count === 0) {
					fetchCart()
				}
			});
		}, { deep: true,immediate: true });
		onMounted(fetchCart);

		return { products, loading, totalPrice, totalDiscounts, totalPriceWithDiscount };
	},
});
</script>

<style scoped>
/* Add your styles here */
</style>