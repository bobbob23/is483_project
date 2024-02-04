<script>
import Toolbar from 'primevue/toolbar';
import Button from 'primevue/button'
export default {
    data() {
        return {
            jobs: [],
            searchItem: ""
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
    <Toolbar>
        <template #center>
            <div class="card flex flex-wrap justify-content-center gap-2">
                <span class="p-input-icon-left">
                    <i class="pi pi-search" style="color:grey, "/>
                    <InputText v-model="searchItem" placeholder="Search by keyword" style="border-radius: 50px; width: 500px"/>
                </span>
                <span>
                    <Button label="Search" style="margin-left: 20px; border-radius: 50px; background-color: darkblue" />
                </span>
            </div>
        </template>
    </Toolbar>
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