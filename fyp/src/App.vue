<script setup>
import TSH_home from '@/components/ATRS_home';
const props = defineProps(['ATRS_home']);
</script>

<template>
  <div>
    <h2>Available Jobs:</h2>
    <ul>
      <li v-for="job in jobs" :key="job.title">
        <strong>{{ job.title }}</strong> - {{ job.location }} | {{ job.type }}
      </li>
    </ul>
  </div>
</template>

<style scoped>
</style>
