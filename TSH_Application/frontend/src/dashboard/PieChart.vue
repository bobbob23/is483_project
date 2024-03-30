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
            default: 'Pie Chart'
        }
    },
    mounted() {
        this.renderChart();
    },
    methods: {
        renderChart() {
            const dataArr = this.data;

            Highcharts.chart(this.$refs.chart, {
                chart: {
                    type: 'pie'
                },
                title: {
                    text: this.title
                },
                plotOptions: {
                    series: {
                        allowPointSelect: true,
                        cursor: 'pointer',
                        dataLabels: [{
                            enabled: true,
                            distance: 20
                        }, 
                        {
                            enabled: true,
                            distance: -50,
                            format: '{point.percentage:.1f}%',
                            style: {
                                fontSize: '1.5em',
                                textOutline: 'none',
                                opacity: 1
                            },
                            filter: {
                                operator: '>',
                                property: 'percentage',
                                value: 10
                            }
                        }]
                    }
                },
                tooltip: {
                    formatter: function() {
                        return '<b>' + this.key + '</b>: <b>' + this.y + '</b>';
                    }
                },
                series: [
                    {
                        name: 'Percentage',
                        colorByPoint: true,
                        data: dataArr
                    }
                ]
            });
        }
    }
}
</script>
