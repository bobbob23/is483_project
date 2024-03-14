<template>
  <div class="m-2 px-2" v-if="formValid == false">
    <Message v-model="error" severity="error" :closable="false">{{ errorMsg }}</Message>
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
svg.p-icon .p-message-icon{
  width: 2px
}
</style>
