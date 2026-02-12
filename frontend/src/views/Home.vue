<template>
	<div class="min-h-screen bg-[#fff8f3] text-[#3f2d2d]">
		<header
			:class="[
				'fixed inset-x-0 top-0 z-50 transition-all duration-500',
				scrolled
					? 'mx-2 mt-2 rounded-2xl border border-white/40 bg-[#fff6f0]/80 shadow-xl backdrop-blur-xl'
					: 'bg-transparent'
			]"
		>
			<nav class="mx-auto flex w-full max-w-7xl items-center justify-between px-4 py-4 lg:px-10">
				<div class="text-xl font-semibold tracking-[0.2em] text-[#7d4f44]">AURÉLIA</div>
				<ul class="hidden items-center gap-8 text-sm font-medium text-[#6b4a43] md:flex">
					<li v-for="item in navItems" :key="item" class="transition hover:text-[#a25c4d]">{{ item }}</li>
				</ul>
				<div class="flex items-center gap-3">
					<button class="icon-button" aria-label="Shopping cart">
						<ShoppingBagIcon class="h-5 w-5" />
					</button>
					<button class="icon-button" aria-label="Profile">
						<UserCircleIcon class="h-5 w-5" />
					</button>
				</div>
			</nav>
		</header>

		<main class="pb-16 pt-24">
			<section class="mx-auto grid max-w-7xl gap-8 px-4 lg:grid-cols-2 lg:px-10">
				<div class="relative overflow-hidden rounded-[24px] shadow-2xl">
					<img
						src="https://images.unsplash.com/photo-1517433670267-08bbd4be890f?auto=format&fit=crop&w=1400&q=80"
						alt="Fresh pastries on a wooden table"
						class="h-[460px] w-full object-cover"
					/>
					<div class="absolute inset-0 bg-gradient-to-r from-[#2b1f1fb3] via-[#2b1f1f66] to-transparent" />
				</div>
				<div class="flex flex-col justify-center">
					<p class="mb-4 text-sm font-semibold uppercase tracking-[0.25em] text-[#ad7a6f]">Luxury artisan bakery</p>
					<h1 class="hero-title text-5xl leading-tight text-[#fff8f3] md:text-6xl lg:text-[#4b2f2a]">
						Baked Fresh Every Morning
					</h1>
					<p class="mt-6 max-w-xl text-base leading-relaxed text-[#7a5d57]">
						{{ heroSubtext }}
					</p>
					<div class="mt-8 flex flex-wrap gap-4">
						<button class="primary-btn">Order Now</button>
						<button class="secondary-btn">Explore Menu</button>
					</div>
				</div>
			</section>

			<section class="mx-auto mt-20 max-w-7xl px-4 lg:px-10">
				<div class="mb-8 flex items-end justify-between">
					<div>
						<p class="section-kicker">Featured Picks</p>
						<h2 class="section-title">Crafted to impress at first bite</h2>
					</div>
				</div>
				<div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
					<article
						v-for="product in featuredProducts"
						:key="product.name"
						class="group overflow-hidden rounded-[24px] border border-white/60 bg-[#fffaf6] shadow-lg transition duration-300 hover:-translate-y-2 hover:shadow-2xl"
					>
						<div class="relative">
							<img :src="product.image" :alt="product.name" class="h-56 w-full object-cover" />
							<span class="badge">{{ product.tag }}</span>
						</div>
						<div class="space-y-3 p-5">
							<div class="flex items-center justify-between">
								<h3 class="text-lg font-semibold text-[#4b2f2a]">{{ product.name }}</h3>
								<p class="text-base font-semibold text-[#a05f4f]">₹{{ product.price }}</p>
							</div>
							<p class="text-sm leading-relaxed text-[#7a5d57]">{{ product.description }}</p>
							<button class="quick-btn">Quick add to cart</button>
						</div>
					</article>
				</div>
			</section>

			<section class="mx-auto mt-20 max-w-7xl px-4 lg:px-10">
				<p class="section-kicker">Browse by Mood</p>
				<h2 class="section-title">Your sweet moments, curated</h2>
				<div class="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
					<div
						v-for="category in categories"
						:key="category.name"
						class="rounded-[20px] bg-[#fffaf6] p-6 shadow-md transition duration-300 hover:-translate-y-1 hover:shadow-xl"
					>
						<p class="text-xs uppercase tracking-[0.22em] text-[#b9887e]">Category</p>
						<h3 class="mt-2 text-xl font-semibold text-[#4b2f2a]">{{ category.name }}</h3>
						<p class="mt-2 text-sm text-[#7a5d57]">{{ category.note }}</p>
					</div>
				</div>
			</section>

			<section class="mx-auto mt-20 max-w-7xl px-4 lg:px-10">
				<p class="section-kicker">Why Choose Us</p>
				<div class="mt-8 grid gap-5 md:grid-cols-3">
					<div v-for="feature in whyChooseUs" :key="feature.title" class="glass-card">
						<div class="mb-3 inline-flex rounded-xl bg-[#f8e7df] p-3 text-[#a05f4f]">
							<component :is="feature.icon" class="h-6 w-6" />
						</div>
						<h3 class="text-lg font-semibold text-[#4b2f2a]">{{ feature.title }}</h3>
						<p class="mt-2 text-sm text-[#7a5d57]">{{ feature.text }}</p>
					</div>
				</div>
			</section>

			<section class="mx-auto mt-20 max-w-7xl px-4 lg:px-10">
				<p class="section-kicker">Loved by Guests</p>
				<h2 class="section-title">Warm words from our regulars</h2>
				<div class="mt-8 grid gap-6 md:grid-cols-3">
					<article v-for="testimonial in testimonials" :key="testimonial.name" class="rounded-[24px] bg-white p-6 shadow-md">
						<div class="mb-4 flex items-center gap-3">
							<img :src="testimonial.avatar" :alt="testimonial.name" class="h-12 w-12 rounded-full object-cover" />
							<div>
								<p class="font-semibold text-[#4b2f2a]">{{ testimonial.name }}</p>
								<p class="text-xs text-[#8c6a63]">{{ testimonial.title }}</p>
							</div>
						</div>
						<p class="mb-4 text-[#7a5d57]">“{{ testimonial.text }}”</p>
						<p class="text-[#f2b01e]">★★★★★</p>
					</article>
				</div>
			</section>

			<section class="mx-auto mt-20 max-w-7xl px-4 lg:px-10">
				<div class="grid grid-cols-2 gap-4 md:grid-cols-4">
					<div v-for="(image, index) in gallery" :key="index" class="overflow-hidden rounded-2xl">
						<img :src="image" alt="Bakery gallery" class="h-44 w-full object-cover transition duration-500 hover:scale-105" />
					</div>
				</div>
			</section>
		</main>

		<footer class="mt-16 bg-[#2f1f1b] text-[#f7e9df]">
			<div class="mx-auto grid max-w-7xl gap-10 px-4 py-14 md:grid-cols-4 lg:px-10">
				<div>
					<h3 class="hero-title text-2xl">AURÉLIA</h3>
					<p class="mt-3 text-sm text-[#dbbfb0]">Freshly baked stories for the most beautiful mornings.</p>
				</div>
				<div>
					<p class="text-sm uppercase tracking-[0.2em] text-[#dbbfb0]">Newsletter</p>
					<div class="mt-3 flex overflow-hidden rounded-xl bg-[#fef5ef]">
						<input type="email" placeholder="Your email" class="w-full bg-transparent px-3 py-2 text-sm text-[#3f2d2d] outline-none" />
						<button class="bg-[#a05f4f] px-4 text-sm font-medium text-white">Join</button>
					</div>
				</div>
				<div>
					<p class="text-sm uppercase tracking-[0.2em] text-[#dbbfb0]">Store Hours</p>
					<p class="mt-3 text-sm">Mon - Sat: 7:00 AM – 9:00 PM</p>
					<p class="text-sm">Sun: 8:00 AM – 7:00 PM</p>
					<div class="mt-4 flex gap-3">
						<span class="social-dot">IG</span>
						<span class="social-dot">FB</span>
						<span class="social-dot">YT</span>
					</div>
				</div>
				<div>
					<p class="text-sm uppercase tracking-[0.2em] text-[#dbbfb0]">Visit Us</p>
					<div class="mt-3 rounded-xl bg-[#f8e7df]/20 p-4 text-xs text-[#f7e9df]">
						<p>24 Rosewood Avenue, Downtown</p>
						<p class="mt-2 rounded-lg bg-[#fef5ef]/20 p-2">Map Preview</p>
					</div>
				</div>
			</div>
		</footer>
	</div>
</template>

<script setup>
import { onMounted, onUnmounted, ref } from 'vue';
import {
	CakeIcon,
	SparklesIcon,
	TruckIcon,
	ShoppingBagIcon,
	UserCircleIcon
} from '@heroicons/vue/24/outline';

const navItems = ['Home', 'Menu', 'Story', 'Reviews', 'Contact'];
const heroSubtext =
	'From buttery croissants to indulgent celebration cakes, our chefs handcraft every batch with premium ingredients and timeless techniques.';

const fallbackData = {
	featured_products: [
		{
			name: 'Velvet Strawberry Gateau',
			price: 980,
			tag: 'Best Seller',
			description: 'Layers of vanilla sponge, fresh berries, and cloud-light cream.',
			image: 'https://images.unsplash.com/photo-1464306076886-debede6f7917?auto=format&fit=crop&w=900&q=80'
		},
		{
			name: 'Belgian Chocolate Tart',
			price: 760,
			tag: 'New',
			description: 'Dark chocolate ganache on a buttery almond shortcrust base.',
			image: 'https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=900&q=80'
		},
		{
			name: 'Rose Pistachio Pastry',
			price: 420,
			tag: 'Eggless',
			description: 'Fragrant rose milk cream and roasted pistachio praline crunch.',
			image: 'https://images.unsplash.com/photo-1559620192-032c4bc4674e?auto=format&fit=crop&w=900&q=80'
		}
	],
	categories: [
		{ name: 'Cakes', note: 'Celebration signatures in luxe finishes.' },
		{ name: 'Pastries', note: 'Delicate handcrafted bites for every craving.' },
		{ name: 'Artisan Bread', note: 'Long-fermented loaves baked every dawn.' },
		{ name: 'Cookies', note: 'Golden, buttery, and deeply comforting.' }
	],
	testimonials: [
		{
			name: 'Ananya R',
			title: 'Food Stylist',
			text: 'Everything tastes as beautiful as it looks. Their pastries feel straight out of Paris.',
			avatar: 'https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?auto=format&fit=crop&w=300&q=80'
		},
		{
			name: 'Rahul M',
			title: 'Loyal Customer',
			text: 'The same-day delivery is flawless and the cakes always arrive fresh and elegant.',
			avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=300&q=80'
		},
		{
			name: 'Sana K',
			title: 'Event Planner',
			text: 'Premium quality every single time. My clients now ask specifically for Aurélia desserts.',
			avatar: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=300&q=80'
		}
	],
	gallery: [
		'https://images.unsplash.com/photo-1519869325930-281384150729?auto=format&fit=crop&w=800&q=80',
		'https://images.unsplash.com/photo-1555507036-ab1f4038808a?auto=format&fit=crop&w=800&q=80',
		'https://images.unsplash.com/photo-1608198093002-ad4e005484ec?auto=format&fit=crop&w=800&q=80',
		'https://images.unsplash.com/photo-1514517220017-8ce97a34a7b6?auto=format&fit=crop&w=800&q=80'
	]
};

const featuredProducts = ref(fallbackData.featured_products);
const categories = ref(fallbackData.categories);
const testimonials = ref(fallbackData.testimonials);
const gallery = ref(fallbackData.gallery);
const scrolled = ref(false);

const whyChooseUs = [
	{ icon: CakeIcon, title: 'Fresh Ingredients', text: 'Daily sourced dairy, flour, and seasonal fruits.' },
	{ icon: SparklesIcon, title: 'Handcrafted', text: 'Each creation is shaped and finished by pastry chefs.' },
	{ icon: TruckIcon, title: 'Same-Day Delivery', text: 'Fast, temperature-safe delivery for special occasions.' }
];

const handleScroll = () => {
	scrolled.value = window.scrollY > 12;
};

const loadHomepageData = async () => {
	try {
		const response = await fetch('/api/method/hrs.controllers.api.get_homepage_content');
		const payload = await response.json();
		if (!payload?.message) return;
		featuredProducts.value = payload.message.featured_products || fallbackData.featured_products;
		categories.value = payload.message.categories || fallbackData.categories;
		testimonials.value = payload.message.testimonials || fallbackData.testimonials;
		gallery.value = payload.message.gallery || fallbackData.gallery;
	} catch (error) {
		console.error('Unable to load bakery homepage data', error);
	}
};

onMounted(() => {
	window.addEventListener('scroll', handleScroll);
	handleScroll();
	loadHomepageData();
});

onUnmounted(() => {
	window.removeEventListener('scroll', handleScroll);
});
</script>

<style scoped>
.hero-title,
.section-title {
	font-family: 'Playfair Display', Georgia, serif;
}

.section-title {
	font-size: clamp(1.8rem, 4vw, 2.5rem);
	color: #4b2f2a;
}

.section-kicker {
	font-size: 0.72rem;
	letter-spacing: 0.22em;
	text-transform: uppercase;
	color: #b9887e;
	font-weight: 700;
}

.icon-button {
	@apply rounded-full border border-white/70 bg-[#fff6f0]/90 p-2 text-[#6b4a43] shadow-sm transition hover:bg-white;
}

.primary-btn {
	@apply rounded-full bg-[#a05f4f] px-6 py-3 text-sm font-semibold text-white shadow-lg transition hover:-translate-y-0.5 hover:bg-[#8f4f40];
}

.secondary-btn {
	@apply rounded-full border border-[#d9b7ad] bg-white/80 px-6 py-3 text-sm font-semibold text-[#6b4a43] transition hover:bg-[#fff4ef];
}

.badge {
	@apply absolute left-4 top-4 rounded-full bg-[#fff6f0]/90 px-3 py-1 text-xs font-semibold text-[#8a4f42] backdrop-blur;
}

.quick-btn {
	@apply rounded-xl bg-[#f7e1d9] px-4 py-2 text-sm font-semibold text-[#7b483c] transition hover:bg-[#f2d2c8];
}

.glass-card {
	@apply rounded-[24px] border border-white/60 bg-white/55 p-6 shadow-md backdrop-blur;
}

.social-dot {
	@apply inline-flex h-8 w-8 items-center justify-center rounded-full bg-[#fef5ef]/20 text-xs;
}

@media (max-width: 1023px) {
	.hero-title {
		color: #fff8f3;
	}
}
</style>
