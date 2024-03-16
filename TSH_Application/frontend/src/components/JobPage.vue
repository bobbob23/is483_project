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
        <div class="job-info flex align-items-center">
          <h1 class="m-3" style="display: inline">{{ jobData.title }}</h1>
          <Button label="Apply with Resume" @click="applyNow(jobData.job_ID)"
            class="resume-button" />
        </div>
        <div class="job-details">
          <div>
            <span class="m-3">
              <i class="pi pi-map-marker mx-2"></i>{{ jobData.location }}
            </span>
            <span class="m-3">
              <i class="pi pi-users mx-2"></i>{{ jobData.type }}
            </span>
            <span class="m-3">
              <i class="pi pi-briefcase mx-2"></i>{{ jobData.department }}
            </span>
          </div>
          <Button label="Apply Manually" @click="applyNow(jobData.job_ID)"
            class="manual-button" />
        </div>
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

<style scoped>
.job-info {
  display: flex;
  justify-content: space-between;
}

.job-details {
  display: flex;
  justify-content: space-between;
}

.resume-button{
  border-radius: 50px;
  padding: 10px 30px;
}

.manual-button{
  border-radius: 50px;
  padding: 10px 43px;
}

.resume-button {
  background-color: whitesmoke;
  color: darkblue;
  border-color: darkblue;
}

.manual-button {
  background-color: darkblue;
  color: white;
}

@media screen and (max-width: 768px) {
  .resume-button,
  .manual-button {
    margin-left: auto;
  }
}

</style scoped>