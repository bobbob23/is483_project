<template>
    <div>
      <h1>Apply for {{ job.title }}</h1>
      <form @submit.prevent="submitForm">
        <div class="p-field">
          <label for="name">Name</label>
          <InputText v-model="formData.name" id="name" :class="{'p-invalid': formErrors.name}" />
          <small class="p-error" v-if="formErrors.name">Name is required</small>
        </div>
        <div class="p-field">
          <label for="email">Email</label>
          <InputText v-model="formData.email" id="email" :class="{'p-invalid': formErrors.email}" />
          <small class="p-error" v-if="formErrors.email">Email is required</small>
        </div>
        <div class="p-field">
          <label for="resume">Resume</label>
          <FileUpload mode="basic" v-model="formData.resume" id="resume" :class="{'p-invalid': formErrors.resume}" />
          <small class="p-error" v-if="formErrors.resume">Resume is required</small>
        </div>
        <div class="p-field">
          <Button label="Submit" type="submit" :disabled="!isFormValid" />
        </div>
      </form>
    </div>
  </template>
  
  <script>
  import { ref, reactive } from 'vue';
  import { InputText } from 'primevue/inputtext';
  import { FileUpload } from 'primevue/fileupload';
  import { Button } from 'primevue/button';
  
  export default {
    name: 'ApplyForm',
    components: {
      InputText,
      FileUpload,
      Button
    },
    setup() {
      const job = ref({
        title: 'Software Engineer'
      });
  
      const formData = reactive({
        name: '',
        email: '',
        resume: null
      });
  
      const formErrors = reactive({
        name: false,
        email: false,
        resume: false
      });
  
      const validateForm = () => {
        formErrors.name = !formData.name.trim();
        formErrors.email = !formData.email.trim();
        formErrors.resume = !formData.resume;
      };
  
      const isFormValid = () => {
        return !Object.values(formErrors).some(error => error);
      };
  
      const submitForm = () => {
        validateForm();
        if (isFormValid()) {
          // Implement your form submission logic here
          console.log('Form Data:', formData);
          // For example, you could send the form data to an API endpoint
          // After successful submission, navigate to the success page
          router.push('/Success');
        }
      };
  
      return { job, formData, formErrors, isFormValid, submitForm };
    }
  };
  </script>