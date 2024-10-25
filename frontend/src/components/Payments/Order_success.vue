<template>
    <div class="w-full px-2 h-full flex flex-col gap-4 justify-center items-center">
        <span class="relative flex w-20 h-20 mb-10">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-200 opacity-75"></span>
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"></span>
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-500 opacity-75"></span>
            <span class="relative rounded-full w-20 h-20 bg-green-600 flex items-center justify-center">
                <FeatherIcon name="check" class="w-10 text-white" />
            </span>
        </span>
        <p class="text-3xl">Order Placed</p>
        <p class="text-lg">You saved 1200</p>
    </div>
</template>