<template>
    <HRNavBar />
    <div class="container">
        <h3 class="p-5">Welcome Back, Manager</h3>
        
    </div>
</template>

<script>
import HRNavBar from "./HRNavBar.vue"
import Highcharts from 'highcharts'
import exportingInit from 'highcharts/modules/exporting'

exportingInit(Highcharts)

export default {
    components:{
        HRNavBar
    },

}


</script>