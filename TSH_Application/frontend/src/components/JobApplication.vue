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
        <hr>
        <FormValidation :formValid="formValid" :errorMsg="errorMsg" />
        <form @submit.prevent="submitForm">
          <div class="row">
            <div class="col"></div>
            <div class="col">
              <label for="resume">Resume <span style="color: red;">*</span></label>
            </div>
            <div class="col">
              <input type="file" class="flex-end" name="resume"
                accept="application/pdf, application/docx, application/doc" :maxFileSize="1000000"
                style="background-color: rgba(211, 211, 211, 0); color: darkblue;"
                @change="onUpload($event, 'resume')" />
            </div>
            <div class="col"></div>
          </div>
          <div class="row">
            <div class="col"></div>
            <div class="col">
              <label for="transcript">Transcript <span style="color: red;">*</span></label>
            </div>
            <div class="col">
              <input type="file" class="flex-end" mode="basic" name="transcript"
                accept="application/pdf, application/docx, application/doc" :maxFileSize="1000000"
                style="background-color: rgba(211, 211, 211, 0); color: darkblue;"
                @change="onUpload($event, 'transcript')" chooseLabel="Upload" />
            </div>
            <div class="col"></div>
          </div>
          <div class="row">
            <div class="col"></div>
            <div class="col">
              <label for="refLetter">Reference Letter</label>
            </div>
            <div class="col">
              <input type="file" class="flex-end" mode="basic" name="refLetter"
                accept="application/pdf, application/docx, application/doc" :maxFileSize="1000000"
                style="background-color: rgba(211, 211, 211, 0); color: darkblue;"
                @change="onUpload($event, 'reference_letter')" chooseLabel="Upload" />
            </div>
            <div class="col"></div>
          </div>
          <br>
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
              <InputText v-model="email" @input="emailInput()" id="email" style="width: 300px" />
              <small v-if="showEmailError && !validateEmail(email)" style="color: red">Invalid email address</small>
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
          <div class="row" v-if="jobData.type !== 'Full time'">
            <div class="col-3"></div>
            <div class="col">
              <label for="gradDate">Month of Graduation <span style="color: red;">*</span></label>
              <Calendar v-model="gradDate" :minDate="minDate" id="gradMonth" dateFormat="mm/yy" style="width: 300px" />
            </div>
            <div class="col">
              <label for="course">GPA <span style="color: grey;">(Actual / Total) </span><span
                  style="color: red;">*</span></label>
              <InputText v-model="gpa" id="gpa" style="width: 300px" />
            </div>
            <div class="col-3"></div>
          </div>
          <div class="row" v-if="jobData.type == 'Internship'">
            <div class="col-3"></div>
            <div class="col">
              <label for="startDate">Start Date <span style="color: red;">*</span></label>
              <Calendar v-model="startDate" :minDate="minDate" dateFormat="dd/mm/yy" style="width: 300px" />
            </div>
            <div class="col">
              <label for="endDate">End Date <span style="color: red;">*</span></label>
              <Calendar v-model="endDate" :minDate="minDate" dateFormat="dd/mm/yy" style="width: 300px" />
            </div>
            <div class="col-3"></div>
          </div>
          <div class="row">
            <div class="col-3"></div>
            <div class="col" v-if="jobData.type !== 'Internship'">
              <label for="pastSalary">Past Salary ($) <span style="color: red;">*</span></label>
              <InputText v-model="pastSalary" @input="pastSalaryInput" id="pastSalary" style="width: 300px" />
              <small v-if="showPastSalaryError && !validatePositiveSalary(pastSalary)" style="color: red">Past salary
                cannot be negative</small>
            </div>
            <div class="col">
              <label for="course">Type of Work Permit <span style="color: red;">*</span></label>
              <Dropdown v-model="workPermit" :options="workPermitList" id="workPermit" style="width: 300px" />
            </div>
            <div class="col-3">
            </div>
          </div>
          <div class="row">
            <div class="col-5">
            </div>
            <div class="col-2 justify-content-centre">
              <Button label="Submit" @click="submitForm()" name="btnSubmit"
                style="border-radius: 50px; background-color: darkblue; width: 150px" />
            </div>
            <div class="col-5">
            </div>
          </div>
        </form>
      </div>
      <Dialog v-model:visible="loading" modal :pt="{
      root: 'border-none',
      mask: {
        style: 'backdrop-filter: blur(2px)'
      }
    }">
        <template #container>
          <div class="text-center d-flex flex-column justify-content-center align-items-center p-5"
            style="border-radius: 10px; background-color: white;">
            <p>We're currently populating the input fields with information extracted from your resume.</p>
            <p>Kindly allow some time for your details to be filled in.</p>
            <i class="pi pi-spin pi-spinner text-center" style="font-size: 3em;"></i> <!-- Loading spinner -->
          </div>
        </template>
      </Dialog>
    </div>
  </div>
</template>

<script>
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';
import Banner from './Banner.vue'
import Dropdown from 'primevue/dropdown';
import NavBar from './NavBar.vue'
import Dialog from 'primevue/dialog';
import axios from 'axios'
import Message from 'primevue/message';
import { createApplicant, createApplicantFiles, getJobListing, getAutofill, createTempFile } from '@/api/api';
import FormValidation from './FormValidation.vue';


export default {
  components: {
    Banner,
    NavBar,
    FormValidation
  },
  data() {
    return {
      jobData: "",
      job_ID: this.$route.params.job_ID,
      errorMsg: "",
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
      startDate: "",
      endDate: "",
      workPermitList: ["Singaporean", "Permanent Resident", "Work/Study Visa"],
      formValid: "",
      job_title: "",
      filesData: new FormData(),
      minDate: new Date(),
      showEmailError: false,
      showPastSalaryError: false,
      resumeUploaded: false,
      transcriptUploaded: false,
      profile: "",
      loading: false,
      skill: ""
      // tempFile: new FormData(),
      // tempURL: ""
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
    onUpload(event, name) {
      const file = event.target.files[0];
      this.filesData.append(name, file)

      if (name === 'resume') {
        this.resumeUploaded = true;
        const fileFormData = new FormData();
        fileFormData.append('pdf_file', file)
        this.loading = true
        fetch(getAutofill, {
          method: 'POST',
          body: fileFormData
        })
        .then(response => {
            return response.json();
          })
          .then(data => {
            console.log(data.data.profile)
            if (data.data) {
              this.loading = false
              this.profile = data.data.profile
              this.fName = this.profile.basics.first_name
              this.lName = this.profile.basics.last_name
              this.email = this.profile.basics.emails[0]
              this.school = this.profile.educations[0].issuing_organization
              this.number = this.profile.basics.phone_numbers[0]
              this.course = this.profile.educations[0].description
              this.skill = this.profile.basics.skills
              this.$cookies.set("skills", this.profile.basics.skills)
            }
          })
          .catch(error => {
            console.error('Error:', error);
          }).finally(() => {
            this.loading = false; // Ensure loading is always set to false, even if there's an error
          });

      } else if (name === 'transcript') {
        this.transcriptUploaded = true;
      }

      // // 2. upload it
      // if (name == 'resume') {
      //   this.tempFile.append(name, file)
      //   fetch(createTempFile, {
      //     method: 'POST',
      //     body: this.tempFile
      //   }).then((response) => {
      //     console.log(response)
      //   }).catch((error) => {
      //     console.log(error)
      // });
      },
    // ===================================================================================================================================
      // var reader = new FileReader();
      // var encodedFile;
      // reader.readAsDataURL(file);
      // reader.onload = function () {
      //   console.log(reader.result);
      //   encodedFile = reader.result
        
      //   axios.get(`${processResume}/'${encodedFile}'`)
      //   .then((response) => {
      //     console.log("processresume" + response.data)
      //   })
      // }

      // 3. cvparser -- store cvparser result to v-model name


      // 4. store skills in cookies
    isFormValid() {
      if (this.jobData.type === 'Full-Time') {
        this.formValid = this.fName.length !== 0 &&
          this.lName.length !== 0 &&
          this.email.length !== 0 &&
          this.number.length !== 0 &&
          this.school.length !== 0 &&
          this.course.length !== 0 &&
          this.resumeUploaded &&
          this.transcriptUploaded &&
          this.pastSalary.length !== 0 &&
          this.workPermit.length !== 0;
      } else if (this.jobData.type === 'Internship') {
        this.formValid = this.fName.length !== 0 &&
          this.lName.length !== 0 &&
          this.email.length !== 0 &&
          this.number.length !== 0 &&
          this.school.length !== 0 &&
          this.course.length !== 0 &&
          this.gradDate.length !== 0 &&
          this.gpa.length !== 0 &&
          this.workPermit.length !== 0 &&
          this.startDate.length !== 0 &&
          this.endDate.length !== 0 &&
          this.resumeUploaded &&
          this.transcriptUploaded;
      }

      return this.formValid
    },
    submitForm() {
      if (this.isFormValid()) {
        const formData = {
          job_id: this.job_ID,
          fName: this.fName,
          lName: this.lName,
          email: this.email,
          number: this.number,
          school: this.school,
          course: this.course,
          gradDate: this.gradDate,
          gpa: this.gpa,
          pastSalary: this.pastSalary,
          workPermit: this.workPermit,
          startDate: this.startDate,
          endDate: this.endDate,
          skill: this.skill
        }

        fetch(createApplicant, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(formData)
        })
          .then(response => {
            if (response.ok) {
              console.log('Form submitted successfully');
              this.filesData.append('email', this.email)
              this.filesData.append('job_id', this.job_ID)
              this.$router.push({
                name: "Success",
                params: {
                  job_title: this.jobData.title
                }
              })
              // Redirect to success page or perform other actions
              fetch(createApplicantFiles, {
                method: 'POST',
                body: this.filesData
              })
                .then(response => {
                  if (response.ok) {
                    console.log('Files sent successful');
                    // Perform actions after the second request
                  } else {
                    console.error('Failed to send files');
                    // Handle error
                  }
                })
                .catch(error => {
                  console.error('Error sending files:', error);
                  // Handle error
                });

            } else {
              console.error('Failed to submit form');
              // Handle error
            }
          })
          .catch(error => {
            console.error('Error submitting form:', error);
            // Handle error
          });
      } else {
        this.errorMsg = "Please fill up all required fields!"
        console.log(this.errorMsg)
      }
    },
    emailInput() {
      this.showEmailError = this.email.length > 0;
    },
    pastSalaryInput() {
      this.showPastSalaryError = this.pastSalary !== null;
    },
    validateEmail(email) {
      const emailRegex = /\S+@\S+\.\S+/;
      return emailRegex.test(email);
    },
    validatePositiveSalary(salary) {
      return salary >= 0;
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

.invalid {
  border-color: red !important;
}
</style scoped>