<template>
    <div>
        <HRNavBar/>
        
        <div>
            <Button label="< Back" class="mt-2 mx-2"
            style="border-radius: 20%; border: lightgrey; height: 35px; background-color: white; color: black "
            @click="$router.go(-1)" />
        </div>
        
        <div>
            <div class="m-3 px-4">
                <h1 class="m-3">{{ formData.title }}</h1>
                <span class="m-3">
                    <i class="pi pi-map-marker mx-2"></i>{{ formData.location }}
                </span>
                <span class="m-3">
                    <i class="pi pi-users mx-2"></i>{{ formData.type }}
                </span>
                <span class="m-3">
                    <i class="pi pi-briefcase mx-2"></i>{{ formData.department }}
                </span>
                <Button label="Apply Now"
                style="border-radius: 50px; background-color: grey; margin-left: 700px; padding: 10px 30px" />
                
                <hr>
                
                <span>
                    <h2 class="mx-3 mt-4">
                        Job Description
                    </h2>
                    <p class="mx-3">
                        {{ formData.job_description }}
                    </p>
                    <h2 class="mx-3 mt-4">
                        Job Requirements
                    </h2>
                    <p class="mx-3">
                        {{ formData.job_requirements }}
                    </p>
                </span>
            </div>
        </div>

        <div class="m-3 px-4">
            <div class="row">
                <div class="col-4">
            </div>
            <div class="col-2 justify-content-centre">
                <Button label="Edit" @click="$router.go(-1)"
                 style="border-radius: 50px; background-color: gray; width: 150px" />
            </div>
            <div class="col-2 justify-content-centre">
                <Button label="Confirm" v-model="formValid"  
                style="border-radius: 50px; background-color: darkblue; width: 150px" />
            </div>
            <div class="col-4"></div>   
          </div>
          <br>
        </div>
        
    </div>
</template>

<script>
import HRNavBar from './HRNavBar.vue';
import axios from "axios";
import { createJobListing } from '@/api/api';

export default {
    components: {
        HRNavBar
    },
    data() {
        return {
            formData: {
                title: "error",
                closing_date: "",
                salary: "",
                hiring_manager: "",
                job_description: "",
                job_requirements: "",
                type: "",
                location: "",
                department: "",
                work_permit: "",
                opening_date: "",
                job_status: "",
            }
        };
    },
    // methods: {
    //     onUpload(event, name) {
    //     const file = event.target.files[0];
    //     console.log(name)
    //     console.log(file)
    //     this.filesData.append(name, file)
    // },
    // submitForm(formValid) {
    //     if (formValid) {
    //         // const formData = {
    //         //     title: this.jobTitle,
    //         //     location: this.jobLocation,
    //         //     type: this.jobType,
    //         //     department: this.jobDept,
    //         //     opening_date: this.opening_date, 
    //         //     closing_date: this.jobAppDead,
    //         //     job_status: 'Active', 
    //         //     hiring_manager: this.jobHM,
    //         //     salary: this.jobSalary,
    //         //     job_description: this.jobDesc,
    //         //     job_requirement: this.jobReq,
    //         //     work_permit: this.jobWorkPermit
    //         // };

    //         fetch(createJobListing, {
    //             method: 'POST',
    //             headers: {
    //                 'Content-Type': 'application/json'
    //             },
    //             body: JSON.stringify(formData),
    //         })
    //         .then(response => {
    //         if (response.ok) {
    //             console.log('Form submitted successfully');
    //             this.$router.push({
    //                 name: "HRSuccess",
    //                 params: {
    //                 job_title: this.jobTitle,
    //                 opening_date: this.opening_date
    //                 }
    //             })
    //             } else {
    //             console.error('Failed to submit form');
    //             }
    //         })
    //         .catch(error => {
    //             console.error('Error submitting form:', error);
    //         });
    //     }
    // }
    // }
}
</script>

<style>
.row {
  padding-top: 10px;
}
</style>