import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import ProductDetails from "../components/product/ProductDetails.vue";
import ProductList from "../components/product/ProductList.vue";
import authRoutes from './auth';
import PlaceOrder from '../views/PlaceOrder.vue';
import Address from '../views/Address.vue';
import MyOrder from '../views/MyOrder.vue';
import Profile from '../views/Profile.vue';
import OrderItem from "../components/OrderItem.vue";

const routes = [
  {
	path: "/",
	name: "Home",
	component: Home,
  },
  {
	path: "/profile",
	name: "Profile",
	component: Profile,
  },
  {
	path: "/order",
	name: "MyOrder",
	component: MyOrder,
  },
  {
	path: "/order/:name",
	name: "OrderItem",
	component: OrderItem,
  },
  {
	path: "/productdetails/:name",
	name: "ProductDetails",
	component: ProductDetails,
  },
  {
	path: "/product-list/category/:name",
	name: "ProductListCategory",
	component: ProductList,
  },
  {
	path: "/product-list/event/:name",
	name: "ProductListEvent",
	component: ProductList,
  },
  {
	path: "/place-order",
	name: "PlaceOrder",
	component: PlaceOrder,
  },
  {
	path: "/address",
	name: "Address",
	component: Address,
  },
  // {
	// path: "/productlist/event/:name",
	// name: "ProductDetails",
	// component: ProductDetails,
  // },
  ...authRoutes,
];

const router = createRouter({
  history: createWebHistory("/hrs"),
  routes,
});

export default router;
