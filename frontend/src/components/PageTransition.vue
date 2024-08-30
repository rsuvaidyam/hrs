<template>
  <transition
    name="fade"
    @before-enter="beforeEnter"
    @enter="enter"
    @leave="leave"
  >
    <slot></slot>
  </transition>
</template>

<script setup>
const beforeEnter = (el) => {
  el.style.opacity = 0;
};

const enter = (el, done) => {
  const fadeIn = () => {
    let opacity = parseFloat(el.style.opacity);
    if (opacity < 1) {
      el.style.opacity = opacity + 0.1;
      requestAnimationFrame(fadeIn);
    } else {
      done();
    }
  };
  fadeIn();
};

const leave = (el, done) => {
  const fadeOut = () => {
    let opacity = parseFloat(el.style.opacity);
    if (opacity > 0) {
      el.style.opacity = opacity - 0.1;
      requestAnimationFrame(fadeOut);
    } else {
      done();
    }
  };
  fadeOut();
};
</script>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s ease-out;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>
