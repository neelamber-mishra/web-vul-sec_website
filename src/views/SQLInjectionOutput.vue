<template>
  <div>
    <h1>SQL Injection Results</h1>
    <div id="output-container">
      <h2>Execution Summary:</h2>
      <p id="summary">{{ summary }}</p>
    </div>
    <router-link to="/sql-injection" class="button">Go Back</router-link>
  </div>
</template>

<script setup>
import { ref } from "vue";

const summary = ref("SQL Injection results will be shown here.");
</script>
