<template>
	<section id="about" class="py-16 md:py-24 px-4 md:px-8 max-w-[1800px] mx-auto">
		<div class="text-center mb-12 md:mb-16">
			<p class="font-sans text-sm uppercase tracking-widest text-chocolate-soft mb-2">Our promise</p>
			<h2 class="font-serif text-3xl md:text-4xl lg:text-5xl font-semibold text-chocolate">Why Choose Us</h2>
		</div>

		<div class="grid grid-cols-1 md:grid-cols-3 gap-8 md:gap-12">
			<article
				v-for="(item, i) in features"
				:key="item.title"
				class="text-center p-8 rounded-card bg-white shadow-soft transition-all duration-300 hover:shadow-lift hover:-translate-y-1"
				v-motion
				:initial="{ opacity: 0, y: 20 }"
				:visible="{ opacity: 1, y: 0 }"
				:delay="i * 100"
			>
				<div class="w-16 h-16 mx-auto mb-6 rounded-2xl bg-blush-soft flex items-center justify-center text-chocolate">
					<span class="text-3xl">{{ item.emoji }}</span>
				</div>
				<h3 class="font-serif text-xl font-semibold text-chocolate mb-2">{{ item.title }}</h3>
				<p class="text-chocolate-soft font-sans text-sm md:text-base">{{ item.description }}</p>
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
