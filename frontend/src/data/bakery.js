const bakeryCarousel = [
  {
    name: 'sunrise-breads',
    image:
      'https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=1600&q=80',
    mimetype: 'image/jpeg',
  },
  {
    name: 'pastry-counter',
    image:
      'https://images.unsplash.com/photo-1523294587484-bae6cc870010?auto=format&fit=crop&w=1600&q=80',
    mimetype: 'image/jpeg',
  },
  {
    name: 'celebration-cakes',
    image:
      'https://images.unsplash.com/photo-1542826438-bd32f43d626f?auto=format&fit=crop&w=1600&q=80',
    mimetype: 'image/jpeg',
  },
];

const bakeryCategories = [
  {
    name: 'artisan-breads',
    name1: 'Artisan Breads',
    image:
      'https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=800&q=80',
  },
  {
    name: 'buttery-pastries',
    name1: 'Buttery Pastries',
    image:
      'https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=800&q=80',
  },
  {
    name: 'tarts',
    name1: 'Seasonal Tarts',
    image:
      'https://images.unsplash.com/photo-1464347744102-11db6282f854?auto=format&fit=crop&w=800&q=80',
  },
  {
    name: 'celebration-cakes',
    name1: 'Celebration Cakes',
    image:
      'https://images.unsplash.com/photo-1542826438-bd32f43d626f?auto=format&fit=crop&w=800&q=80',
  },
  {
    name: 'cookies-bars',
    name1: 'Cookies & Bars',
    image:
      'https://images.unsplash.com/photo-1541599540903-216a46ca1dc0?auto=format&fit=crop&w=800&q=80',
  },
];

const bakeryEvents = [
  {
    name: 'morning-bakes',
    name1: 'Morning Bakes',
    image:
      'https://images.unsplash.com/photo-1483695028939-5bb13f8648b0?auto=format&fit=crop&w=1200&q=80',
  },
  {
    name: 'afternoon-treats',
    name1: 'Afternoon Treats',
    image:
      'https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=1200&q=80',
  },
  {
    name: 'celebration-cakes',
    name1: 'Celebration Cakes',
    image:
      'https://images.unsplash.com/photo-1542826438-bd32f43d626f?auto=format&fit=crop&w=1200&q=80',
  },
];

const bakeryProducts = [
  {
    name: 'sourdough-loaf',
    name1: 'Classic Sourdough Loaf',
    category: 'artisan-breads',
    events: 'morning-bakes',
    images: [
      {
        name: 'sourdough-main',
        image:
          'https://images.unsplash.com/photo-1549931319-a545dcf3bc73?auto=format&fit=crop&w=900&q=80',
      },
      {
        name: 'sourdough-slice',
        image:
          'https://images.unsplash.com/photo-1483695028939-5bb13f8648b0?auto=format&fit=crop&w=900&q=80',
      },
    ],
    items: [
      {
        name: 'sourdough-loaf-500g',
        name1: 'Classic Sourdough Loaf',
        qty: 500,
        unit: 'g',
        price: 280,
        discounts: 10,
        final_price: 252,
        description:
          'Naturally leavened sourdough with a caramelized crust and a soft, tangy crumb. Fermented for 24 hours for maximum flavor.',
        key_features:
          '<ul><li>Slow-fermented for 24 hours</li><li>Stone-baked crust</li><li>No preservatives</li></ul>',
        count: 0,
        parent: 'sourdough-loaf',
      },
    ],
    owner: 'Hearthstone Bakery',
  },
  {
    name: 'butter-croissant',
    name1: 'Butter Croissant',
    category: 'buttery-pastries',
    events: 'morning-bakes',
    images: [
      {
        name: 'croissant-main',
        image:
          'https://images.unsplash.com/photo-1509365465985-25d11c17e812?auto=format&fit=crop&w=900&q=80',
      },
      {
        name: 'croissant-stack',
        image:
          'https://images.unsplash.com/photo-1495147466023-ac5c588e2e94?auto=format&fit=crop&w=900&q=80',
      },
    ],
    items: [
      {
        name: 'butter-croissant-single',
        name1: 'Butter Croissant',
        qty: 1,
        unit: 'pc',
        price: 90,
        discounts: 0,
        final_price: 90,
        description:
          'Layered, flaky, and baked with cultured butter for a crisp exterior and tender interior.',
        key_features:
          '<ul><li>Hand-laminated dough</li><li>Golden, flaky layers</li><li>Made with cultured butter</li></ul>',
        count: 0,
        parent: 'butter-croissant',
      },
      {
        name: 'butter-croissant-pack',
        name1: 'Butter Croissant (Pack of 4)',
        qty: 4,
        unit: 'pcs',
        price: 320,
        discounts: 5,
        final_price: 304,
        description:
          'Perfect for sharing — four buttery croissants baked fresh every morning.',
        key_features:
          '<ul><li>Pack of four</li><li>Freshly baked daily</li><li>Best served warm</li></ul>',
        count: 0,
        parent: 'butter-croissant',
      },
    ],
    owner: 'Hearthstone Bakery',
  },
  {
    name: 'berry-tart',
    name1: 'Seasonal Berry Tart',
    category: 'tarts',
    events: 'afternoon-treats',
    images: [
      {
        name: 'berry-tart-main',
        image:
          'https://images.unsplash.com/photo-1464347744102-11db6282f854?auto=format&fit=crop&w=900&q=80',
      },
      {
        name: 'berry-tart-slice',
        image:
          'https://images.unsplash.com/photo-1511919884226-fd3cad34687c?auto=format&fit=crop&w=900&q=80',
      },
    ],
    items: [
      {
        name: 'berry-tart-6inch',
        name1: 'Seasonal Berry Tart',
        qty: 6,
        unit: 'inch',
        price: 540,
        discounts: 8,
        final_price: 497,
        description:
          'A crisp almond crust filled with vanilla pastry cream and topped with seasonal berries.',
        key_features:
          '<ul><li>Almond sable crust</li><li>Vanilla pastry cream</li><li>Seasonal berries</li></ul>',
        count: 0,
        parent: 'berry-tart',
      },
    ],
    owner: 'Hearthstone Bakery',
  },
  {
    name: 'chocolate-cake',
    name1: 'Double Chocolate Celebration Cake',
    category: 'celebration-cakes',
    events: 'celebration-cakes',
    images: [
      {
        name: 'chocolate-cake-main',
        image:
          'https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=900&q=80',
      },
      {
        name: 'chocolate-cake-slice',
        image:
          'https://images.unsplash.com/photo-1542826438-bd32f43d626f?auto=format&fit=crop&w=900&q=80',
      },
    ],
    items: [
      {
        name: 'chocolate-cake-1kg',
        name1: 'Double Chocolate Celebration Cake',
        qty: 1,
        unit: 'kg',
        price: 1200,
        discounts: 12,
        final_price: 1056,
        description:
          'Moist chocolate sponge layered with dark chocolate ganache and finished with silky buttercream.',
        key_features:
          '<ul><li>Three layers of chocolate sponge</li><li>Dark chocolate ganache</li><li>Custom message included</li></ul>',
        count: 0,
        parent: 'chocolate-cake',
      },
      {
        name: 'chocolate-cake-2kg',
        name1: 'Double Chocolate Celebration Cake (2kg)',
        qty: 2,
        unit: 'kg',
        price: 2200,
        discounts: 10,
        final_price: 1980,
        description:
          'Extra-large celebration cake for gatherings and milestones.',
        key_features:
          '<ul><li>Serves 20-24 guests</li><li>Custom message included</li><li>Made to order</li></ul>',
        count: 0,
        parent: 'chocolate-cake',
      },
    ],
    owner: 'Hearthstone Bakery',
  },
  {
    name: 'caramel-cookie-box',
    name1: 'Salted Caramel Cookie Box',
    category: 'cookies-bars',
    events: 'afternoon-treats',
    images: [
      {
        name: 'caramel-cookie-main',
        image:
          'https://images.unsplash.com/photo-1499636136210-6f4ee915583e?auto=format&fit=crop&w=900&q=80',
      },
      {
        name: 'caramel-cookie-stack',
        image:
          'https://images.unsplash.com/photo-1486427944299-d1955d23e34d?auto=format&fit=crop&w=900&q=80',
      },
    ],
    items: [
      {
        name: 'caramel-cookie-box-8',
        name1: 'Salted Caramel Cookie Box',
        qty: 8,
        unit: 'pcs',
        price: 420,
        discounts: 6,
        final_price: 395,
        description:
          'Chewy cookies with salted caramel centers, finished with flaky sea salt.',
        key_features:
          '<ul><li>Box of 8 cookies</li><li>Filled with caramel</li><li>Perfect gift option</li></ul>',
        count: 0,
        parent: 'caramel-cookie-box',
      },
    ],
    owner: 'Hearthstone Bakery',
  },
];

const CART_KEY = 'bakery_cart';

const normalizeCart = (cart) =>
  cart
    .filter((entry) => entry?.count > 0)
    .map((entry) => ({ ...entry, count: Math.max(0, entry.count) }));

const getCart = () => {
  if (typeof window === 'undefined') {
    return [];
  }
  try {
    const raw = window.localStorage.getItem(CART_KEY);
    if (!raw) {
      return [];
    }
    return normalizeCart(JSON.parse(raw));
  } catch (error) {
    return [];
  }
};

const setCart = (cart) => {
  if (typeof window === 'undefined') {
    return;
  }
  window.localStorage.setItem(CART_KEY, JSON.stringify(normalizeCart(cart)));
};

const findProduct = (productName) => bakeryProducts.find((product) => product.name === productName);

const findVariant = (product, variantName) =>
  product?.items?.find((item) => item.name === variantName) || product?.items?.[0];

const buildCartEntry = (product, variant, count) => ({
  product: { ...variant },
  count,
  images: product.images,
});

const addToCart = ({ product: productName, event, option }) => {
  const product = findProduct(productName);
  if (!product) {
    return { data: { count: 0 } };
  }
  const variant = findVariant(product, option);
  const cart = getCart();
  const existingIndex = cart.findIndex((entry) => entry.product.name === variant.name);
  const existing = existingIndex >= 0 ? cart[existingIndex] : null;
  const currentCount = existing?.count ?? 0;
  const nextCount = event === 'minus' ? Math.max(currentCount - 1, 0) : currentCount + 1;

  if (existing) {
    cart[existingIndex] = buildCartEntry(product, variant, nextCount);
  } else {
    cart.push(buildCartEntry(product, variant, nextCount));
  }

  setCart(cart);
  return { data: { count: nextCount } };
};

const groupProductsByEvent = () => {
  const eventMap = new Map(bakeryEvents.map((event) => [event.name, event.name1]));
  return bakeryProducts.reduce((accumulator, product) => {
    const label = eventMap.get(product.events) || 'Featured';
    if (!accumulator[label]) {
      accumulator[label] = [];
    }
    accumulator[label].push(product);
    return accumulator;
  }, {});
};

const productsList = ({ category, event }) => {
  if (category) {
    return bakeryProducts.filter((product) => product.category === category);
  }
  if (event) {
    return bakeryProducts.filter((product) => product.events === event);
  }
  return bakeryProducts;
};

const getProductDetails = (name) => bakeryProducts.find((product) => product.name === name);

const cartCount = () => getCart().filter((entry) => entry.count > 0).length;

export const getMockResponse = (method, args = {}) => {
  switch (method) {
    case 'hrs.controllers.api.get_carousel':
      return { images: bakeryCarousel };
    case 'hrs.controllers.api.get_category':
      return bakeryCategories;
    case 'hrs.controllers.api.get_event':
      return bakeryEvents;
    case 'hrs.controllers.api.get_event_by_product':
      return groupProductsByEvent();
    case 'hrs.controllers.api.products_list':
      return productsList(args.data || {});
    case 'hrs.controllers.api.get_product_details':
      return getProductDetails(args.name);
    case 'hrs.controllers.api.add_to_cart':
      return addToCart(args);
    case 'hrs.controllers.api.get_cart':
      return getCart();
    case 'hrs.controllers.api.cart_count':
      return cartCount();
    case 'hrs.controllers.api.get_address':
      return { default_address: true };
    case 'hrs.controllers.api.place_order':
      return { status: 'ok' };
    default:
      return undefined;
  }
};

export { bakeryCarousel, bakeryCategories, bakeryEvents, bakeryProducts };
