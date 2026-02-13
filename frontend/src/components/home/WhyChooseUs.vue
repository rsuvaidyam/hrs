<template>
	<section id="about" class="py-12 sm:py-16 md:py-20 px-4 sm:px-6 md:px-8 max-w-[1200px] mx-auto">
		<div class="text-center mb-10 md:mb-12">
			<p class="font-sans text-xs uppercase tracking-widest text-chocolate-soft mb-1.5">Our promise</p>
			<h2 class="font-serif text-2xl sm:text-3xl md:text-4xl font-semibold text-chocolate">Why Choose Us</h2>
		</div>

		<div class="grid grid-cols-1 sm:grid-cols-3 gap-6 md:gap-8">
			<article
				v-for="(item, i) in features"
				:key="item.title"
				class="text-center p-6 md:p-8 rounded-2xl bg-white shadow-soft transition-all duration-300 hover:shadow-lift hover:-translate-y-1 border border-cream-dark/50"
				v-motion
				:initial="{ opacity: 0, y: 16 }"
				:visible="{ opacity: 1, y: 0 }"
				:delay="i * 80"
			>
				<div class="w-14 h-14 mx-auto mb-4 rounded-xl bg-blush-soft flex items-center justify-center text-2xl">
					{{ item.emoji }}
				</div>
				<h3 class="font-serif text-lg font-semibold text-chocolate mb-1.5">{{ item.title }}</h3>
				<p class="text-chocolate-soft font-sans text-sm leading-relaxed">{{ item.description }}</p>
			</article>
		</div>
	</section>
</template>

<script setup>
const features = [
	{
		title: 'Fresh Ingredients',
		description: 'We source the finest local and organic ingredients so every bite is pure and delicious.',
		emoji: '🥬',
	},
	{
		title: 'Handcrafted',
		description: 'Every pastry and cake is made by our skilled bakers with traditional methods and love.',
		emoji: '❤️',
	},
	{
		title: 'Same-Day Delivery',
		description: 'Order by noon and enjoy fresh treats at your door the same day. We deliver with care.',
		emoji: '🚚',
	},
];
</script>
