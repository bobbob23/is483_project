<template>
  <Banner msg="CAREERS AT TSH" />
  <Button label="< Back" class="mt-2 mx-2"
    style="border-radius: 20%; border: lightgrey; height: 35px; background-color: white; color: black "
    @click="$router.go(-1)" />
  <div class="m-3 px-4">
    <h1 class="m-3">{{ jobData.title }}</h1>
    <hr>
    <form @submit.prevent="submitForm">
      <div class="row">
        <div class="col-3"></div>
        <div class="col">
          <label for="firstname" style="display: block">First Name</label>
          <InputText id="firstname" v-model="fName" style="width: 300px" />
        </div>
        <div class="col">
          <label for="lName" style="display: block"> Last Name</label>
          <InputText v-model="lName" id="lName" style="width: 300px" />
        </div>
        <div class="col-3"></div>
      </div>

      <div class="row">
        <div class="col-3"></div>
        <div class="col">
          <label for="email">Email</label>
          <InputText v-model="email" id="email" style="width: 300px"/>
        </div>
        <div class="col">
          <label for="contact">Contact Number</label>
          <InputText v-model="number" id="number" style="width: 300px"/>
        </div>
        <div class="col-3"></div>
      </div>
      <div class="p-field">
        <Button label="Submit" type="submit" v-model="formValid" @click="submitForm(formValid)" />
        <!--to add in disable submit button if form is not filled up-->
      </div>
    </form>
  </div>
</template>
  
<script>
import InputText from 'primevue/inputtext';
import FileUpload from 'primevue/fileupload';
import Button from 'primevue/button';
import Banner from './Banner.vue'

export default {
  components: {
    Banner
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
      jobData: "",
      job_ID: this.$route.params.job_ID,
      name: "",
      email: "",
      resume: "",
      number: "",
      formValid: true,
    }
  },
  mounted() {
    this.jobData = this.jobs[this.job_ID - 1]
  },
  methods: {
    submitForm(formValid) {
      if (formValid) {
        this.$router.push({
          name: "Success",
        })
      }
    }
  }
}
</script>
<style scoped>
.row{
  padding-top: 10px;
}

label,
InputText {
  display: block;
}
</style scoped>