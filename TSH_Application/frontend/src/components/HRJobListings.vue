<template>
    <HRNavBar />
    <div class="row flex" style="background-color: rgb(230, 230, 230);">
        <div class="col-1">
            <Button label="< Back" class="my-2 mx-2 flex-start"
                style="border-radius: 20%; border: rgb(230, 230, 230); height: 35px; background-color: rgb(230, 230, 230); color: black "
                @click="$router.go(-1)" />
        </div>
    </div>
    <div class="container mt-4">
        <div class="row">
            <div class="col-2"></div>
            <h3 class="col-2">Job Listings ({{ jobCount }})</h3>
            <div class="col-4"></div>
            <Button class="col-1" label="+ New Job" style="background-color: darkblue;" @click="$router.push('/hr_createjob')"/>
            <div class="col-2"></div>
        </div>

        <div class="row mt-3" v-for="(job, index) in jobs" :key="job.title">
            <!-- <div class="col-1">
            </div> -->
            <div class="col-10">
                <Card style="width: 100%; margin-left: 13%; margin-bottom: 2%; margin-right: 3%"
                    @mouseenter="hover[index] = true" @mouseleave="hover[index] = false" class="div"
                    :class="{ 'div-hover': hover[index] }" @click="goToApplicantsPage(job.job_ID, job.title)">
                    <template #title>{{ job.title }}</template>
                    <template #content>
                        <div class="content-container" style="display: flex;">
                            <div class="d-flex">
                                <div class="mt-4 w-100">
                                    <p style="color: rgb(91, 91, 91); margin-right: 0;">Application Deadline: {{ job.closing_date.slice(6,16)}}</p>
                                </div>
                                <div class="d-flex" style="margin-left: 30%">
                                    <div class="text-center mx-3">
                                        <h3>{{ job.unprocessed_num }}</h3>
                                        <span class="d-block">Unprocessed</span>
                                    </div>
                                    <div class="text-center mx-3">
                                        <h3>{{ job.shortlisted_num }}</h3>
                                        <span class="d-block">Shortlist</span>
                                    </div>
                                    <div class="text-center mx-3">
                                        <h3> {{ job.interview_num }}</h3>
                                        <span class="d-block">Interview</span>
                                    </div>
                                </div>
                            </div>
                            <div style="display:block; flex: 1;" class="ml-auto">
                                <Button label="Edit" style="display: block; margin: -3% auto 3%; background-color: white; 
                                    color: darkblue; border: darkblue 1px solid; width: 40%;" />
                                <Button label="Deactivate" style="display: block; margin: 0 auto; background-color: white; 
                                    color: darkblue; border: darkblue 1px solid; width: 40%;" />
                            </div>
                        </div>
                    </template>
                </Card>
            </div>
            <hr>
        </div>


    </div>
</template>
<script>
import HRNavBar from "./HRNavBar.vue"
import { getAllJobListing } from '@/api/api';
import axios from "axios";

export default {
    components: {
        HRNavBar
    },
    data() {
        return {
            jobs: "",
            jobCount: "",
            hover: "",
        }
    },
    mounted() {
        axios.get(getAllJobListing)
            .then((response) => {
                console.log(response.data.data)
                this.jobs = response.data.data
                this.hover = new Array(response.data.data.length).fill(false);
                this.jobCount = this.jobs.length
            })
    },
    methods: {
        goToApplicantsPage(job_ID, job_title) {
            this.$router.push({
                name: "HRJobApplicants",
                params: {
                    job_ID: job_ID,
                    job_title: job_title
                }
            })
        }
    },
    methods: {
        newJobPage() {
            this.$router.push('/CreateJobPage.vue');
        }
    }
}


</script>

<style>
.div-hover {
    background-color: lightgrey;
}

Button {
    border-radius: 30px;
}
</style>