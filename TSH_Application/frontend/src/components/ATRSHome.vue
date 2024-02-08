<template>
    <Toolbar>
        <template #center>
            <div>
                <span class="p-input-icon-left">
                    <AutoComplete v-model="searchItem" placeholder="Search by keyword"
                        style="border-radius: 100px; width: 200px" :suggestions="jobListingTitles" @complete="search" 
                        @keyup.enter="retrieveListings(searchItem)"
                        />
                </span>
                <span>
                    <Button label="Search Jobs" style="margin-left: 20px; 
                        border-radius: 50px; background-color: darkblue" @click="retrieveListings(searchItem)" />
                </span>
            </div>
        </template>
    </Toolbar>

    <div class="row">
        <div class="mt-4 p-2 col-1">
        </div>
        <div class="mt-4 p-2 col-3">
            <h3>Filters</h3>
        </div>
        <div class="p-2 col-8">
            <h3 id="header" style="padding-left: 50px;">Available Jobs</h3>
            <hr>
        </div>
    </div>

    <div class="container">
        <div class="row">
            <div class="col-3">
                <h4>Experience Level</h4>
                <Listbox class="w-full" v-model="selectedExperience" :options="experienceLevel"
                    @click="reloadListings(selectedExperience, selectedLocation)" />
                <h4 class="mt-3">Location</h4>
                <Listbox class="w-full" v-model="selectedLocation" :options="countries" style="padding: 0px;"
                    @click="reloadListings(selectedExperience, selectedLocation)" />
            </div>
            <div class="col-1">
            </div>
            <div class="col-8">
                <Card v-for="(job, index) in jobs" :key="job.title"
                    style="margin-bottom: 20px; margin-left: -35px; width: 45rem;" @click="viewRoleListing(job)"
                    @mouseenter="hover[index] = true" @mouseleave="hover[index] = false" class="div"
                    :class="{ 'div-hover': hover[index] }">
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
import Button from 'primevue/button';
import Card from 'primevue/card';
import Listbox from 'primevue/listbox'
import AutoComplete from 'primevue/autocomplete'

export default {
    data() {
        return {
            jobs: [], // to be used to populate all listings
            untouchedJobList: [], // original job list that contains all job listings
            jobListingTitles: [], // to be used to populate datalist tag for search bar
            selectedExperience: "",
            experienceLevel: ["Internship", "Entry-Level", "Experienced"],
            selectedLocation: "",
            countries: ["Singapore", "Malaysia"],
            searchItem: "",
            hover: [],
        };
    },
    mounted() {
        fetch('jobs.json')
            .then(res => res.json())
            .then(data => {
                this.jobs = data;
                this.untouchedJobList = data;
                this.hover = new Array(data.length).fill(false);
            })
    },
    methods: {
        viewRoleListing(job) {
            alert(job.title + " job listing")
        },
        reloadListings(selectedExperience, selectedLocation) {
            fetch('jobs.json')
                .then(res => res.json())
                .then(data => {
                    if (!selectedExperience && !selectedLocation) {
                        this.jobs = data;
                    } else if (selectedExperience && selectedLocation) {
                        this.jobs = data.filter(job => {
                            return job.type === selectedExperience && job.location === selectedLocation;
                        });
                    } else if (selectedLocation) {
                        this.jobs = data.filter(job => job.location === selectedLocation);
                    } else {
                        this.jobs = data.filter(job => job.type === selectedExperience);
                    }
                })
        },

        search(event) {
            setTimeout(() => {
                if (!event.query.trim().length) {
                    this.jobListingTitles = [...this.untouchedJobList];
                } else {
                    this.jobListingTitles = this.untouchedJobList.filter((job) => {
                        const title = job.title.toLowerCase();
                        return title.startsWith(event.query.toLowerCase());
                    }).map((job) => job.title); // extracting only the 'title' property
                }
            }, 200);
        },

        retrieveListings(searchVar) {
            fetch('jobs.json')
                .then(res => res.json())
                .then(data => {
                    let jobTitleSearch = searchVar.toLowerCase()
                    this.jobs = this.untouchedJobList.filter((job) => {
                        return job.title.toLowerCase().includes(jobTitleSearch)
                    });
                });
        }
    },
}
</script>

<style scoped>
#header {
    /* text-align: center; */
    margin: 20px;
}

.div-hover {
    background-color: lightgrey;
}
</style scoped>