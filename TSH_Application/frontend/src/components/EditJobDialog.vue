<template>
    <div class="flex justify-content-center">
        <Button label="Edit" style="display: block; margin: 0 auto; background-color: white; 
                                    color: darkblue; border: darkblue 1px solid; width: 80%;"
            @click="visible = true" />
        <Dialog v-model:visible="visible" modal header="Edit Job Listing" :style="{ width: '25rem' }">
            <div class="flex gap-2" style="display: flex; flex-direction: column;">
                <label for="name" style="font-size:small;">Job Listing Name</label>
                <InputText id="name" class="flex-end" autocomplete="off" style="width: 100%;"
                    v-model="jobListingName" />
            </div>

            <!-- <div class="row">
                <div class="col mt-2">
                    <label for="startDate" style="font-size:small;">Opening Date</label>
                    <Calendar v-model="startDate" :minDate="new Date()" dateFormat="dd/mm/yy" />
                </div>
                <div class="col mt-2">
                    <label for="closeDate" style="font-size:small;">Closing Date</label>
                    <Calendar v-model="closeDate" :minDate="new Date()" dateFormat="dd/mm/yy" />
                </div>
            </div> -->

            <div class="flex gap-2 mt-3" style="display: flex; flex-direction: column;">
                <label for="requirement" style="font-size:small;">Job Requirements</label>
                <Textarea id="requirement" class="flex-auto" autocomplete="off" v-model="requirements" />
            </div>

            <div class="flex gap-2 mt-3" style="display: flex; flex-direction: column;">
                <label for="description" style="font-size:small;">Job Description</label>
                <Textarea id="description" class="flex-auto" autocomplete="off" v-model="description" style="height: 200px"/>
            </div>

            <div class="flex justify-content-center mt-5">
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
            jobListingName: "",
            description: "",
            requirements: "",
            startDate: "",
            closeDate: "",
            job: ""
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
                        this.startDate = this.formatDate(response.data.data.opening_date)
                        // this.origStart = response.data.data.opening_date
                        this.closeDate = this.formatDate(response.data.data.closing_date)
                        // this.origClose = response.data.data.closing_date
                    })
            }
        }

    },
    methods: {
        editJobListing() {
            console.log(this.job_ID)
            // if(this.formatDate(this.origClose) == this.closeDate && this.formatDate(this.origStart) == this.startDate){
            //     this.closeDate = this.origClose
            //     this.startDate = this.origStart
            //     console.log(this.origClose)
            //     console.log("end" + this.closeDate)
            //     console.log("start" + this.startDate)
            //     console.log(this.origStart)
            // }
            axios.put(`${editJobListing}/${this.job_ID}`, {
                title: this.jobListingName,
                description: this.description,
                requirement: this.requirements,
                location: this.job.location,
                type: this.job.type,
                department: this.job.department,
                closing_date: this.closing_date,
                opening_date: this.job.opening_date,
                job_status: this.job.job_status,
                hiring_manager: this.job.hiring_manager,
                salary: this.job.salary,
                work_permit: this.job.work_permit
            }).then((response) => {
                console.log(response)
                this.visible = false
            })

        },
        formatDate(dateString) {
            const date = new Date(dateString);
            // Get the day, month, and year
            const day = date.getUTCDate().toString().padStart(2, '0');
            const month = (date.getUTCMonth() + 1).toString().padStart(2, '0');
            const year = date.getUTCFullYear();

            return `${day}/${month}/${year}`;
        },
        parseDateString(formattedDate) {
            const [day, month, year] = formattedDate.split('/');
            const date = new Date(Date.UTC(year, month - 1, day));
            return date.toUTCString();
        }
    }
};

</script>