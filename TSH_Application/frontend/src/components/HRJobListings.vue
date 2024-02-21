<template>
    <HRNavBar />
    <Button label="< Back" class="mt-2 mx-2"
        style="border-radius: 20%; border: lightgrey; height: 35px; background-color: white; color: black "
        @click="$router.go(-1)" />
    <div class="container">
        <div class="row">
            <div class="col-2"></div>
            <h3 class="col-2">Job Listings ({{ jobCount }})</h3>
            <div class="col-4"></div>
            <Button class="col-1" label="+ New Job" style="background-color: darkblue;" />
            <div class="col-2"></div>
        </div>

        <Card v-for="(job, index) in jobs" :key="job.title"
            style="width: 70%; margin-left: 13%; margin-bottom: 2%; margin-top: 2%" @mouseenter="hover[index] = true"
            @mouseleave="hover[index] = false" class="div" :class="{ 'div-hover': hover[index] }">
            <template #title>{{ job.title }}</template>
            <template #content>
                <div class="row">
                    <div class="col-4">
                        <span style="color: rgb(91, 91, 91); padding-top: 30%;">
                            Application Deadline: {{ job.closing_date }}
                        </span>
                    </div>
                    <div class="col-6">
                    </div>
                    <div class="col-2">
                        <Button label="Edit"
                            style="margin-left: 20%; margin-bottom: 5%; background-color: white; 
                            color: darkblue; border: darkblue 1px solid;" 
                        />
                        <Button label="Deactivate"
                            style="background-color: white; color: darkblue; border: darkblue 1px solid" 
                        />
                    </div>
                </div>
            </template>

        </Card>

    </div>
</template>
<script>
import HRNavBar from "./HRNavBar.vue"
export default {
    components: {
        HRNavBar
    },
    data() {
        return {
            jobs: "",
            jobCount: "",
            hover: "",
        }
    },
    mounted() {
        fetch('jobs.json')
            .then(res => res.json())
            .then(data => {
                this.jobs = data;
                this.jobCount = data.length
                this.hover = new Array(data.length).fill(false);

            })
    },
}


</script>

<style>
.div-hover {
    background-color: lightgrey;
}

Button {
    border-radius: 30px;
}
</style>