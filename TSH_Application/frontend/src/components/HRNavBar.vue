<template>
    <div class="card">
        <Menubar :model="items" style="padding-left: 20%; padding-top: 1%; background-color: white; color: darkblue; " >
            <template #start>
                <img src="../assets/tsh-logo.png" style="height: 40px">
            </template>
        </Menubar>
    </div>
</template>

<script>
import Menubar from 'primevue/menubar';
export default {
    data() {
        return {
            items: [
                {
                    label: 'Home',
                    command:() => {
                        this.$router.push({
                            name: "HRHome"
                        })
                    }
                },
                {
                    label: 'Dashboard',
                    command:() => {
                        this.$router.push({
                            name: "HRDashboard"
                        })
                    }
                }, 
                {
                    label: 'Job Listings',
                    command:() => {
                        this.$router.push({
                            name: "HRJobListings"
                        })
                    }
                },
                {
                    label: "Applicant",
                    command:() => {
                        this.$router.push({
                            name: "Home"
                        })
                    }
                },
                {
                    label: "Manager",
                    command:() => {
                        this.$router.push({
                            name: "Manager"
                        })
                    }
                },
            ]
        }
    }

}
</script>
<style scoped>

</style>