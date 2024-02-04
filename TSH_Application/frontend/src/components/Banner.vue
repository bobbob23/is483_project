<script setup>
defineProps({
  msg: {
    type: String,
    required: true
  }
})
</script>

<template>
  <div class="banner-photo">
    <div class="banner-box">
      <h1>{{ msg }}</h1>
    </div>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  color: whitesmoke;
  font-size: 2.6rem;
  position: relative;
  font-family: 'Inika-Regular'
}

.banner-photo {
  background: url('../assets/tsh-banner.jpg');
  height: 30vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
.banner-box {
  box-sizing: border-box;
  padding: 20px;
  border: 8px solid whitesmoke;
  text-align: center;
  position: absolute
}

</style>
