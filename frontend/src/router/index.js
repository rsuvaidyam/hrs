import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import ProductDetails from "../components/product/ProductDetails.vue";
import ProductList from "../components/product/ProductList.vue";
import authRoutes from './auth';

const routes = [
  {
	path: "/",
	name: "Home",
	component: Home,
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
