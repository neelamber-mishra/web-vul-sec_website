<template>
  <div>
    <h1>Directory Crawl Results</h1>
    <div id="output-container">
      <h2>Summary:</h2>
      <p id="summary">{{ summary }}</p>
      <h2>Links Found:</h2>
      <ul id="links-list">
        <li v-for="(link, index) in links" :key="index">{{ link }}</li>
      </ul>
    </div>
    <router-link to="/crawl" class="button">Go Back</router-link>
  </div>
</template>

<script setup>
import { ref } from "vue";

const summary = ref("Crawling results will be displayed here.");
const links = ref(["example.com/about", "example.com/login"]);
</script>
