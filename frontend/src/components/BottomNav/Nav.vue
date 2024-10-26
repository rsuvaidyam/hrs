<template>
    <div v-show="showNav" class="w-full h-14 fixed bg-primary bottom-0 transition-opacity duration-1000">
        <div class="w-full flex justify-around items-center h-full">
            <router-link to="/" :class="router.currentRoute.value.path === '/' ? 'bg-gray-600 p-3 rounded-full' : ''">
                <FeatherIcon name="home" class="text-white w-6"/>
            </router-link>
            <div :class="router.currentRoute.value.path === '/notification' ? 'bg-gray-600 p-3 rounded-full' : ''">
                <FeatherIcon name="bell" class="text-white w-6"/>
            </div>
            <router-link to="/order" :class="router.currentRoute.value.path === '/order' ? 'bg-gray-600 p-3 rounded-full' : ''">
                <FeatherIcon name="shopping-bag" class="text-white w-6"/>
            </router-link>
        </div>
    </div>
</template>

<script setup>
import { onMounted, onUnmounted, ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
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
