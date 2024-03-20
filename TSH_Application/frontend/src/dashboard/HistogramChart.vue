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
        bins: {
            type: Array,
            required: true
        },
        title: {
            type: String,
            default: 'Histogram'
        },
        xAxisTitle: {
            type: String,
            default: 'Bins'
        },
        yAxisTitle: {
            type: String,
            default: 'Frequency'
        }
    },
    mounted() {
        this.renderChart();
    },
    methods: {
        renderChart() {
            const frequencies = this.data.map(item => item.value);

            Highcharts.chart(this.$refs.chart, {
                chart: {
                    type: 'column'
                },
                title: {
                    text: this.title
                },
                xAxis: {
                    title: {
                        text: this.xAxisTitle
                    },
                    categories: this.bins
                },
                yAxis: {
                    title: {
                        text: this.yAxisTitle
                    }
                },
                series: [{
                    name: 'Frequency',
                    data: frequencies
                }]
            });
        }
    }
}
</script>
