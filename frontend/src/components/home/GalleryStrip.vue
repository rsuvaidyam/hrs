<template>
	<section class="py-16 md:py-20 px-0 overflow-hidden">
		<div class="text-center mb-10 md:mb-12 px-4">
			<p class="font-sans text-sm uppercase tracking-widest text-chocolate-soft mb-2">Behind the scenes</p>
			<h2 class="font-serif text-3xl md:text-4xl font-semibold text-chocolate">From Our Kitchen</h2>
		</div>

		<div class="flex gap-2 md:gap-4 overflow-x-auto pb-4 scroll-smooth" style="scrollbar-width: none;">
			<a
				v-for="(img, i) in galleryImages"
				:key="i"
				:href="img.url || img"
				target="_blank"
		rel="noopener noreferrer"
				class="flex-shrink-0 w-64 md:w-80 h-64 md:h-80 rounded-card overflow-hidden group focus:outline-none focus-visible:ring-2 focus-visible:ring-bakery-primary"
			>
				<img
					:src="img.url || img"
					:alt="img.alt || 'Bakery gallery'"
					class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110"
				/>
			</a>
		</div>
	</section>
</template>

<script setup>
import { ref, onMounted, inject } from 'vue';

const call = inject('$call', null);
const galleryImages = ref([]);

const defaultGallery = [
	{ url: 'https://images.unsplash.com/photo-1509440159596-0249088772ff?w=400&q=80', alt: 'Pastries' },
	{ url: 'https://images.unsplash.com/photo-1558961363-fa8fdf82db35?w=400&q=80', alt: 'Cakes' },
	{ url: 'https://images.unsplash.com/photo-1509365465985-25d11c17e812?w=400&q=80', alt: 'Bread' },
	{ url: 'https://images.unsplash.com/photo-1488477181946-6428a0291777?w=400&q=80', alt: 'Bakery' },
	{ url: 'https://images.unsplash.com/photo-1517433670267-fabb9f310f1e?w=400&q=80', alt: 'Coffee and pastry' },
	{ url: 'https://images.unsplash.com/photo-1541783245831-57d98fb82859?w=400&q=80', alt: 'Croissant' },
];

onMounted(async () => {
	try {
		if (call) {
			const res = await call('hrs.controllers.api.get_gallery', {});
			galleryImages.value = Array.isArray(res) && res.length ? res : defaultGallery;
		} else {
			galleryImages.value = defaultGallery;
		}
	} catch {
		galleryImages.value = defaultGallery;
	}
});
</script>
