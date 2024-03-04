<template>
  <div>
    <template v-if="!formValid">
      <div class="p-col-12">
        <Message severity="error">{{ errorMsg }}</Message>
      </div>
    </template>
  </div>
</template>

<script>
import Message from 'primevue/message';

export default {
  props: {
    formValid: {
      type: Boolean,
      required: true
    },
    errorMsg: {
      type: String,
      default: 'Please fill up all required fields!'
    }
  },
  components: {
    Message
  }
}
</script>

<style scoped>
</style>
