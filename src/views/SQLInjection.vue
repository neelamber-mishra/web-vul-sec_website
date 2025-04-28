<template>
  <div>
    <h1>SQL Injection Tool</h1>
    <form @submit.prevent="submitForm">
      <input
        v-model="url"
        type="text"
        placeholder="Enter Target URL"
        required
      />
      <button type="submit">Execute SQL Injection</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";

const url = ref("");

const submitForm = () => {
  console.log("SQL Injection on:", url.value);
};
</script>
