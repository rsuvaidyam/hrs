<template>
	<section class="relative py-12 sm:py-16 md:py-20 px-5 sm:px-8 md:px-10 overflow-hidden">
		<!-- Contrasting background with subtle pattern -->
		<div class="absolute inset-0 bg-gradient-to-br from-chocolate via-chocolate/95 to-[#3d2a20]" aria-hidden="true" />
		<div class="absolute inset-0 opacity-[0.06]" style="background-image: url('data:image/svg+xml,%3Csvg width=\'60\' height=\'60\' viewBox=\'0 0 60 60\' xmlns=\'http://www.w3.org/2000/svg\'%3E%3Cpath d=\'M30 0L60 30L30 60L0 30Z\' fill=\'%23fff\' fill-opacity=\'.4\'/%3E%3C/svg%3E');" aria-hidden="true" />
		<!-- Decorative blobs (frosting shapes) -->
		<div class="absolute top-10 right-10 w-32 h-32 rounded-full bg-blush/20 blur-2xl" aria-hidden="true" />
		<div class="absolute bottom-10 left-10 w-40 h-40 rounded-full bg-beige/20 blur-3xl" aria-hidden="true" />

		<div class="relative z-10 max-w-4xl mx-auto text-center">
			<h2 class="font-serif text-3xl md:text-4xl lg:text-5xl font-semibold text-white mb-4">
				Design Your Dream Cake
			</h2>
			<p class="text-white/90 text-lg md:text-xl mb-8 font-sans font-light max-w-xl mx-auto">
				Choose flavours, layers, and decorations. We’ll bring your vision to life.
			</p>
			<router-link
				to="/product-list/category/all"
				class="inline-flex items-center justify-center gap-2 px-8 py-4 md:px-10 md:py-5 rounded-pill bg-white text-chocolate font-semibold text-base md:text-lg shadow-lift transition-all duration-300 hover:bg-cream hover:shadow-[0_16px_48px_rgba(0,0,0,0.2)] hover:-translate-y-1 focus:outline-none focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-offset-2 focus-visible:ring-offset-chocolate"
			>
				Start Customizing
				<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z" /><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
			</router-link>
		</div>
	</section>
</template>

<script setup>
</script>
