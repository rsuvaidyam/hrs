<template>
    <div v-show="showNav" class="w-full h-16 fixed bg-chocolate bottom-0 left-0 right-0 z-30 transition-opacity duration-300 safe-bottom flex items-center px-2">
        <div class="w-full flex justify-around items-center">
            <router-link to="/" class="flex flex-col items-center gap-0.5 py-2 px-4 rounded-xl min-w-[64px] min-h-[44px] justify-center" :class="router.currentRoute.value.path === '/' ? 'bg-white/20' : ''">
                <FeatherIcon name="home" class="text-white w-6 h-6"/>
                <span class="text-white text-xs">Home</span>
            </router-link>
            <router-link to="/cart" class="flex flex-col items-center gap-0.5 py-2 px-4 rounded-xl min-w-[64px] min-h-[44px] justify-center relative" :class="router.currentRoute.value.path === '/cart' ? 'bg-white/20' : ''">
                <FeatherIcon name="shopping-cart" class="text-white w-6 h-6"/>
                <span class="text-white text-xs">View Cart</span>
                <span v-if="(store && store.cart_count > 0)" class="absolute top-1 right-2 min-w-[18px] h-[18px] flex items-center justify-center rounded-full bg-bakery-primary text-white text-xs font-bold">{{ store.cart_count }}</span>
            </router-link>
            <router-link to="/order" class="flex flex-col items-center gap-0.5 py-2 px-4 rounded-xl min-w-[64px] min-h-[44px] justify-center" :class="router.currentRoute.value.path === '/order' ? 'bg-white/20' : ''">
                <FeatherIcon name="shopping-bag" class="text-white w-6 h-6"/>
                <span class="text-white text-xs">Orders</span>
            </router-link>
        </div>
    </div>
</template>

<script setup>
import { onMounted, onUnmounted, ref, inject } from 'vue';
import { useRouter } from 'vue-router';
import FeatherIcon from 'frappe-ui/src/components/FeatherIcon.vue';

const router = useRouter();
const store = inject('store', { cart_count: 0 });
const showNav = ref(true);
let lastScroll = 0;

const handleScroll = () => {
    const currentScroll = window.pageYOffset;
    if (currentScroll > lastScroll && currentScroll > 0) {
        showNav.value = false; // Hide on scroll down
    } else {
        showNav.value = true; // Show on scroll up
    }
    lastScroll = currentScroll;
};

onMounted(() => {
    window.addEventListener('scroll', handleScroll);
});

onUnmounted(() => {
    window.removeEventListener('scroll', handleScroll);
});
</script>

<style scoped>
/* Optional smooth transition for the visibility */
.v-enter-active, .v-leave-active {
    transition: opacity 0.3s;
}
.v-enter-from, .v-leave-to {
    opacity: 0;
}
</style>
