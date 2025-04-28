<template>
  <div>
    <h1>Brute Force Tool</h1>
    <form @submit.prevent="submitForm">
      <input
        v-model="url"
        type="text"
        placeholder="Enter Target URL"
        required
      />
      <input
        v-model="username"
        type="text"
        placeholder="Enter Username"
        required
      />
      <label>Upload Password File:</label>
      <input @change="handleFile" type="file" required />
      <button type="submit">Execute Brute Force</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";

const url = ref("");
const username = ref("");
const passwordFile = ref(null);

const handleFile = (event) => {
  passwordFile.value = event.target.files[0];
};

const submitForm = () => {
  console.log({
    url: url.value,
    username: username.value,
    passwordFile: passwordFile.value,
  });
  // Send it to backend
};
</script>
