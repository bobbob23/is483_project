<template>
    <div class="flex justify-content-center">
        <Button label="Edit" style="display: block; margin: 0 auto; background-color: white; 
                                    color: darkblue; border: darkblue 1px solid; width: 80%;"
            @click="visible = true" />
        <Dialog v-model:visible="visible" modal header="Edit Job Listing" :style="{ width: '25rem' }">
            <div class="row">
                <div class="col flex" style="display: flex; flex-direction: column;">
                    <label for="name" style="font-size:small;">Job Listing Name</label>
                    <InputText id="name" class="flex-end" autocomplete="off" style="width: 100%;"
                        v-model="jobListingName" />
                </div>
                <div class="col flex" style="display: flex; flex-direction: column;">
                    <label for="location" style="font-size:small;">Location</label>
                    <Dropdown v-model="location" :options="locationList" id="location" />
                </div>
            </div>

            <div class="row">
                <div class="col mt-2">
                    <label for="startDate" style="font-size:small;">Opening Date</label>
                    <Calendar v-model="startDate" dateFormat="D, dd M yy" />
                </div>
                <div class="col mt-2">
                    <label for="closeDate" style="font-size:small;">Closing Date</label>
                    <Calendar v-model="closeDate" dateFormat="D, dd M yy" />
                </div>
            </div>

            <div class="flex row">
                <div class="col mt-2" style="display: flex; flex-direction: column;">
                    <label for="type" style="font-size:small;">Job Type</label>
                    <Dropdown v-model="type" :options="typeList" id="type" />
                </div>
                <div class="col mt-2" style="display: flex; flex-direction: column;">
                    <label for="department" style="font-size:small;">Department</label>
                    <Dropdown v-model="department" :options="departmentList" id="department" />
                </div>
            </div>

            <div class="flex mt-3" style="display: flex; flex-direction: column;">
                <label for="requirement" style="font-size:small;">Job Requirements</label>
                <Textarea id="requirement" class="flex-auto" autocomplete="off" v-model="requirements"
                    style="height: 150px" />
            </div>

            <div class="flex mt-3" style="display: flex; flex-direction: column;">
                <label for="description" style="font-size:small;">Job Description</label>
                <Textarea id="description" class="flex-auto" autocomplete="off" v-model="description"
                    style="height: 150px" />
            </div>

            <div class="flex justify-content-center mt-2" style="text-align: center;">
                <Button type="button" label="Cancel" severity="secondary" @click="visible = false" link></Button>
                <Button type="button" label="Save" @click="editJobListing()"></Button>
            </div>
        </Dialog>
    </div>
</template>

<script>
import Dialog from 'primevue/dialog';
import { getJobListing, editJobListing } from '@/api/api';
import axios from 'axios';

export default {
    props: {
        job_ID: Number,
    },
    data() {
        return {
            visible: false,
            typeList: ["Internship", "Full-Time"],
            departmentList: ["Engineering", "Technology", "Management"],
            locationList: ["Singapore", "Malaysia"],
            jobListingName: "",
            description: "",
            requirements: "",
            startDate: "",
            closeDate: "",
            type: "",
            department: "",
            job: "",
            location: "",
        };
    },
    watch: {
        visible(newVal) {
            if (newVal) {
                axios.get(`${getJobListing}/${this.job_ID}`)
                    .then((response) => {
                        console.log(response.data.data)
                        this.job = response.data.data
                        this.jobListingName = response.data.data.title
                        this.description = response.data.data.description
                        this.requirements = response.data.data.requirement
                        this.startDate = response.data.data.opening_date
                        this.closeDate = response.data.data.closing_date
                        this.type = response.data.data.type
                        this.department = response.data.data.department
                        this.location = response.data.data.location
                    })
            }
        }

    },
    methods: {
        editJobListing() {
            console.log(this.job_ID)
            axios.put(`${editJobListing}/${this.job_ID}`, {
                title: this.jobListingName,
                description: this.description,
                requirement: this.requirements,
                location: this.location,
                type: this.type,
                department: this.department,
                closing_date: new Date(this.closeDate),
                opening_date: new Date(this.startDate),
                job_status: this.job.job_status,
                hiring_manager: this.job.hiring_manager,
                salary: this.job.salary,
                work_permit: this.job.work_permit
            }).then((response) => {
                console.log(response)
                this.visible = false
            })

        },
    },
};

</script>