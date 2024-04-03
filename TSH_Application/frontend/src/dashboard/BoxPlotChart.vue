<template>
    <div ref="chart"></div>
</template>

<script>
import Highcharts from 'highcharts';
import HighchartsMore from 'highcharts/highcharts-more';

HighchartsMore(Highcharts);

export default {
    props: {
        data: {
            type: Array,
            required: true
        },
        title: {
            type: String,
            default: 'Box Plot'
        },
        xAxisTitle: {
            type: String,
            default: 'Bins'
        },
        yAxisTitle: {
            type: String,
            default: 'Frequency'
        },
        seriesName: {
            type: String,
            default: 'Distribution'
        }
    },
    mounted() {
        this.renderChart();
    },
    methods: {
        renderChart() {
            const dataArr = this.data[1];
            var department = this.data[0];
            var header = this.title;
            if (department != undefined){
                department = department.charAt(0).toUpperCase() + department.slice(1);
                header += " (" + department + ")"
            }

            Highcharts.chart(this.$refs.chart, {
                chart: {
                    type: 'boxplot'
                },
                title: {
                    text: header
                },
                xAxis: {
                    labels:{
                        enabled: false
                    }
                },
                yAxis: {
                    title: {
                        text: this.yAxisTitle
                    }
                },
                plotOptions: {
                    boxplot: {
                        fillColor: '#F0F0E0',
                        lineWidth: 3,
                        medianColor: '#0C5DA5',
                        medianDashStyle: 'line',
                        medianWidth: 3,
                        stemColor: '#A63400',
                        stemDashStyle: 'line',
                        stemWidth: 1,
                        whiskerColor: '#000000',
                        whiskerLength: '50%',
                        whiskerWidth: 3
                    }
                },
                legend: {
                    enabled: false
                },
                series: [{
                    name: department,
                    data: [dataArr]
                }]
            })
        }
    }
}
</script>