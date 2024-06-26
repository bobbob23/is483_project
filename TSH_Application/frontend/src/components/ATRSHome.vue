<template>
    <NavBar />
    <Banner msg="CAREERS AT TSH" />
    <Toolbar>
        <template #center>
            <div>
                <span class="p-input-icon-left">
                    <AutoComplete v-model="searchItem" placeholder="Search by keyword" style="border-radius: 100px;"
                        :suggestions="jobListingTitles" @complete="search" @keyup.enter="retrieveListings(searchItem)" />
                </span>
                <span>
                    <Button label="Search Jobs" style="margin-left: 20px; 
                        border-radius: 50px; background-color: darkblue" @click="retrieveListings(searchItem)"/>
                </span>
            </div>
        </template>
    </Toolbar>
    <div v-if="jobs.length == 0 && !selectedLocation && !selectedExperience" class="text-center mt-5">
        <i class="pi pi-spin pi-spinner" style="font-size: 3em;"></i> <!-- Progress spinner -->
    </div>
    <div v-else>
        <div class="row">
            <div class="mt-4 col-1">
            </div>
            <div class="mt-4 col-3">
                <h3 style="margin-left: 75px;">Filters</h3>
            </div>
            <div class="col-1">
            </div>
            <div class="p-2 col-7">
                <h3 id="header" style="padding-left: 50px;">Available Jobs</h3>
                <hr>
            </div>
        </div>

        <div class="container">
            <div class="row">
                <div class="col-1">
                </div>
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
                <div class="col-7">
                    <Card v-for="(job, index) in jobs" :key="job.title" style="margin-bottom: 20px; margin-left: 30px;"
                        @click="viewRoleListing(job.job_ID)" @mouseenter="hover[index] = true"
                        @mouseleave="hover[index] = false" class="div" :class="{ 'div-hover': hover[index] }">
                        <template #title>{{ job.title }}</template>
                        <template #content>
                            <span class="m-3">
                                <i class="pi pi-map-marker mx-2"></i>{{ job.location }}
                            </span>
                            <span class="m-3">
                                <i class="pi pi-users mx-2"></i>{{ job.type }}
                            </span>
                            <span class="m-3">
                                <i class="pi pi-briefcase mx-2"></i>{{ job.department }}
                            </span>
                        </template>
                    </Card>
                </div>
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
import Banner from './Banner.vue'
import NavBar from './NavBar.vue'
import axios from "axios";
import { getAllActiveJob } from "@/api/api.js";


export default {
    components: {
        Banner,
        NavBar
    },
    data() {
        return {
            jobs: [], // to be used to populate all listings
            untouchedJobList: [], // original job list that contains all job listings
            jobListingTitles: [], // to be used to populate datalist tag for search bar
            selectedExperience: "",
            experienceLevel: ["Internship", "Full-Time"],
            selectedLocation: "",
            countries: ["Singapore", "Malaysia"],
            searchItem: "",
            hover: [],
            loading: true,
        };
    },
    mounted() {
        axios.get(getAllActiveJob)
            .then((response) => {
                this.jobs = response.data.data
                console.log(this.jobs)
                this.untouchedJobList = response.data.data
                this.hover = new Array(response.data.data.length).fill(false);
            })
    },
    methods: {
        viewRoleListing(job_ID) {
            this.$router.push({
                name: "JobDetails",
                params: {
                    job_ID: job_ID
                }
            })
        },
        reloadListings(selectedExperience, selectedLocation) {
            axios.get(getAllActiveJob)
                .then((response) => {
                    if (!selectedExperience && !selectedLocation) {
                        this.jobs = response.data.data;
                    } else if (selectedExperience && selectedLocation) {
                        this.jobs = response.data.data.filter(job => {
                            return job.type === selectedExperience && job.location === selectedLocation;
                        });
                    } else if (selectedLocation) {
                        this.jobs = response.data.data.filter(job => job.location === selectedLocation);
                    } else {
                        this.jobs = response.data.data.filter(job => job.type === selectedExperience);
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
            axios.get(getAllActiveJob)
                .then((response) => {
                    console.log(response.data.data)
                    let jobTitleSearch = searchVar.toLowerCase()
                    this.jobs = this.untouchedJobList.filter((job) => {
                        return job.title.toLowerCase().includes(jobTitleSearch)
                    });
                })
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