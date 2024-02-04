<script>
export default {
    data() {
        return {
            jobs:[]
        };
    },
    mounted() {
        fetch('jobs.json')
        .then(res => res.json())
        .then(data => this.jobs = data)
    },
}
</script>

<template>
    <h2 id="header">Available Jobs</h2>
    <div>
    <Card v-for="job in jobs" :key="job.title">
        <template #title>{{ job.title }}</template>
        <template #content>
            <p class="m-0">
                {{ job.location }} - {{ job.type }} - {{ job.department }}
            </p>
        </template>
    </Card>
    </div>
</template>

<style scoped>

#header {
    text-align: center;
    margin: 20px;
}

</style scoped>