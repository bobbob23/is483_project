<template>
  <NavBar/>
  <!-- <Banner msg="CAREERS AT TSH" /> -->
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
            style="background-color: rgba(211, 211, 211, 0); color: darkblue;" @upload="onUpload" :auto="true"
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
            style="background-color: rgba(211, 211, 211, 0); color: darkblue;" @upload="onUpload" :auto="true"
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
            style="background-color: rgba(211, 211, 211, 0); color: darkblue;" @upload="onUpload" :auto="true"
            chooseLabel="Upload" />
        </div>
        <div class="col"></div>
      </div>
      <div class="row">
        <div class="col-3"></div>
        <div class="col">
          <label for="firstname" style="display: block">First Name <span style="color: red;">*</span></label>
          <InputText id="firstname" v-model="fName" style="width: 300px" />
        </div>
        <div class="col">
          <label for="lName" style="display: block"> Last Name <span style="color: red;">*</span></label>
          <InputText v-model="lName" id="lName" style="width: 300px" />
        </div>
        <div class="col-3"></div>
      </div>

      <div class="row">
        <div class="col-3"></div>
        <div class="col">
          <label for="email">Email <span style="color: red;">*</span></label>
          <InputText v-model="email" id="email" style="width: 300px" />
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
          <label for="course">GPA <span style="color: grey;">(Actual / Total) </span><span style="color: red;">*</span></label>
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
          <Button label="Submit" type="submit" v-model="formValid" @click="submitForm(formValid)" style="border-radius: 50px; background-color: darkblue; width: 150px"/>
        </div>
        <div class="col-5">
        </div>
      </div>
      <!--to add in disable submit button if form is not filled up-->
    </form>
  </div>
</template>
  
<script>
import InputText from 'primevue/inputtext';
import FileUpload from 'primevue/fileupload';
import Button from 'primevue/button';
import Banner from './Banner.vue'
import Dropdown from 'primevue/dropdown';
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
      jobData: "",
      job_ID: this.$route.params.job_ID,
      fName: "",
      lName: "",
      email: "",
      resume: "",
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
    this.jobData = this.jobs[this.job_ID - 1]
    this.job_title = this.jobData.title
  },
  methods: {
    submitForm(formValid) {
      if (formValid) {
        this.$router.push({
          name: "Success",
          params: {
            job_title: this.job_title
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