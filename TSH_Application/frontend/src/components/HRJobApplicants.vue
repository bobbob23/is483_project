<template>
    <div>
        <HRNavBar />
        <div>
            <div class="row flex" style="background-color: rgb(230, 230, 230);">
                <div class="col-1">
                    <Button label="< Back" class="my-2 mx-2 flex-start"
                        style="border-radius: 20%; border: rgb(230, 230, 230); height: 35px; background-color: rgb(230, 230, 230); color: black "
                        @click="$router.go(-1)" />
                </div>
            </div>
            <div class="row mt-4">
                <div class="col-3"></div>
                <div class="col-6">
                    <h3>
                        {{ job_title }} - Applicants
                    </h3>
                    <hr>
                    <Message severity="info">The applicants have been ranked by algorithm. 👩🏽‍💻</Message>
                </div>
                <div class="col-3"></div>
            </div>
            <div class="row mt-3 text-center" v-if="applicants.length == 0">
                <i class="pi pi-spin pi-spinner" style="font-size: 3em;"></i> <!-- Progress spinner -->
            </div>
            <div class="row mt-3" v-for="(applicant, index) of applicants" v-else>
                <div class="col-3"></div>
                <div class="col-6">
                    <Card @click="goToApplicantDetails(applicant.email, job_ID)" @mouseenter="hover[index] = true"
                        @mouseleave="hover[index] = false" :class="{ 'div-hover': hover[index] }">
                        <template #title>
                            <span style="color: rgb(127, 126, 126);">{{ applicant.rank_number }}</span>
                            {{ applicant.first_name }} {{ applicant.last_name }}
                            <span :style="{ backgroundColor: getStatusColor(applicant.applicant_status) }"
                                style="font-size:15px; color: white; border-radius: 5%; margin-left: 0%" class="p-2">{{
                            applicant.applicant_status }}</span>
                        </template>

                        <template #content>
                            <div class="content-container" style="display: flex">
                                <div class="text-container">
                                    <p class="my-0">
                                        School: {{ applicant.school }}
                                    </p>
                                    <p class="mb-0 text-secondary secondary">
                                        Contact Number: {{ applicant.phone_number }}
                                    </p>
                                    <p class="mb-0 text-secondary secondary">
                                        Email: {{ applicant.email }}
                                    </p>
                                    <p class="mb-0 text-secondary secondary">
                                        Graduation: {{ applicant.grad_month.slice(8, 16) }}
                                    </p>
                                </div>
                            </div>
                        </template>
                    </Card>
                    <div style="display: block; flex: 1; margin-left: 45%; " :key="applicant">
                        <Button label="Shortlist" style="display: block; margin: -40% auto 3%; background-color: white; 
                color: darkblue; border: darkblue 1px solid; width: 90%; border-radius: 100px;" :disabled="applicant.applicant_status == 'Shortlisted'"
                            @click="showDialog('Shortlisted', applicant)" />
                        <Button label="Reject" style="display: block; margin: 0 auto; background-color: white; 
                color: darkblue; border: darkblue 1px solid; width: 90%; border-radius: 100px;" :disabled="applicant.applicant_status == 'Reject'"
                            @click="showDialog('Reject', applicant)" />
                        <Button label="Invite for Interview" style="display: block; margin: 3% auto 3%; background-color: white; 
                color: darkblue; border: darkblue 1px solid; width: 90%; border-radius: 100px;" :disabled="applicant.applicant_status == 'Interview'"
                            @click="showDialog('Interview', applicant)" />
                    </div>
                    <Dialog v-model:visible="openDialog" modal :style="{ width: '25rem' }">

                        <template v-if="status === 'Shortlisted'">
                            <h4 class="text-center">Shortlist Applicant</h4>
                            <p class="text-center">Are you sure that you would like to shortlist <strong>{{
                            applicantSelected.first_name }} {{ applicantSelected.last_name }}</strong> for <strong> {{ job_title}} </strong> role? </p>
                        </template>

                        <template v-else-if="status === 'Reject'">
                            <h4 class="text-center">Reject Applicant</h4>
                            <p class="text-center">Are you sure that you would like to reject {{
                            applicantSelected.first_name }} {{ applicantSelected.last_name }} for <strong> {{ job_title}} </strong>
                                role? </p>
                        </template>

                        <template v-else-if="status === 'Interview'">
                            <h4 class="text-center">Invite Applicant for Interview</h4>
                            <p class="text-center">Are you sure that you would like to invite 
                                <strong> {{ applicantSelected.first_name }} {{ applicantSelected.last_name }} </strong> for an interview for
                                <strong> {{ job_title}} </strong> role? </p>
                        </template>
                        <div class="text-center">
                            <Button style="margin-right: 5%" label="Cancel" @click="openDialog = false" link />
                            <Button style="border-radius: 20px; background-color: darkblue; border: darkblue"
                                label="Yes" @click="changeStatus(applicantSelected.email, job_ID, status)" />
                        </div>
                    </Dialog>
                </div>
                <div class="col-1"></div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios"
import HRNavBar from "./HRNavBar.vue"
import { getAllApplicantByJobID, editApplicantStatus } from "@/api/api.js"
import Card from "primevue/card"
import Button from 'primevue/button'
import Dialog from "primevue/dialog"


export default {
    components: {
        HRNavBar
    },
    data() {
        return {
            job_ID: this.$route.params.job_ID,
            job_title: this.$route.params.job_title,
            applicants: [],
            hover: "",
            openDialog: false,
            applicantSelected: "",
            status: "",
        }
    },
    mounted() {
        this.getApplicants()
    },
    methods: {
        getApplicants() {
            axios.get(`${getAllApplicantByJobID}/${this.job_ID}`)
                .then((response => {
                    console.log(this.job_ID)
                    console.log(response.data.data)
                    this.applicants = response.data.data
                    this.hover = new Array(response.data.data.length).fill(false);
                }))
        },
        changeStatus(email, job_ID, status) {
            axios.put(`${editApplicantStatus}/${email}/${job_ID}/${status}`)
                .then((response) => {
                    this.$router.go()
                })
        },
        goToApplicantDetails(email, job_id) {
            this.$router.push({
                name: "ViewApplicant",
                params: {
                    job_ID: job_id,
                    email: email
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
        showDialog(status, applicant) {
            this.openDialog = true
            this.status = status
            this.applicantSelected = applicant
        },
    }
}

</script>

<style>
.div-hover {
    background-color: lightgrey;
}
.p-message .p-message-wrapper {
    padding: 0.25rem 0.5rem; 
}
</style>