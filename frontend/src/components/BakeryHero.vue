<template>
  <section class="px-3 md:px-8 pt-6 max-w-[1800px] mx-auto w-full">
    <div
      class="bg-[#f2fbf6] rounded-2xl p-6 md:p-10 flex flex-col lg:flex-row items-center gap-8 shadow-sm"
    >
      <div class="flex-1">
        <p class="text-sm uppercase tracking-[0.3em] text-primary font-semibold">Ferns N Petals</p>
        <h1 class="text-3xl md:text-5xl font-semibold text-main mt-2 leading-tight">
          Send flowers, cakes, and gifts that arrive fresh and on time.
        </h1>
        <p class="text-base md:text-lg text-tatary mt-4">
          Celebrate birthdays, anniversaries, and everyday wins with curated bouquets, decadent
          cakes, and thoughtful hampers delivered across India.
        </p>
        <div class="flex flex-wrap gap-3 mt-6">
          <router-link
            to="/product-list/category/flowers"
            class="bg-primary text-white px-5 py-2 rounded-md font-medium"
          >
            Shop Fresh Flowers
          </router-link>
          <router-link
            to="/product-list/category/gift-hampers"
            class="border border-primary text-primary px-5 py-2 rounded-md font-medium"
          >
            Explore Gift Hampers
          </router-link>
        </div>
        <div class="flex flex-wrap gap-6 mt-8 text-sm text-main">
          <div class="flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-primary"></span>
            <span>Same-day delivery in 350+ cities</span>
          </div>
          <div class="flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-primary"></span>
            <span>Hand-tied bouquets & premium cakes</span>
          </div>
          <div class="flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-primary"></span>
            <span>Free message cards with every gift</span>
          </div>
        </div>
      </div>
      <div class="flex-1 w-full">
        <div class="grid grid-cols-2 gap-4">
          <img
            class="rounded-xl object-cover h-40 md:h-52 w-full"
            src="https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=format&fit=crop&w=800&q=80"
            alt="Pink rose bouquet"
          />
          <img
            class="rounded-xl object-cover h-40 md:h-52 w-full"
            src="https://images.unsplash.com/photo-1486427944299-d1955d23e34d?auto=format&fit=crop&w=800&q=80"
            alt="Gift hamper"
          />
          <img
            class="rounded-xl object-cover h-40 md:h-52 w-full"
            src="https://images.unsplash.com/photo-1542835435-4b8d3f24a51a?auto=format&fit=crop&w=800&q=80"
            alt="Chocolate cake"
          />
          <img
            class="rounded-xl object-cover h-40 md:h-52 w-full"
            src="https://images.unsplash.com/photo-1509042239860-f550ce710b93?auto=format&fit=crop&w=800&q=80"
            alt="Assorted flowers"
          />
        </div>
      </div>
    </div>
  </section>
</template>
