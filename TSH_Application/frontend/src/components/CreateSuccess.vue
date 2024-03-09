<template>
    <div class="container py-5">
      <lottie-player src="https://lottie.host/5df8f7d5-2580-4b30-927f-79a8da2745dc/rMdBu8tgCh.json" background="#FFFFFF"
        speed="1" style="width: 300px; height: 300px;" direction="1" playMode="normal" autoplay></lottie-player>
      <h3>You have successfully created {{ job_title }}</h3>
      <p style="color: rgb(140, 139, 139)">The job will be posted on {{ opening_date }}</p>
      <Button label="Back to Job Listings" @click="goHome()" style="border-radius: 10%; background-color: darkblue;"/>
    </div>
  </template>
  
  <script>
  import Button from 'primevue/button';
  
  export default {
    data() {
      return {
        job_title: this.$route.params.job_title,
        opening_date: this.$route.params.opening_date
      }
    },
    methods:{
      goHome(){
        this.$router.push({
          name: "HRJobListings"
        })
      }
    }
  };
  </script>
  
  <style scoped>
  .container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    height: 100%; /* Ensure container fills the height of its parent */
  }
  </style>