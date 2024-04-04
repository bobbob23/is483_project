<template>
    <div class="flex justify-content-center">
        <Button label="Deactivate" style="display: block; margin: 0 auto; background-color: white; 
                                    color: darkblue; border: darkblue 1px solid; width: 80%;"
            @click="visible = true" />
        <Dialog v-model:visible="visible" modal header="Delete Job Listing" :style="{ width: '25rem' }">
            <p class="text-center">Are you sure that you want to delete this listing?</p>
            <div class="flex justify-content-center " style="text-align: center;">
                <Button type="button" label="Cancel" severity="secondary" @click="visible = false" link></Button>
                <Button type="button" label="Delete" @click="deleteJobListing(job_ID)"></Button>
            </div>
        </Dialog>
    </div>
</template>

<script>
import Dialog from 'primevue/dialog';
import { deleteJobListing } from '@/api/api';
import axios from 'axios';

export default {
    props: {
        job_ID: Number,
    },
    data() {
        return {
            visible: false,
            job: ""
        };
    },
    methods: {
        deleteJobListing(jobID){
            axios.delete(`${deleteJobListing}/${jobID}`)
                .then((response) => {
                    console.log(response.data)
                    console.log("works")
                })
        }
    }
};

</script>