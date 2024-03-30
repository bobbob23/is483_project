<template>
    <HRNavBar />
    <div class="container">
        <h3 class="p-5">Welcome Back, Anis</h3>
        <div class="row" style="margin-bottom: 40px;">
            <div class="col chartBox">
                <highcharts class="hc" :options="GPAchartOptions" :constructor-type="'chart'" ref="chart">
                </highcharts>
            </div>
            <div class="col chartBox">
                <highcharts class="hc" :options="SchoolchartOptions" :constructor-type="'chart'" ref="chart">
                </highcharts>
            </div>
        </div>
        <div class="row" style="margin-bottom: 40px; ">
            <div class="col chartBox">
                <highcharts class="hc" :options="CoursechartOptions" :constructor-type="'chart'" ref="chart">
                </highcharts>
            </div>
            <div class="col chartBox">
                <highcharts class="hc" :options="PastSalarychartOptions" :constructor-type="'chart'" ref="chart">
                </highcharts>
            </div>
        </div>
        <div class="row chartBox" style="margin-bottom: 40px;">
            <div>
                <highcharts class="hc" :options="WorkPermitchartOptions" :constructor-type="'chart'" ref="chart">
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
        HRNavBar
    },
    data() {
        return {
            GPAchartOptions: {
                chart: {
                    type: 'pie'
                },
                title: {
                    text: "Candidates split by GPA"
                },
                colors: ["#011B56", "#A5A5A5", "#EB2A27", "#F2C611"],
                series: [
                    {
                        data: [{
                            name: "< 3.0",
                            y: 10
                        },
                        {
                            name: "3.0 - 3.5",
                            y: 20
                        },
                        {
                            name: "3.5 - 4.0",
                            y: 20
                        },
                        {
                            name: "> 4.0",
                            y: 15
                        }
                        ]
                    }
                ]
            },
            SchoolchartOptions: {
                chart: {
                    type: 'pie'
                },
                title: {
                    text: "Candidates split by School"
                },
                colors: ["#011B56", "#A5A5A5", "#EB2A27", "#F2C611"],
                series: [
                    {
                        data: [{
                            name: "SUSS",
                            y: 10
                        },
                        {
                            name: "NTU",
                            y: 20
                        },
                        {
                            name: "SMU",
                            y: 20
                        },
                        {
                            name: "NUS",
                            y: 15
                        }
                        ]
                    }
                ]
            },
            CoursechartOptions: {
                chart: {
                    type: 'pie'
                },
                title: {
                    text: "Candidates split by Courses"
                },
                colors: ["#011B56", "#A5A5A5", "#EB2A27", "#F2C611", "#008000"],
                series: [
                    {
                        data: [{
                            name: "Engineering",
                            y: 10
                        },
                        {
                            name: "Information Systems",
                            y: 10
                        },
                        {
                            name: "Computer Science",
                            y: 8
                        },
                        {
                            name: "Business Management",
                            y: 3
                        },
                        {
                            name: "Accounting",
                            y: 5
                        }
                        ]
                    }
                ]
            },
            PastSalarychartOptions: {
                chart: {
                    type: 'pie'
                },
                title: {
                    text: "Candidates split by Past Salary"
                },
                colors: ["#011B56", "#A5A5A5", "#EB2A27", "#F2C611"],
                series: [
                    {
                        data: [{
                            name: "< $3000",
                            y: 10
                        },
                        {
                            name: "$3000 - $5000",
                            y: 10
                        },
                        {
                            name: "$5000 - $7000",
                            y: 8
                        },
                        {
                            name: "> $7000",
                            y: 3
                        }
                        ]
                    }
                ]
            },
            WorkPermitchartOptions: {
                chart: {
                    type: 'pie'
                },
                title: {
                    text: "Candidates split by Work Permit Status"
                },
                colors: ["#011B56", "#A5A5A5", "#EB2A27"],
                series: [
                    {
                        data: [{
                            name: "Singaporean",
                            y: 15
                        },
                        {
                            name: "Permanent Resident",
                            y: 15
                        },
                        {
                            name: "Work/Study Visa",
                            y: 5
                        }
                        ]
                    }
                ]
            }
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