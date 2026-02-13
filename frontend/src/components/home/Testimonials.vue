<template>
	<section class="py-16 md:py-24 px-4 md:px-8 bg-cream-dark/50">
		<div class="max-w-[1800px] mx-auto">
			<div class="text-center mb-12 md:mb-16">
				<p class="font-sans text-sm uppercase tracking-widest text-chocolate-soft mb-2">Kind words</p>
				<h2 class="font-serif text-3xl md:text-4xl lg:text-5xl font-semibold text-chocolate">What Our Customers Say</h2>
			</div>

			<div class="relative overflow-hidden">
				<div
					class="flex gap-6 md:gap-8 overflow-x-auto pb-4 snap-x snap-mandatory scroll-smooth"
					ref="carousel"
					style="scrollbar-width: none; -ms-overflow-style: none;"
				>
					<article
						v-for="(t, i) in testimonials"
						:key="t.id || i"
						class="flex-shrink-0 w-[85vw] sm:w-[70vw] md:w-[400px] snap-center rounded-card bg-white p-6 md:p-8 shadow-soft"
					>
						<div class="flex gap-1 mb-4" aria-label="5 out of 5 stars">
							<svg v-for="s in 5" :key="s" class="w-5 h-5 text-amber-400" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" /></svg>
						</div>
						<p class="text-chocolate font-sans text-base md:text-lg leading-relaxed italic">"{{ t.quote }}"</p>
						<div class="mt-6 flex items-center gap-4">
							<div class="w-12 h-12 rounded-full bg-blush flex items-center justify-center text-chocolate font-serif font-semibold">
								{{ (t.customer_name || 'Customer')[0] }}
							</div>
							<div>
								<p class="font-semibold text-chocolate">{{ t.customer_name || 'Customer' }}</p>
								<p v-if="t.role" class="text-sm text-chocolate-soft">{{ t.role }}</p>
							</div>
						</div>
					</article>
				</div>
			</div>
		</div>
	</section>
</template>

<script setup>
import { ref, onMounted, inject } from 'vue';

const call = inject('$call', null);
const carousel = ref(null);
const testimonials = ref([]);

onMounted(async () => {
	try {
		if (call) {
			const res = await call('hrs.controllers.api.get_testimonials', {});
			testimonials.value = Array.isArray(res) && res.length ? res : defaultTestimonials;
		} else {
			testimonials.value = defaultTestimonials;
		}
	} catch {
		testimonials.value = defaultTestimonials;
	}
});

const defaultTestimonials = [
	{ id: 1, quote: 'The best croissants in town. Fresh, buttery, and always consistent.', customer_name: 'Priya S.', role: 'Regular customer' },
	{ id: 2, quote: 'Ordered a custom cake for my daughter\'s birthday. It was stunning and delicious!', customer_name: 'Rahul M.', role: '' },
	{ id: 3, quote: 'Same-day delivery and the bread was still warm. Incredible service.', customer_name: 'Anita K.', role: 'First-time buyer' },
];
</script>
