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
        <div class="row mt-3" v-for="(applicant, index) of applicants">
            <div class="col-3"></div>
            <div class="col-6">
                <Card>
                    <template #title>
                        {{ applicant.rank_number }} {{ applicant.first_name }} {{ applicant.last_name }}
                    </template>
                    <template #content>
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
                            Graduation: {{ applicant.grad_month }}
                        </p>
                    </template>
                </Card>
            </div>
            <div class="col-3"></div>
        </div>
    </div>
</template>
<script>
import axios from "axios"
import HRNavBar from "./HRNavBar.vue"
import { getAllApplicantByJobID } from "@/api/api.js"
import Card from "primevue/card"

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
        }
    }
}

</script>