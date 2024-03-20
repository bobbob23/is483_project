<template>
    <div ref="chart"></div>
</template>

<script>
import Highcharts from 'highcharts';

export default {
    props: {
        data: {
            type: Array,
            required: true
        },
        title: {
            type: String,
            default: 'Bar Chart'
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
            const dataArr = this.data[1]
            const yArr = this.data[0]

            Highcharts.chart(this.$refs.chart, {
                chart: {
                    type: 'bar'
                },
                title: {
                    text: this.title
                },
                xAxis: {
                    title: {
                        text: this.xAxisTitle
                    },
                    categories: yArr
                },
                yAxis: {
                    title: {
                        text: this.yAxisTitle
                    },
                    allowDecimals: false
                },
                plotOptions: {
                    bar: {
                        borderRadius: '50%',
                        dataLabels:{
                            enabled: true
                        },
                        groupPadding: 0.1
                    }
                },
                tooltip:{
                    formatter: function (){
                        return '<b>'+ this.x + ': ' + this.y + '</b>';
                    }
                },
                series: [{
                    name: this.seriesName,
                    data: dataArr
                }]
            })
        }
    }
}
</script>