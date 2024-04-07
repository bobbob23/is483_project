<template>
    <div>
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
            <div class="col-8 mt-1">
                <div class="">
                    <p v-if="status == 'Reject'" class="p-3 mt-2" style="background-color: var(--red-100); color: var(--red-900);border-radius: 10px;">
                        Reason for Rejection: {{ reject_reason }}
                    </p>
                    <h3>{{ fName }} {{ lName }} </h3> 
                    <Dialog  v-model:visible="openDialog" modal :style="{ width: '25rem' }">
                        <h3>Score Details</h3>
                        <p style="margin-bottom: 2%">Education Level: {{ scoreDetails.education_level }}</p>
                        <p style="margin-bottom: 2%">Education Field: {{ scoreDetails.education_field }}</p>
                        <p style="margin-bottom: 2%">Number of Companies: {{ scoreDetails.num_companies_worked }} </p>
                        <p style="margin-bottom: 2%">Total Working Years: {{ scoreDetails.total_working_years }}</p>
                        <p style="margin-bottom: 2%; font-weight: bold">Overall Matching Score: <span style="font-weight: bold">{{ scoreDetails.overall_probability }}%</span> </p>
                    </Dialog>
                    <Button link style="color: blue" class="p-0 mb-2"> <u class="ml-5" @click="openDialog = true">Overall Matching Rate: {{ scoreDetails.overall_probability }} %</u></Button>
                    <p>
                        <span class="text-secondary secondary">
                            <i class="pi pi-file"></i> Resume &nbsp;
                            <i class="pi pi-file"></i>Transcript &nbsp;
                            <span><i class="pi pi-file"></i> Reference Letter</span>
                        </span>
                        &nbsp;
                        <i class="pi pi-download" style="color: darkblue"></i>&nbsp;
                        <Button label='Download all'
                            class="mt-1 p-0" style="color: darkblue" link @click="getFiles()" />
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
                        <h4 class="my-4">Skills</h4>
                        <p class="mb-1" v-for="(skill, index) in skill_list" :key="index" style="font-weight: bold;"> &nbsp {{ skill }}</p>
                        <div class="my-4"></div>
                    </div>
                </div>
            </div>
            <div class="col-2"></div>
        </div>
    </div>
</template>

<script>
import axios from "axios"
import HRNavBar from "./HRNavBar.vue"
import { getApplicantDetails, getApplicantFiles, getScoreDetails } from "@/api/api";
import Button from 'primevue/button';
import Dialog from "primevue/dialog";

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
            status: "",
            number: "",
            school: "",
            course: "",
            openDialog: false,
            scoreDetails: "",
            reject_reason: "",
            gradDate: "",
            gpa: "",
            skill_list:[]
        }
    },
    mounted() {
        this.getApplicantDetails();
        this.readPdf();
        this.getScoreDetails()
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
                    this.status = response.data.data.status
                    this.reject_reason = response.data.data.reject_reason
                    this.course = response.data.data.course_of_study
                    this.gradDate = response.data.data.grad_month.slice(8, 16)
                    this.gpa = response.data.data.GPA
                    this.skill_list = response.data.data.skill
                })
        },
        getFiles() {
            axios.get(`${getApplicantFiles}/${this.email}/${this.job_ID}`)
                .then(response => {                   
                    if(response.data.isApplied == true){
                        alert("Files have been successfully downloaded into applicant_files folder!")
                    } 
                    else {
                        alert("Download Failed!")
                    }
                })
        },
        getStatusColor(status) {
            switch (status) {
                case 'Unprocessed':
                    return '#d3d3d3';
                case 'Shortlisted':
                    return 'grey';
                case 'Interview':
                    return 'darkblue';
                case 'Reject':
                    return '#ff6961';
                default:
                    return 'transparent';
            }
        },
        getScoreDetails(){
            axios.get(`${getScoreDetails}/${this.email}`)
                .then((response) => {
                    console.log(response.data.data)
                    this.scoreDetails = response.data.data
                })
        },
        readPdf() {
            // let pdfReader = new PdfReader()
            // pdfReader.parseFileItems("../backend/applicantFiles/SnapeSeverus_reference_letter.pdf", (err, item) => {
            //     if (err) console.error("error:", err);
            //     else if (!item) console.warn("end of file");
            //     else if (item.text) console.log(item.text);
            // });

        }
    }
}

</script>