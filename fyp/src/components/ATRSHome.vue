<template>
<h1>Careers at TSH</h1>
<div>
    <ul>
        <li v-for="jobs in jobs" :key="job.title">
            <strong>{{ job.title }}</strong> - {{ job.location }} - {{ job.type }} - {{ job.department }}
        </li>
    </ul>
</div>
</template>

<script>
export default {
    data() {
        return {
            jobs: []
        };
    },
    mounted() {
        this.fetchJobs();
    },
    methods: {
        async fetchJobs(){
            try {
            const response = await fetch('/jobs.json');
            this.jobs = await response.json();
            } catch (error) {
            console.error('Error fetching jobs:', error);
            }
        }
    }
} 
</script>