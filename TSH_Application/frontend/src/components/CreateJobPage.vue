<template>
    <div>
        <HRNavBar/>
        <div>
            <Button label="< Back" class="mt-2 mx-2"
            style="border-radius: 20%; border: lightgrey; height: 35px; background-color: white; color: black "
            @click="$router.go(-1)" />
        </div>

        <div class="m-3 px-4">
            <h1 class="m-3">New Job</h1>
            <hr>

            <div class="row">
                <div class="col-3"></div>
                <div class="col">
                    <label for="jobTitle" style="display: block">Job Title <span style="color: red;">*</span></label>
                    <InputText id="jobTitle" v-model="jobTitle" style="width: 300px" />
                </div>
                <div class="col">
                    <label for="jobType" style="display: block">Job Type <span style="color: red;">*</span></label>
                    <Dropdown v-model="jobType" :options="jobTypeList" id="jobType" style="width: 300px" />
                </div>
                <div class="col-3"></div>
            </div>

            <div class="row">
                <div class="col-3"></div>
                <div class="col">
                    <label for="jobLocation" style="display: block">Location <span style="color: red;">*</span></label>
                    <Dropdown v-model="jobLocation" :options="jobLocationList" id="jobLocation" style="width: 300px" />
                </div>
                <div class="col">
                    <label for="jobDept" style="display: block">Department <span style="color: red;">*</span></label>
                    <Dropdown v-model="jobDept" :options="jobDeptList" id="jobDept" style="width: 300px" />
                </div>
                <div class="col-3"></div>
            </div>

            <div class="row">
                <div class="col-3"></div>
                <div class="col">
                    <label for="jobAppDead" style="display: block">Application Deadline <span style="color: red;">*</span></label>
                    <Calendar v-model="jobAppDead" showIcon iconDisplay="input" dateFormat="dd/mm/yy" id="jobAppDead" style="width: 300px" />
                </div>
                <div class="col">
                    <label for="jobSalary" style="display: block">Salary ($) <span style="color: red;">*</span></label>
                    <InputText v-model="jobSalary" id="jobSalary" style="width: 300px" />
                </div>
                <div class="col-3"></div>
            </div>

            <div class="row">
                <div class="col-3"></div>
                <div class="col">
                    <label for="jobWorkPermit" style="display: block">Type of Work Permit(s) <span style="color: red;">*</span></label>
                    <MultiSelect v-model="jobWorkPermit" display="chip" :options="jobWorkPermitList" id="jobWorkPermit" style="width: 300px" />
                </div>
                <div class="col">
                    <label for="jobHM" style="display: block">Hiring Manager <span style="color: red;">*</span></label>
                    <InputText v-model="jobHM" id="jobHM" style="width: 300px" />
                </div>
                <div class="col-3"></div>
            </div>

            <div class="row">
                <div class="col-3"></div>
                <div class="col">
                    <label for="jobDesc" style="display: block">Job Description <span style="color: red;">*</span></label>
                    <Textarea v-model="jobDesc" rows="5" id="jobDesc" style="width: 643px;" />
                </div>
                <div class="col-3"></div>
            </div>

            <div class="row">
                <div class="col-3"></div>
                <div class="col">
                    <label for="jobReq" style="display: block">Job Requirements <span style="color: red;">*</span></label>
                    <Textarea v-model="jobReq" rows="5" id="jobReq" style="width: 643px;" />
                </div>
                <div class="col-3"></div>
            </div>
            <br>

            <div class="row">
                <div class="col-4">
            </div>
            <div class="col-2 justify-content-centre">
                <Button label="Cancel" @click="cancelForm"
                 style="border-radius: 50px; background-color: gray; width: 150px" />
            </div>
            <div class="col-2 justify-content-centre">
                <Button label="Confirm" v-model="formValid" @click="submitForm(formValid)" 
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
        return{
            jobTitle: "",
            jobAppDead: "",
            jobSalary: "",
            jobHM: "",
            jobDesc: "",
            jobReq: "",
            jobType: "",
            jobLocation: "",
            jobDept: "",
            jobWorkPermit: "",
            jobTypeList: ["Internship", "Full-Time"],
            jobLocationList: ["Singapore", "Malaysia"],
            jobDeptList: ["Engineering", "Technology", "Management"],
            jobWorkPermitList: ["Singaporean", "Permanent Resident", "Work/Study Visa"],
            opening_date: new Date().toISOString().split('T')[0],
            formValid: true,
        }
    },
    methods: {
        onUpload(event, name) {
        const file = event.target.files[0];
        console.log(name)
        console.log(file)
        this.filesData.append(name, file)
    },
    submitForm(formValid) {
        if (formValid) {
            const formData = {
                title: this.jobTitle,
                location: this.jobLocation,
                type: this.jobType,
                department: this.jobDept,
                opening_date: this.opening_date, 
                closing_date: this.jobAppDead,
                job_status: 'Active', 
                hiring_manager: this.jobHM,
                salary: this.jobSalary,
                job_description: this.jobDesc,
                job_requirement: this.jobReq,
                work_permit: this.jobWorkPermit
            };

            fetch(createJobListing, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData),
            })
            .then(response => {
            if (response.ok) {
                console.log('Form submitted successfully');
                this.$router.push({
                    name: "HRSuccess",
                    params: {
                    job_title: this.jobTitle,
                    opening_date: this.opening_date
                    }
                })
                } else {
                console.error('Failed to submit form');
                }
            })
            .catch(error => {
                console.error('Error submitting form:', error);
            });
        }
    }
    }
}
</script>

<style>
.row {
  padding-top: 10px;
}
</style>


