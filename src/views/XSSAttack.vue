<template>
  <div>
    <h1>XSS Attack Tool</h1>
    <form @submit.prevent="submitForm">
      <input
        v-model="url"
        type="text"
        placeholder="Enter Target URL"
        required
      />
      <input
        v-model="payload"
        type="text"
        placeholder="Enter XSS Payload"
        required
      />
      <button type="submit">Execute XSS Attack</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";

const url = ref("");
const payload = ref("");

const submitForm = () => {
  console.log("XSS Attack on:", url.value, "Payload:", payload.value);
};
</script>
