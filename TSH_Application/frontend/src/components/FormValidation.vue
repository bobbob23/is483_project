<template>
  <div class="p-col-12" v-if="formValid == false">
    <Message v-model="error" severity="error">{{ errorMsg }}</Message>
  </div>
</template>

<script>
import Message from 'primevue/message';

export default {
  props: {
    formValid: Boolean,
    errorMsg: String,
  },
}
</script>

<style>
.p-message .p-message-wrapper {
    padding: 0.25rem 0.5rem; 
}
</style>
