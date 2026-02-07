<template>
  <section class="px-3 md:px-8 pt-6 max-w-[1800px] mx-auto w-full">
    <div
      class="bg-[#fff7f1] rounded-2xl p-6 md:p-10 flex flex-col lg:flex-row items-center gap-8 shadow-sm"
    >
      <div class="flex-1">
        <p class="text-sm uppercase tracking-[0.3em] text-primary font-semibold">Hearthstone Bakery</p>
        <h1 class="text-3xl md:text-5xl font-semibold text-main mt-2 leading-tight">
          Freshly baked breads, pastries, and celebration cakes made every morning.
        </h1>
        <p class="text-base md:text-lg text-tatary mt-4">
          From buttery croissants to handcrafted sourdough loaves, our kitchen is dedicated to warm,
          comforting flavors and beautiful bakes for every moment.
        </p>
        <div class="flex flex-wrap gap-3 mt-6">
          <router-link
            to="/product-list/category/celebration-cakes"
            class="bg-primary text-white px-5 py-2 rounded-md font-medium"
          >
            Shop Celebration Cakes
          </router-link>
          <router-link
            to="/product-list/category/artisan-breads"
            class="border border-primary text-primary px-5 py-2 rounded-md font-medium"
          >
            Explore Artisan Breads
          </router-link>
        </div>
        <div class="flex flex-wrap gap-6 mt-8 text-sm text-main">
          <div class="flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-primary"></span>
            <span>Locally sourced ingredients</span>
          </div>
          <div class="flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-primary"></span>
            <span>Same-day preorder pickups</span>
          </div>
          <div class="flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-primary"></span>
            <span>Custom celebration cakes</span>
          </div>
        </div>
      </div>
      <div class="flex-1 w-full">
        <div class="grid grid-cols-2 gap-4">
          <img
            class="rounded-xl object-cover h-40 md:h-52 w-full"
            src="https://images.unsplash.com/photo-1509365465985-25d11c17e812?auto=format&fit=crop&w=800&q=80"
            alt="Fresh croissants"
          />
          <img
            class="rounded-xl object-cover h-40 md:h-52 w-full"
            src="https://images.unsplash.com/photo-1542826438-bd32f43d626f?auto=format&fit=crop&w=800&q=80"
            alt="Celebration cake"
          />
          <img
            class="rounded-xl object-cover h-40 md:h-52 w-full"
            src="https://images.unsplash.com/photo-1549931319-a545dcf3bc73?auto=format&fit=crop&w=800&q=80"
            alt="Fresh sourdough"
          />
          <img
            class="rounded-xl object-cover h-40 md:h-52 w-full"
            src="https://images.unsplash.com/photo-1464347744102-11db6282f854?auto=format&fit=crop&w=800&q=80"
            alt="Fruit tart"
          />
        </div>
      </div>
    </div>
  </section>
</template>
