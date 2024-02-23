<template>
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
      <hr>
      <form @submit.prevent="submitForm">
        <div class="row">
          <div class="col"></div>
          <div class="col">
            <label for="resume">Resume <span style="color: red;">*</span></label>
          </div>
          <div class="col">
            <FileUpload class="flex-end" mode="basic" name="resume" v-model="resume" url="/api/upload"
              accept="application/pdf, application/docx, application/doc" :maxFileSize="1000000"
              style="background-color: rgba(211, 211, 211, 0); color: darkblue;" @upload="onUpload"
              chooseLabel="Upload" />
          </div>
          <div class="col"></div>
        </div>
        <div class="row">
          <div class="col"></div>
          <div class="col">
            <label for="transcript">Transcript <span style="color: red;">*</span></label>
          </div>
          <div class="col">
            <FileUpload class="flex-end" mode="basic" name="resume" v-model="transcript" url="/api/upload"
              accept="application/pdf, application/docx, application/doc" :maxFileSize="1000000"
              style="background-color: rgba(211, 211, 211, 0); color: darkblue;" @upload="onUpload"
              chooseLabel="Upload" />
          </div>
          <div class="col"></div>
        </div>
        <div class="row">
          <div class="col"></div>
          <div class="col">
            <label for="refLetter">Reference Letter</label>
          </div>
          <div class="col">
            <FileUpload class="flex-end" mode="basic" name="refLetter" v-model="refLetter" url="/api/upload"
              accept="application/pdf, application/docx, application/doc" :maxFileSize="1000000"
              style="background-color: rgba(211, 211, 211, 0); color: darkblue;" @upload="onUpload"
              chooseLabel="Upload" />
          </div>
          <div class="col"></div>
        </div>
        <div class="row">
          <div class="col-3"></div>
          <div class="col">
            <label for="firstname" style="display: block">First Name <span style="color: red;">*</span></label>
            <InputText id="firstname" v-model="fName" style="width: 300px"/>
          </div>
          <div class="col">
            <label for="lName" style="display: block"> Last Name <span style="color: red;">*</span></label>
            <InputText v-model="lName" id="lName" style="width: 300px"/>
          </div>
          <div class="col-3"></div>
        </div>

        <div class="row">
          <div class="col-3"></div>
          <div class="col">
            <label for="email">Email <span style="color: red;">*</span></label>
            <InputText v-model="email" id="email" style="width: 300px" :class="{ 'invalid': fNameEmpty }"/>
          </div>
          <div class="col">
            <label for="contact">Contact Number <span style="color: red;">*</span></label>
            <InputText v-model="number" id="number" style="width: 300px" />
          </div>
          <div class="col-3"></div>
        </div>
        <div class="row">
          <div class="col-3"></div>
          <div class="col">
            <label for="school">School <span style="color: red;">*</span></label>
            <InputText v-model="school" id="school" style="width: 300px" />
          </div>
          <div class="col">
            <label for="course">Course of Study <span style="color: red;">*</span></label>
            <InputText v-model="course" id="course" style="width: 300px" />
          </div>
          <div class="col-3"></div>
        </div>
        <div class="row" v-if="jobData.type !== 'Entry-Level'">
          <div class="col-3"></div>
          <div class="col">
            <label for="gradDate">Month of Graduation <span style="color: red;">*</span></label>
            <InputText v-model="gradDate" id="gradMonth" style="width: 300px" />
          </div>
          <div class="col">
            <label for="course">GPA <span style="color: grey;">(Actual / Total) </span><span
                style="color: red;">*</span></label>
            <InputText v-model="gpa" id="gpa" style="width: 300px" />
          </div>
          <div class="col-3"></div>
        </div>
        <div class="row">
          <div class="col-3"></div>
          <div class="col" v-if="jobData.type !== 'Internship'">
            <label for="pastSalary">Past Salary ($) <span style="color: red;">*</span></label>
            <InputText v-model="pastSalary" id="pastSalary" style="width: 300px" />
          </div>
          <div class="col">
            <label for="course">Type of Work Permit <span style="color: red;">*</span></label>
            <Dropdown v-model="workPermit" :options="workPermitList" id="workPermit" style="width: 300px" />
          </div>
          <div class="col-3"></div>
        </div>
        <div class="row">
          <div class="col-5">
          </div>
          <div class="col-2 justify-content-centre">
            <Button label="Submit" type="submit" v-model="formValid" @click="submitForm(formValid)"
              style="border-radius: 50px; background-color: darkblue; width: 150px" />
          </div>
          <div class="col-5">
          </div>
          <div class="row" style="width: 95%" v-if="errorMsg">
            <div class="col-5"></div>
            <div class="col-2">
              <Message severity="error">Warning Message</Message>
            </div>
          </div>
        </div>
        <!--to add in disable submit button if form is not filled up-->
      </form>
    </div>
  </div>
</template>
  
<script>
import InputText from 'primevue/inputtext';
import FileUpload from 'primevue/fileupload';
import Button from 'primevue/button';
import Banner from './Banner.vue'
import Dropdown from 'primevue/dropdown';
import NavBar from './NavBar.vue'
import axios from 'axios'
import Message from 'primevue/message';
import { getJobListing } from '@/api/api';


export default {
  components: {
    Banner,
    NavBar
  },
  data() {
    return {
      jobData: "",
      job_ID: this.$route.params.job_ID,
      errorMsg: "",
      resume: "",
      refLetter: "",
      transcript: "",
      fName: "",
      lName: "",
      email: "",
      number: "",
      school: "",
      course: "",
      gradDate: "",
      gpa: "",
      pastSalary: "",
      workPermit: "",
      workPermitList: ["Singaporean", "Permanent Resident", "Work/Study Visa"],
      formValid: true,
      job_title: "",

    }
  },
  mounted() {
    if (!this.jobData) {
      axios.get(`${getJobListing}/${this.job_ID}`)
        .then((response) => {
          console.log(response.data.data)
          this.jobData = response.data.data
        })
    }
  },
  methods: {
    submitForm(formValid) {
      if (formValid) {
        this.$router.push({
          name: "Success",
          params: {
            job_title: this.jobData.title
          }
        })
      }
    }
  }
}
</script>
<style scoped>
.row {
  padding-top: 10px;
}

label,
InputText {
  display: block;
}
</style scoped>