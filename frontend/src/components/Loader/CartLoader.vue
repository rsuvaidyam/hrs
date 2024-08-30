<template>
	<div class="h-full w-full flex flex-col md:flex-row gap-2 px-2 md:px-6">
		<div class="w-full md:w-[70%] h-full p-2 flex flex-col gap-3">
			<div class="w-full animate-pulse bg-gray-100 rounded-md h-28 p-2 flex justify-between" v-for="item in data"
				:key="item">
				<div class="flex gap-2">
					<div class="md:w-20 w-24 h-full rounded-md bg-gray-200"></div>
					<div class="flex flex-col gap-2">
						<p class="w-32 h-5 bg-gray-200 rounded-sm"></p>
						<p class="w-24 h-4 bg-gray-200 rounded-sm"></p>
						<p class="w-24 h-4 bg-gray-200 rounded-sm"></p>
					</div>
				</div>
				<div class="flex justify-end flex-col">
					<p class="w-16 h-8 bg-gray-200 rounded-sm"></p>
				</div>
			</div>
		</div>
		<div class="w-full md:w-[30%] h-full p-2">
			<div class="w-full h-56 bg-gray-200 animate-pulse rounded-md"></div>
		</div>
	</div>
</template>
<script setup>
import { ref } from 'vue';
const data = ref([1, 2, 3, 4, 5]);
</script>