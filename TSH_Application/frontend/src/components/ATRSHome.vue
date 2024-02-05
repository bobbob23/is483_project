<template>
    <Toolbar>
        <template #center>
            <div>
                <span class="p-input-icon-left">
                    <i class="pi pi-search" style="color:grey, " />
                    <InputText v-model="searchItem" placeholder="Search by keyword"
                        style="border-radius: 50px; width: 500px" />
                </span>
                <span>
                    <Button label="Search Jobs"
                        style="margin-left: 20px; border-radius: 50px; background-color: darkblue" />
                </span>
            </div>
        </template>
    </Toolbar>

    <div class="row">
        <div class="p-2 col-4"></div>
        <div class="p-2 col-8">
            <h2 id="header" style="padding-left: 50px;">Available Jobs</h2>
            <hr>
        </div>
    </div>

    <div class="container">
        <div v-for="job in jobs" :key="job.title" class="row">
            <div class="p-2 col-4">

            </div>
            <div class="p-2 col-8">
                <Card style="margin: 20px; width: 45rem;">
                    <template #title>{{ job.title }}</template>
                    <template #content>
                        <p class="m-0">
                            {{ job.location }} - {{ job.type }} - {{ job.department }}
                        </p>
                    </template>
                </Card>
            </div>
        </div>
    </div>
</template>

<script>
import Toolbar from 'primevue/toolbar';
import Button from 'primevue/button'
import Card from 'primevue/card';

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

<style scoped>
#header {
    /* text-align: center; */
    margin: 20px;
}
</style scoped>