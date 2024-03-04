<template>
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
            </div>
            <div class="col-3"></div>
        </div>
        <div class="row mt-3 text-center" v-if="applicants == []">
            <i class="pi pi-spin pi-spinner" style="font-size: 3em;"></i> <!-- Progress spinner -->
        </div>  
        <div class="row mt-3" v-for="(applicant, index) of applicants" v-else>
            <div class="col-3"></div>
            <div class="col-6">
                <Card @click="goToApplicantDetails(applicant.email, job_ID)">
                    <template #title>
                        <span style="color: rgb(127, 126, 126);">{{ applicant.rank_number }}</span> {{ applicant.first_name
                        }} {{ applicant.last_name }}
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
                            <div class="mt-5" style="display: block;  flex: 1; margin-left: 40%; ">
                                <Button label="Shortlist" style="display: block; margin: -40% auto 3%; background-color: white; 
                color: darkblue; border: darkblue 1px solid; width: 90%; border-radius: 100px;"
                                    @click="changeStatus(applicant.email, job_ID, 'Shortlisted')" />
                                <Button label="Reject" style="display: block; margin: 0 auto; background-color: white; 
                color: darkblue; border: darkblue 1px solid; width: 90%; border-radius: 100px;"
                                    @click="changeStatus(applicant.email, job_ID, 'Reject')" />
                                <Button label="Invite for Interview" style="display: block; margin: 3% auto 3%; background-color: white; 
                color: darkblue; border: darkblue 1px solid; width: 90%; border-radius: 100px;"
                                    @click="changeStatus(applicant.email, job_ID, 'Interview')" />
                            </div>
                        </div>
                    </template>
                </Card>
            </div>
            <div class="col-1"></div>
            <hr class="mt-3">
        </div>
    </div>
</template>
<script>
import axios from "axios"
import HRNavBar from "./HRNavBar.vue"
import { getAllApplicantByJobID, editApplicantStatus } from "@/api/api.js"
import Card from "primevue/card"
import Button from 'primevue/button';


export default {
    components: {
        HRNavBar
    },
    data() {
        return {
            job_ID: this.$route.params.job_ID,
            job_title: this.$route.params.job_title,
            applicants: [],
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
                }))
        },
        changeStatus(email, job_ID, status) {
            axios.put(`${editApplicantStatus}/${email}/${job_ID}/${status}`)
                .then((response) => {
                    console.log(response)
                    alert(`You have successfully changed the status!`)
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
        }
    }
}

</script>