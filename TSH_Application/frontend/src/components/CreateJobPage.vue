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

            <FormValidation :formValid="formValid" :errorMsg="errorMsg"/>

            <Dialog v-model:visible="cancelDialog" modal header="Are you sure?" :style="{ width: '25rem' }">
                <span class="p-text-secondary block mb-5">Your changes will not be saved.</span>
                <div class="text-center m-2">
                    <Button type="button" label="Cancel" severity="secondary" @click="cancelJob()"/>
                    <Button type="button" label="Go Back" @click="cancelDialog = false"/>
                </div>
            </Dialog>

            <div class="row">
                <div class="col-3"></div>
                <div class="col">
                    <label for="title" style="display: block">Job Title <span style="color: red;">*</span></label>
                    <InputText id="title" v-model="title" style="width: 300px"/>
                </div>
                <div class="col">
                    <label for="type" style="display: block">Job Type <span style="color: red;">*</span></label>
                    <Dropdown v-model="type" :options="typeList" id="type" style="width: 300px" />
                </div>
                <div class="col-3"></div>
            </div>

            <div class="row">
                <div class="col-3"></div>
                <div class="col">
                    <label for="location" style="display: block">Location <span style="color: red;">*</span></label>
                    <Dropdown v-model="location" :options="locationList" id="location" style="width: 300px" />
                </div>
                <div class="col">
                    <label for="department" style="display: block">Department <span style="color: red;">*</span></label>
                    <Dropdown v-model="department" :options="departmentList" id="department" style="width: 300px" />
                </div>
                <div class="col-3"></div>
            </div>

            <div class="row">
                <div class="col-3"></div>
                <div class="col">
                    <label for="closing_date" style="display: block">Application Deadline <span style="color: red;">*</span></label>
                    <Calendar v-model="closing_date" showIcon iconDisplay="input" dateFormat="dd/mm/yy" id="closing_date" style="width: 300px" />
                </div>
                <div class="col">
                    <label for="salary" style="display: block">Salary ($) <span style="color: red;">*</span></label>
                    <InputText v-model="salary" id="salary" style="width: 300px" />
                </div>
                <div class="col-3"></div>
            </div>

            <div class="row">
                <div class="col-3"></div>
                <div class="col">
                    <label for="work_permit" style="display: block">Type of Work Permit(s) <span style="color: red;">*</span></label>
                    <MultiSelect v-model="work_permit" display="chip" :options="work_permitList" id="work_permit" style="width: 300px" />
                </div>
                <div class="col">
                    <label for="hiring_manager" style="display: block">Hiring Manager <span style="color: red;">*</span></label>
                    <InputText v-model="hiring_manager" id="hiring_manager" style="width: 300px" />
                </div>
                <div class="col-3"></div>
            </div>

            <div class="row">
                <div class="col-3"></div>
                <div class="col">
                    <label for="job_description" style="display: block">Job Description <span style="color: red;">*</span></label>
                    <Textarea v-model="job_description" rows="5" id="job_description" style="width: 643px;">
                    </Textarea>
                </div>
                <div class="col-3"></div>
            </div>

            <div class="row">
                <div class="col-3"></div>
                <div class="col">
                    <label for="job_requirements" style="display: block">Job Requirements <span style="color: red;">*</span></label>
                    <Textarea v-model="job_requirements" rows="5" id="job_requirements" style="width: 643px;" />
                </div>
                <div class="col-3"></div>
            </div>
            <br>

            <div class="row">
                <div class="col-4">
            </div>
            <div class="col-2 justify-content-centre">
                <Button label="Cancel" @click="showCancelDialog"
                 style="border-radius: 50px; background-color: gray; width: 150px" />
            </div>
            <div class="col-2 justify-content-centre">
                <Button label="Preview" v-model="formValid" @click="previewJob" 
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
import FormValidation from './FormValidation.vue';

export default {
    components: {
        HRNavBar,
        FormValidation,
    },
    data() {
        return{
            title: "",
            closing_date: "",
            salary: "",
            hiring_manager: "",
            job_description: "",
            job_requirements: "",
            type: "",
            location: "",
            department: "",
            work_permit: "",
            typeList: ["Internship", "Full-Time"],
            locationList: ["Singapore", "Malaysia"],
            departmentList: ["Engineering", "Technology", "Management"],
            work_permitList: ["Singaporean", "Permanent Resident", "Work/Study Visa"],
            opening_date: new Date().toISOString().split('T')[0],
            formValid: "",
            errorMsg: "",
            cancelDialog: false
        }
    },
    methods: {
        isFormValid() {
            this.formValid =
            this.title.length !== 0 &&
            this.salary.length !== 0 &&
            this.hiring_manager.length !== 0 &&
            this.job_description.length !== 0 &&
            this.job_requirements.length !== 0 &&
            this.type.length !== 0 &&
            this.location.length !== 0 &&
            this.department.length !== 0 &&
            this.work_permit.length !== 0 &&
            this.opening_date.length !== 0 &&
            this.closing_date.length !== 0 

            return this.formValid
        },
        
        showCancelDialog() {
            this.cancelDialog = true
        },

        cancelJob() {
            this.$router.go(-1)
        },

        updateFormData(formData) {
            this.$store.dispatch('updateFormData', formData);
        },

        previewJob() {
            if (this.isFormValid() !== false) {
                const formData = {
                    title: this.title,
                    location: this.location,
                    type: this.type,
                    department: this.department,
                    opening_date: this.opening_date, 
                    closing_date: this.closing_date,
                    job_status: 'Active', 
                    hiring_manager: this.hiring_manager,
                    salary: this.salary,
                    job_description: this.job_description,
                    job_requirement: this.job_requirements,
                    work_permit: this.work_permit
                };

                this.updateFormData(formData);
                console.log(this.$store.state.formData)

                this.$router.push({
                    name: 'PreviewNewJob',
                    params: {
                        jobTitle: this.title
                    }
                })

            } else {
                this.errorMsg = "Please fill up all required fields!"
                console.log(this.errorMsg)
            }
        },
    },
    
}
</script>

<style>
.row {
  padding-top: 10px;
}
</style>


