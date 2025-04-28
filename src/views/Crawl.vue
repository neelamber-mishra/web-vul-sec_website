<template>
  <div>
    <h1>Crawl Directories</h1>
    <form @submit.prevent="submitForm">
      <input v-model="url" type="text" placeholder="Enter URL" required />
      <button type="submit">Crawl</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";

const url = ref("");

const submitForm = () => {
  console.log("Crawling:", url.value);
};
</script>
