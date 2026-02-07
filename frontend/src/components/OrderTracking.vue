<template>
    <div class="order-tracking">
      
      
      <div v-for="(item, index) in steps" :key="item.title" class="step">
        <div class="step-indicator">
          <div
            :class="{
              'circle': true,
              'completed': index < currentStep,
              'current': index === currentStep,
              'upcoming': index > currentStep
            }"
          >
            <span v-if="index < currentStep">
                <FeatherIcon name="check" class="w-3" />
            </span>
          </div>
          <div v-if="index < steps.length - 1" class="line"></div>
        </div>
        
        <div class="step-details">
          <p class="step-title">{{ item.title }}</p>
          <p v-if="item.date" class="step-date">{{ item.date }}</p>
          <p v-else class="step-date">{{ item.status }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import FeatherIcon from 'frappe-ui/src/components/FeatherIcon.vue';
  import { computed } from 'vue';

  const props = defineProps({
    orderStatus: { type: String, default: 'Confirm' },
    orderDate: { type: String, default: '' },
    shippingStatus: { type: String, default: 'Pending' },
    shippingDate: { type: String, default: '' },
    deliveryStatus: { type: String, default: 'Pending' },
    deliveryDate: { type: String, default: '' },
  });

  const formatDate = (value) => {
    if (!value) return '';
    const parsed = new Date(value);
    if (Number.isNaN(parsed.getTime())) return '';
    return parsed.toLocaleString();
  };

  const steps = computed(() => ([
    { title: 'Order Confirmed', date: formatDate(props.orderDate), status: props.orderStatus },
    { title: 'Shipped', date: formatDate(props.shippingDate), status: props.shippingStatus },
    { title: 'Delivery', date: formatDate(props.deliveryDate), status: props.deliveryStatus },
  ]));
  
  const currentStep = computed(() => {
    if (props.deliveryStatus === 'Confirm') return 2;
    if (props.shippingStatus === 'Confirm') return 1;
    return 0;
  });
  </script>
  
  <style scoped>
  .order-tracking {
    width: 100%;
    padding: 16px;
    font-family: Arial, sans-serif;
  }

  .step {
    display: flex;
    align-items: flex-start;
    margin-bottom: 10px;
  }
  .step-indicator {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-right: 10px;
  }
  .circle {
    width: 20px;
    height: 20px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    color: #fff;
    background-color: #ccc;
  }
  .completed {
    background-color: #4caf50;
  }
  .current {
    background-color: #ffa500;
  }
  .upcoming {
    background-color: #e0e0e0;
  }
  .line {
    width: 2px;
    height: 60px;
    background-color: #e0e0e0;
  }
  .step-details {
    display: flex;
    flex-direction: column;
  }
  .step-title {
    font-weight: bold;
    font-size: 14px;
  }
  .step-date {
    color: #666;
    font-size: 12px;
  }
  </style>
  
