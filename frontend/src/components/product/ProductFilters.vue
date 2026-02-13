<template>
	<div class="flex flex-wrap items-center gap-2 md:gap-3 py-3 px-2 md:px-8">
		<span class="text-sm font-medium text-chocolate-soft mr-1">Filters:</span>
		<button
			v-for="f in filters"
			:key="f.key"
			@click="toggle(f.key)"
			:class="[
				'px-3 py-1.5 rounded-button text-sm font-medium transition-colors',
				active[f.key]
					? 'bg-bakery-primary text-white shadow-soft'
					: 'bg-white border border-chocolate/20 text-chocolate hover:border-bakery-primary hover:text-bakery-primary'
			]"
		>
			{{ f.label }}
		</button>
	</div>
</template>

<script setup>
import { reactive, watch } from 'vue';

const props = defineProps({
	modelValue: { type: Object, default: () => ({}) },
});

const emit = defineEmits(['update:modelValue']);

const filters = [
	{ key: 'eggless', label: 'Eggless' },
	{ key: 'vegan', label: 'Vegan' },
	{ key: 'gluten_free', label: 'Gluten Free' },
];

const active = reactive({
	eggless: !!props.modelValue.eggless,
	vegan: !!props.modelValue.vegan,
	gluten_free: !!props.modelValue.gluten_free,
});

function toggle(key) {
	active[key] = !active[key];
	const out = {};
	filters.forEach((f) => {
		if (active[f.key]) out[f.key] = 1;
	});
	emit('update:modelValue', out);
}

watch(
	() => props.modelValue,
	(v) => {
		active.eggless = !!v.eggless;
		active.vegan = !!v.vegan;
		active.gluten_free = !!v.gluten_free;
	},
	{ deep: true }
);
</script>
