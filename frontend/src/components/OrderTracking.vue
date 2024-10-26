<template>
    <div class="order-tracking">
      
      
      <div v-for="(item, index) in steps" :key="index" class="step">
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
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import FeatherIcon from 'frappe-ui/src/components/FeatherIcon.vue';
import { ref } from 'vue';
  
  const steps = ref([
    { title: 'Order Confirmed', date: 'Your Order has been placed, Sat 26th Oct' },
    { title: 'Shipped', date: 'Expected by Oct 30' },
    { title: 'Delivery', date: 'Nov 03 by 11 PM' },
  ]);
  
  const currentStep = ref(1); // Adjust this to simulate progress
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
  