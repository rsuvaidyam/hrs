<!-- src/components/PageTransition.vue -->
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
  import { useMotion } from '@vueuse/motion';
  
  const { fadeIn, fadeOut } = useMotion();
  
  const beforeEnter = (el) => {
    fadeOut(el);
  };
  
  const enter = (el, done) => {
    fadeIn(el, done);
  };
  
  const leave = (el, done) => {
    fadeOut(el, done);
  };
  </script>
  
  <style scoped>
  .fade-enter-active, .fade-leave-active {
    transition: opacity 1s ease-in-out; /* Added easing function */
  }
  
  .fade-enter, .fade-leave-to /* .fade-leave-active in <2.1.8 */ {
    opacity: 0;
  }
  
  /* Optional: Add some scale transformation for a more dynamic effect */
  .fade-enter {
    transform: scale(0.5);
  }
  
  .fade-enter-to {
    transform: scale(2);
  }
  
  .fade-leave-to {
    transform: scale(2);
  }
  </style>
  