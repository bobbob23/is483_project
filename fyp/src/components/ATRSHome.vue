<script>
export default {
    data() {
        return {
            jobs:[]
        };
    },
    mounted() {
        fetch('http://localhost:3000/')
        .then(res => res.json())
        .then(data => this.jobs = data)
    }
}
</script>

<template>
    <h1>Available Jobs</h1>
    <div>
        <ul>
            <li v-for="job in jobs" :key="job.title">
                <strong>{{ job.title }}</strong> - {{ job.location }} - {{ job.type }} - {{ job.department }}
            </li>
        </ul>
    </div>
</template>