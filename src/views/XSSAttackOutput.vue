<template>
  <div>
    <h1>XSS Attack Results</h1>
    <div id="output-container">
      <h2>Execution Summary:</h2>
      <p id="summary">{{ summary }}</p>
    </div>
    <router-link to="/xss-attack" class="button">Go Back</router-link>
  </div>
</template>

<script setup>
import { ref } from "vue";

// Simulating receiving a summary (you will set it dynamically later)
const summary = ref("XSS Attack results will be displayed here.");
</script>

<style scoped>
</style>
