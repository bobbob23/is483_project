<template>
  <NavBar/>
  <!-- <Banner msg="CAREERS AT TSH" /> -->
  <Button label="< Back" class="mt-2 mx-2"
    style="border-radius: 20%; border: lightgrey; height: 35px; background-color: white; color: black "
    @click="$router.go(-1)" />
  <div class="m-3 px-4">
    <h1 class="m-3">{{ jobData.title }}</h1>
    <p>{{ jobData.description }}</p>
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
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Debitis, dolorum! Velit aspernatur dolor libero fuga
        optio, labore officiis sunt quas molestias cum dolore delectus eius impedit praesentium deserunt doloremque
        nostrum.
      </p>
      <h2 class="mx-3 mt-4">
        Job Requirements
      </h2>
      <p class="mx-3">
      <ul>
        <li>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Necessitatibus asperiores harum, quod dolorem cum
          voluptatum natus. Officia, temporibus. Deserunt minus id officia, mollitia nobis repudiandae reiciendis dolore
          et ut iusto.
        </li>
        <li>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Necessitatibus asperiores harum, quod dolorem cum
          voluptatum natus. Officia, temporibus. Deserunt minus id officia, mollitia nobis repudiandae reiciendis dolore
          et ut iusto.
        </li>
        <li>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Necessitatibus asperiores harum, quod dolorem cum
          voluptatum natus. Officia, temporibus. Deserunt minus id officia, mollitia nobis repudiandae reiciendis dolore
          et ut iusto.
        </li>
      </ul>
      </p>
    </span>
  </div>
</template>
  
<script>
import Button from 'primevue/button';
import Banner from './Banner.vue'
import NavBar from './NavBar.vue'

export default {
  components: {
    Banner,
    NavBar
  },
  data() {
    return {
      jobs: [
        {
          "job_ID": 1,
          "title": "UI/UX",
          "location": "Singapore",
          "type": "Internship",
          "department": "Technology",
          "closing_date": "2015-11-01"
        },
        {
          "job_ID": 2,
          "title": "Software Engineer",
          "location": "Singapore",
          "type": "Entry-Level",
          "department": "Technology",
          "closing_date": "2015-11-15"
        },
        {
          "job_ID": 3,
          "title": "Machining Intern",
          "location": "Singapore",
          "type": "Internship",
          "department": "Engineering",
          "closing_date": "2015-12-01"
        },
        {
          "job_ID": 4,
          "title": "Precision Engineer",
          "location": "Singapore",
          "type": "Entry-Level",
          "department": "Technology",
          "closing_date": "2015-12-15"
        },
        {
          "job_ID": 5,
          "title": "Machining Specialist",
          "location": "Singapore",
          "type": "Internship",
          "department": "Machining",
          "closing_date": "2016-01-01"
        }
      ],
      job_ID: this.$route.params.job_ID,
      jobData: {},
    };
  },
  mounted() {
    this.getListingDetails();
  },
  methods: {
    getListingDetails() {
      this.jobData = this.jobs[this.job_ID - 1]
    },
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