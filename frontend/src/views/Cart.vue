<!-- src/components/Cart.vue -->
<template>
	<div class="pt-10 md:pt-0 h-full">
		<div class="w-full h-full flex items-center justify-center" v-if="loading">
			<CartLoader />
		</div>
		<CartAlert v-else-if="!products.length" />
		<div v-else class=" pb-12 w-full h-full px-0 lg:px-4 bg-gray-100 relative">
			<div
				class="flex flex-col px-2 pb-2 md:flex-row gap-3 h-full pt-1 md:pt-3 overflow-y-auto md:overscroll-y-none scrollbar-thin">
				<div
					class="w-full md:w-[70%] md:overflow-y-auto px-2 rounded-md shadow-md md:shadow-none md:scrollbar-thin md:border h-auto md:h-full flex flex-col bg-white">
					<CartItem v-for="item in products" :key="item.name" :product="item"
						:isSelected="selectedProductIds.includes(item.name)" @delete="deleteItem"
						@quantityChange="updateCartItemCount" @select="toggleProductSelection" />
				</div>
				<div class="w-full md:w-[30%]">
					<div class="md:border rounded-md bg-white h-auto shadow-md md:shadow-none">
						<p class="text-lg text-gray-600 h-12 border-b flex items-center px-4">PRICE DETAILS</p>
						<div class="flex flex-col gap-5 p-4 border-b">
							<p class="flex justify-between items-center">Price <span class="flex items-center">
									<!-- <BiRupee class="text-base" /> -->
									{{ totalPrice }}</span></p>
							<p class="flex justify-between items-center">Discounts <span
									class="flex items-center text-primary">-
									<!-- <BiRupee class="text-base" /> -->
									{{ totalDiscounts }}</span></p>
							<p class="flex justify-between items-center">Delivery Charge <del
									class="flex items-center text-gray-500">
									<!-- <BiRupee class="text-base" /> -->
									40</del></p>
						</div>
						<p class="flex justify-between px-4 py-2 font-medium">Total Price <span
								class="flex items-center">
								<!-- <BiRupee class="text-base" /> -->
								{{ totalPriceWithDiscount }}</span></p>
					</div>
				</div>
			</div>
			<div v-if="selectedProductIds.length"
				class="fixed w-full left-0 bg-white h-12 z-50 bottom-0 px-2 md:px-16 flex justify-between items-center">
				<p class="text-xl text-gray-700 flex items-center">Total Price : <span
						class="text-lg flex items-center">
						<!-- <BiRupee /> -->
						 {{ totalPriceWithDiscount }}
					</span></p>
				<router-link to="/buy" class="text-white rounded-sm bg-primary py-1 px-8">PLACE ORDER</router-link>
			</div>
		</div>
	</div>
</template>

<script >
import { defineComponent, ref, computed, onMounted, watch, inject } from 'vue';
import CartItem from '../components/CartItem.vue';
import CartAlert from '../components/CartAlert.vue';
import CartLoader from '../components/Loader/CartLoader.vue';
export default defineComponent({
	name: 'Cart',
	components: { CartItem, CartAlert,CartLoader },
	setup() {
		const products = ref([]);
		const loading = ref(true);
		const selectedProductIds = ref([]);
		const call = inject('$call');
		const session = inject('$session');
		const fetchCart = async () => {
			try {
				const response = await call('hrs.controllers.cart.get_cart', { usr: session.user });
				products.value = response;
				selectedProductIds.value = response.map((e) => e.name);
				loading.value = false;
			} catch (error) {
				// Handle error, e.g., show a toast or redirect to login
				console.error(error);
			}
		};

		const deleteItem = async (name) => {
			try {
				const response = await call('hrs.controllers.cart.delete_item', { id: name });
				products.value = products.value.filter(product => product.name !== name);
				selectedProductIds.value = selectedProductIds.value.filter(pid => pid !== name);
			} catch (error) {
				console.error(error);
			}
		};

		  const updateCartItemCount = async (id, value) => {
		// 	try {
		// 	  onst response = await call('hrs.controllers.cart.update_item',{ id: id, value: value });
		// 	  const product = products.value.find(p => p.name === id);
		// 	  if (product) {
		// 		product.count = value;
		// 	  }
		// 	} catch (error) {
		// 	  console.error(error);
		// 	}
		  };

		  const toggleProductSelection = (id) => {
			const index = selectedProductIds.value.indexOf(id);
			if (index !== -1) {
			  selectedProductIds.value.splice(index, 1);
			} else {
			  selectedProductIds.value.push(id);
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

		onMounted(fetchCart);

		return { products, loading, selectedProductIds, totalPrice, totalDiscounts, totalPriceWithDiscount };
	},
});
</script>

<style scoped>
/* Add your styles here */
</style>