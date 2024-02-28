<template>
  <div>
    <NavBar />
    <!-- <Banner msg="CAREERS AT TSH" /> -->
    <div v-if="!jobData" class="text-center mt-5">
      <i class="pi pi-spin pi-spinner" style="font-size: 3em;"></i> <!-- Progress spinner -->
    </div>
    <div v-else>
      <Button label="< Back" class="mt-2 mx-2"
        style="border-radius: 20%; border: lightgrey; height: 35px; background-color: white; color: black "
        @click="$router.go(-1)" />
      <div class="m-3 px-4">
        <h1 class="m-3">{{ jobData.title }}</h1>
        <span class="m-3">
          <i class="pi pi-map-marker mx-2"></i>{{ jobData.location }}
        </span>
        <span class="m-3">
          <i class="pi pi-users mx-2"></i>{{ jobData.type }}
        </span>
        <span class="m-3">
          <i class="pi pi-briefcase mx-2"></i>{{ jobData.department }}
        </span>
        <Button label="Apply Now" @click="applyNow(jobData.job_ID)"
          style="border-radius: 50px; background-color: darkblue; margin-left: 700px; padding: 10px 30px" />
        <hr>
        <span>
          <h2 class="mx-3 mt-4">
            Job Description
          </h2>
          <p class="mx-3">
            {{ jobData.description }}
          </p>
          <h2 class="mx-3 mt-4">
            Job Requirements
          </h2>
          <p class="mx-3">
            {{ jobData.requirement }}
          </p>
        </span>
      </div>
    </div>
  </div>
</template>
  
<script>
import Button from 'primevue/button';
import Banner from './Banner.vue'
import NavBar from './NavBar.vue'
import axios from 'axios';
import { getJobListing } from '@/api/api';

export default {
  components: {
    Banner,
    NavBar
  },
  data() {
    return {
      job_ID: this.$route.params.job_ID,
      jobData: "",
    };
  },
  mounted() {
    axios.get(`${getJobListing}/${this.job_ID}`)
      .then((response) => {
        console.log(response.data.data)
        this.jobData = response.data.data
      })
  },
  methods: {
    applyNow(job_ID) {
      this.$router.push({
        name: "ApplyForm",
        params: {
          job_ID: job_ID
        }
      })
    }
  }
};
</script>