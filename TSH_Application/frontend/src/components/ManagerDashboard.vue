<template>
    <HRNavBar />
    <div v-if="!isLoading" class="container">
        <h3 class="p-5">Welcome Back, Manager</h3>
        <!-- Row 1 -->
        <div class="row" style="margin-bottom: 40px;">
            <div class="col chartBox">
                <highcharts class="hc" :options="funnelChartOptions" style="width: 100%;" />
            </div>
            <div class="col chartBox">
                <pie-chart :data="workPermitData" title="Work Permit" />
            </div>
        </div>
        <!-- Row 2 -->
        <div class="row" style="margin-bottom: 40px;">
            <div class="col chartBox">
                <histogram-chart :data="GPAhistogramData" :bins="GPAhistorgramBins" title="GPA" x-axis-title="GPA Score"
                    y-axis-title="Number of Applicants" seriesName="GPA Distribution" />
            </div>
            <div class="col chartBox">
                <bar-chart :data="schoolData" title="School" x-axis-title="School" y-axis-title="Number of Applicants"
                    seriesName="School Distribution" />
            </div>
        </div>
        <!-- Row 3 -->
        <div class="row" style="margin-bottom: 40px;">
            <div class="col chartBox">
                <bar-chart :data="courseData" title="Course of Study" x-axis-title="Course of Study"
                    y-axis-title="Number of Applicants" seriesName="Course of Study Distribution" />
            </div>
            <div class="col chartBox">
                <box-plot-chart :data="pastSalaryData" title="Past Salary" x-axis-title="" y-axis-title="Salary ($)"
                    seriesName="Salary" />
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import HRNavBar from "./HRNavBar.vue"
import Highcharts from 'highcharts'
import loadFunnel from 'highcharts/modules/funnel';
import HistogramChart from '../dashboard/HistogramChart.vue';
import BarChart from '../dashboard/BarChart.vue';
import BoxPlotChart from '../dashboard/BoxPlotChart.vue';
import PieChart from '../dashboard/PieChart.vue';
import { getDashboardDepartment, getDashboardJobID } from "@/api/api.js";

loadFunnel(Highcharts);

export default {
    components: {
        HRNavBar,
        HistogramChart,
        BarChart,
        BoxPlotChart,
        PieChart
    },
    data() {
        return {
            isLoading: true,
            apiData: null,
            // DEPARTMENT IS HARDCODED FOR NOW!
            department: 'technology',
            colors: ["#C2272D", "#F8931F", "#E6E600", "#009245", "#0193D9", "#0C04ED", "#612F90"],
            funnelChartOptions: {
                chart: {
                    type: 'funnel'
                },
                title: {
                    text: "Candidate Pipeline Chart"
                },
                subtitle: {
                    text: 'Provides an overview of the number of candidates at each stage of the hiring process for positions'
                },
                plotOptions: {
                    series: {
                        dataLabels: {
                            enabled: true,
                            format: '<b>{point.name}</b> \n ({point.y:,.0f})',
                            softConnector: true
                        },
                        center: ['50%', '60%'],
                        neckWidth: '20%',
                        neckHeight: '25%',
                        width: '70%',
                        height: '80%'
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
                }]
            },
            GPAhistorgramBins: ['< 3.0', '< 3.5', '< 4.0', '> 4.0']
        };
    },
    computed: {
        GPAhistogramData() {
            return [
                {
                    category: '< 3.5',
                    value: {
                        y: this.apiData.GPA['< 3.5'],
                        color: this.colors[0]
                    }
                },
                {
                    category: '< 3.0',
                    value: {
                        y: this.apiData.GPA['< 3.0'],
                        color: this.colors[1]
                    }
                },
                {
                    category: '< 4.0',
                    value: {
                        y: this.apiData.GPA['< 4.0'],
                        color: this.colors[2]
                    }
                },
                {
                    category: '> 4.0',
                    value: {
                        y: this.apiData.GPA['> 4.0'],
                        color: this.colors[3]
                    }
                }
            ];
        },
        schoolData() {
            const returnList = []
            const nameList = Object.keys(this.apiData.school)
            returnList.push(nameList)

            const numList = []
            for (let i = 0; i < nameList.length; i++) {
                var colorNum = i
                if (i > 6) {
                    colorNum = Math.floor(Math.random() * 4);
                }
                const schoolArr = {
                    y: this.apiData.school[nameList[i]],
                    color: this.colors[colorNum]
                }
                numList.push(schoolArr)
            }
            returnList.push(numList)
            return returnList
        },
        courseData() {
            const returnList = []
            const nameList = Object.keys(this.apiData.courses)
            returnList.push(nameList)

            const numList = []
            for (let i = 0; i < nameList.length; i++) {
                var colorNum = i
                if (i > 6) {
                    colorNum = Math.floor(Math.random() * 4);
                }
                const courseArr = {
                    y: this.apiData.courses[nameList[i]],
                    color: this.colors[colorNum]
                }
                numList.push(courseArr)
            }
            returnList.push(numList)
            return returnList
        },
        pastSalaryData() {
            const returnList = []
            returnList.push(this.department)
            returnList.push(this.apiData.past_salary)
            return returnList
        },
        workPermitData() {
            const returnList = []
            const nameList = Object.keys(this.apiData.work_permit)

            for (let i = 0; i < nameList.length; i++) {
                const courseArr = {
                    name: nameList[i],
                    y: this.apiData.work_permit[nameList[i]]
                }

                returnList.push(courseArr)
            }
            return returnList
        },
    },
    mounted() {
        this.getData();
    },
    methods: {
        getData() {
            axios.get(getDashboardDepartment + this.department.toString())
                .then(response => {
                    this.apiData = response.data.data
                    this.funnelChartOptions.series[0].data = [
                        ['Unprocessed', this.apiData.status['unprocessed']],
                        ['Shortlisted', this.apiData.status['shortlisted']],
                        ['Interviewing', this.apiData.status['interview']],
                        ['Successful', this.apiData.status['hired']]
                    ]
                    this.isLoading = false
                })
                .catch(error => {
                    console.error('Error fetching data!', error);
                });
        }
    }
}
</script>

<style>
.chartBox {
    padding: 1rem;
    border-radius: 5px;
    box-shadow: 1px 1px 1px 1px #888888;
    margin: 0.5rem
}
</style>