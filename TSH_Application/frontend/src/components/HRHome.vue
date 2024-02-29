<template>
    <HRNavBar />
    <div class="container">
        <h3 class="p-5">Welcome Back, Anis</h3>
        <div class="row">
            <div class="col-4">
                <Card>
                    <template #subtitle>
                        <span style="font-weight: 600;">
                            Active Jobs <i class="pi pi-briefcase" style="height: 100%"></i>
                        </span>
                    </template>
                    <template #content>
                        <h1>2</h1>
                    </template>
                    <template #footer>
                        <Button class="w-100" style="border: 0; background-color: #ededed; color: #011B56; font-weight: 600;" label="View More >"/>
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
                        <h1>5</h1>
                    </template>
                    <template #footer>
                        <Button class="w-100" style="border: 0; background-color: #ededed; color: #011B56; font-weight: 600;" label="View More >"/>
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
                        <h1>3</h1> 
                    </template>
                    <template #footer>
                        <Button class="w-100" style="border: 0; background-color: #ededed; color: #011B56; font-weight: 600;" label="View More > "/>
                    </template>
                </Card>
            </div>
        </div>
        <div class="row">
            <div class="col-3" style="padding-top: 10%">
                <h4>Overall Applicant Status</h4>
                <p>Unprocessed: 46</p>
                <p>Shortlisted: 11</p>
                <p>Interview: 4</p>
            </div>
            <div class="col-4 mt-4">
                <highcharts class="hc" :options="chartOptions" :constructor-type="'chart'" ref="chart">
                </highcharts>
            </div>
        </div>
    </div>
</template>
<script>
import HRNavBar from "./HRNavBar.vue"
import Card from "primevue/card"
import Button from "primevue/button"
import Highcharts from 'highcharts'
import exportingInit from 'highcharts/modules/exporting'

exportingInit(Highcharts)

export default {
    components: {
        HRNavBar,
    },
    data() {
        return {
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
                            y: 46
                        },{
                            name: "Shortlist",
                            y: 11
                        },{
                            name: "Interview",
                            y: 4
                        }]
                    }
                ]
            }
        }
    }
}


</script>