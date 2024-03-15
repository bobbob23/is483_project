<template>
    <HRNavBar />
    <div class="container">
        <h3 class="p-5">Welcome Back, Manager</h3>
        <div class="d-flex justify-content-center">
            <highcharts class="hc" :options="funnelChartOptions" style="width: 60%">
            </highcharts>
        </div>
    </div>
</template>

<script>
import HRNavBar from "./HRNavBar.vue"
import Highcharts from 'highcharts'
import loadFunnel from 'highcharts/modules/funnel';

loadFunnel(Highcharts);

export default {
    components: {
        HRNavBar
    },
    data() {
        return {
            funnelChartOptions: {
                chart: {
                    type: 'pyramid'
                },
                title: {
                    text: ""
                }, 
                plotOptions: {
                    series: {
                        dataLabels: {
                            enabled: true,
                            format: '<b>{point.name}</b> ({point.y:,.0f})',
                            softConnector: true
                        },
                        // center: ['40%', '60%'],
                        // neckWidth: '30%',
                        // neckHeight: '25%',
                        width: '80%'
                    }
                },
                series: [{
                    name: '',
                    data: [
                        ['Unprocessed', 8000],
                        ['Shortlisted', 4064],
                        ['Interviewing', 1987],
                        ['Successful', 900],
                    ]
                }],
            }
        }
    }

}


</script>