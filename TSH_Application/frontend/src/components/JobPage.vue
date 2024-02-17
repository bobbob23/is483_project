<template>
    <div>
      <h1>{{ job.title }}</h1>
      <p>{{ job.description }}</p>
      <Button label="Apply Now" @click="applyNow" />
    </div>
  </template>
  
  <script>
  import { Button } from 'primevue/button';
  // import { ref } from 'vue';
  // import { useRouter } from 'vue-router';
  
  export default {
    // name: 'JobDetails',
    // components: {
    //   Button
    // },
    data() {
      return {
        job: {
          title: 'Software Engineer',
          description: 'We are looking for a skilled software engineer to join our team...'
        }
      };
    },
    // setup() {
    //   const job = ref({
    //     title: 'Software Engineer',
    //     description: 'We are looking for a skilled software engineer to join our team...'
    //   });
  
      // const router = useRouter();
  
      // const applyNow = () => {
      //   router.push('/Job');
      // };
  
      // return { job, applyNow };
    };
  </script>