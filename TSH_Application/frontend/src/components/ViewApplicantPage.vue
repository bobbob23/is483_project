<template>
    <HRNavBar />
    <div class="row flex" style="background-color: rgb(230, 230, 230);">
        <div class="col-1">
            <Button label="< Back" class="my-2 mx-2 flex-start"
                style="border-radius: 20%; border: rgb(230, 230, 230); height: 35px; background-color: rgb(230, 230, 230); color: black "
                @click="$router.go(-1)" />
        </div>
    </div>
    <div v-if="fName == ''" class="text-center mt-5">
        <i class="pi pi-spin pi-spinner" style="font-size: 3em;"></i> <!-- Progress spinner -->
    </div>
    <div class="row" v-else>
        <div class="col-2"></div>
        <div class="col-8 mt-4">
            <div class="">
                <h3>{{ fName }} {{ lName }}</h3>
                <p>
                    <span class="text-secondary secondary">
                        <i class="pi pi-file"></i> Resume &nbsp;
                        <i class="pi pi-file"></i>Transcript &nbsp;
                        <span><i class="pi pi-file"></i> Reference Letter</span>
                    </span>
                    &nbsp;
                    <i class="pi pi-download" style="color: darkblue"></i> <Button label='Download all' class="mt-1 p-0"
                        style="color: darkblue" link />
                </p>
                <hr>
                <div>
                    <h4 class="my-4">Contact Information</h4>
                    <p class="mb-1" style="font-weight: bold;"> &nbsp; First Name: {{ fName }} </p>
                    <p class="mb-1" style="font-weight: bold;"> &nbsp; Last Name: {{ lName }}</p>
                    <p class="mb-1" style="font-weight: bold;"> &nbsp; Email: {{ email }} </p>
                    <p class="mb-1" style="font-weight: bold;"> &nbsp; Contact Number: {{ number }}</p>
                    <h4 class="my-4">Education</h4>
                    <p class="mb-1" style="font-weight: bold;"> &nbsp; School: {{ school }}</p>
                    <p class="mb-1" style="font-weight: bold;"> &nbsp; Course of Study: {{ course }} </p>
                    <p class="mb-1" style="font-weight: bold;"> &nbsp; Month of Graduation: {{ gradDate }}</p>
                    <p class="mb-1" style="font-weight: bold;"> &nbsp; GPA: {{ gpa }}</p>
                </div>
            </div>
        </div>
        <div class="col-2"></div>
    </div>
</template>
<script>
import axios from "axios"
import HRNavBar from "./HRNavBar.vue"
import { getApplicantDetails } from "@/api/api";
import Button from 'primevue/button';

export default {
    components: {
        HRNavBar
    },
    data() {
        return {
            job_ID: this.$route.params.job_ID,
            email: this.$route.params.email,
            res: "",
            name: "",
            fName: "",
            lName: "",
            number: "",
            school: "",
            course: "",
            gradDate: "",
            gpa: ""
        }
    },
    mounted() {
        this.getApplicantDetails();
    },
    methods: {
        getApplicantDetails() {
            axios.get(`${getApplicantDetails}/${this.email}/${this.job_ID}`)
                .then((response) => {
                    console.log(response.data.data)
                    this.fName = response.data.data.first_name
                    this.lName = response.data.data.last_name
                    this.number = response.data.data.phone_number
                    this.school = response.data.data.school
                    this.school = response.data.data.school
                    this.course = response.data.data.course_of_study
                    this.gradDate = response.data.data.grad_month.slice(8, 16)
                    this.gpa = response.data.data.GPA
                })
        }
    }
}

</script>