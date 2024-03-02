<template>
    <HRNavBar />
    <div class="container">
        <h3 class="p-5">Welcome Back, Anis</h3>
        <div class="container text-center" v-if="unprocessed == '' || active == ''">
            <i class="pi pi-spin pi-spinner" style="font-size: 3em;"></i> <!-- Progress spinner -->
        </div>
        <div class="container" v-else>
            <div class="row">
                <div class="col-4">
                    <Card>
                        <template #subtitle>
                            <span style="font-weight: 600;">
                                Active Jobs <i class="pi pi-briefcase" style="height: 100%"></i>
                            </span>
                        </template>
                        <template #content>
                            <h1>{{ active }}</h1>
                        </template>
                        <template #footer>
                            <Button class="w-100"
                                style="border: 0; background-color: #ededed; color: #011B56; font-weight: 600;"
                                label="View More >" />
                        </template>
                    </Card>
                </div>
                <div class="col-4 ">
                    <Card>
                        <template #subtitle>
                            <span style="font-weight: 600;">
                                Unprocessed Applicants <i class="pi pi-users" style="height: 100%"></i>
                            </span>
                        </template>
                        <template #content>
                            <h1>{{ unprocessed }}</h1>
                        </template>
                        <template #footer>
                            <Button class="w-100"
                                style="border: 0; background-color: #ededed; color: #011B56; font-weight: 600;"
                                label="View More >" />
                        </template>
                    </Card>
                </div>
                <div class="col-4">
                    <Card>
                        <template #subtitle>
                            <span style="font-weight: 600;">
                                Scheduled Interviews <i class="pi pi-calendar" style="height: 100%"></i>
                            </span>
                        </template>
                        <template #content>
                            <h1>{{ interview }}</h1>
                        </template>
                        <template #footer>
                            <Button class="w-100"
                                style="border: 0; background-color: #ededed; color: #011B56; font-weight: 600;"
                                label="View More > " />
                        </template>
                    </Card>
                </div>
            </div>
            <div class="row">
                <div class="col-3" style="padding-top: 10%">
                    <h4>Overall Applicant Status</h4>
                    <p>Unprocessed: {{ unprocessed }}</p>
                    <p>Shortlisted: {{ shortlisted }}</p>
                    <p>Interview: {{ interview }}</p>
                </div>
                <div class="col-4 mt-4">
                    <highcharts class="hc" :options="chartOptions" :constructor-type="'chart'" ref="chart">
                    </highcharts>
                </div>
                <div class="col-5 mt-4">
                    <div class="card flex justify-content-center">
                        <h4 class="px-2 pt-2">New Applicants</h4>
                        <VirtualScroller :items="applicants" :itemSize="50" style="height: 350px; width: 100%"
                        class="border-1 surface-border border-round"  >
                            <template v-slot:item="{ item }">
                                <div :class="['flex align-items-center p-2']"
                                    style="height: 50px">
                                    {{ item.fName }} {{ item.lName }}
                                    <p style="color: rgb(130, 129, 129)">{{ item.email }}</p>
                                </div>
                            </template>
                        </VirtualScroller>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>
<script>
import HRNavBar from "./HRNavBar.vue"
import Card from "primevue/card"
import Button from "primevue/button"
import VirtualScroller from 'primevue/virtualscroller';
import Highcharts from 'highcharts'
import exportingInit from 'highcharts/modules/exporting'
import { getAllApplicantStatus, getAllActiveJob, getAllApplicant } from '@/api/api'
import axios from "axios"

exportingInit(Highcharts)

export default {
    components: {
        HRNavBar,
    },
    data() {
        return {
            unprocessed: "",
            interview: "",
            shortlisted: "",
            active: "",
            applicants: [],
            chartOptions: {
                chart: {
                    type: 'pie'
                },
                title: {
                    text: ""
                },
                colors: ["#011B56", "#A5A5A5", "#EB2A27"],
                series: [
                    {
                        data: [{
                            name: "Unprocessed",
                            y: 0
                        }, {
                            name: "Shortlist",
                            y: 0
                        }, {
                            name: "Interview",
                            y: 0
                        }]
                    }
                ]
            }
        }
    },
    mounted() {
        this.getAppStatusCount()
        this.getAllActiveJobs()
        this.getApplicants()
    },
    methods: {
        getAppStatusCount() {
            axios.get(getAllApplicantStatus)
                .then((response) => {
                    this.unprocessed = response.data.unprocessed
                    this.interview = response.data.interview
                    this.shortlisted = response.data.shortlisted

                    // Update the chart data here
                    this.chartOptions.series[0].data = [{
                        name: "Unprocessed",
                        y: this.unprocessed
                    }, {
                        name: "Shortlist",
                        y: this.shortlisted
                    }, {
                        name: "Interview",
                        y: this.interview
                    }]
                })
        },
        getAllActiveJobs() {
            axios.get(getAllActiveJob)
                .then((response) => {
                    this.active = response.data.job_listing_num
                })
        },
        getApplicants(){
            axios.get(getAllApplicant)
                .then((response) => {
                    console.log(response.data.data)
                    this.applicants = response.data.data
                })
        }
    }
}


</script>