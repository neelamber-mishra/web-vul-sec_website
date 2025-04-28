<template>
  <div>
    <h1>Brute Force Results</h1>
    <div id="output-container">
      <h2>Execution Summary:</h2>
      <p id="summary">{{ summary }}</p>
    </div>
    <router-link to="/brute-force" class="button">Go Back</router-link>
  </div>
</template>

<script setup>
import { ref } from "vue";
const summary = ref("Summary data will be shown here.");
</script>
