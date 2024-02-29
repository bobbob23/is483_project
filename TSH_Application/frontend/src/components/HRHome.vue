<template>
    <HRNavBar />
    <div class="container">
        <h3 class="p-5">Welcome Back, Anis</h3>
        <div class="row">
            <div class="col-3" style="padding-top: 10%">
                <h4>Overall Applicant Status</h4>
                <p>Unprocessed: 46</p>
                <p>Shortlisted: 11</p>
                <p>Interview: 4</p>
            </div>
            <div class="col-4">
                <highcharts class="hc" :options="chartOptions" :constructor-type="'chart'" ref="chart">
                </highcharts>
            </div>
        </div>
    </div>
</template>
<script>
import HRNavBar from "./HRNavBar.vue"
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