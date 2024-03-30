<template>
    <div class="row" style="height: 30px; background-color: darkblue; color: white; padding-left: 50%">
        <span class="ml-4"> <i class="pi pi-phone mx-2 mt-1" style="color: white;"></i>Office Tel: +65 62800555 &emsp;&emsp;&emsp;&emsp; <i class="pi pi-envelope mx-1 mt-2" style="color: white;"></i> Email: sales@tshgroup.com.sg</span>         
    </div>
    <div class="card">
        <Menubar :model="items" style="padding-left: 10%; padding-top: 1%; background-color: white; color: darkblue;" >
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
                },
                {
                    label: 'About TSH'
                }, 
                {
                    label: 'Core Business'
                },
                {
                    label: 'Business Infrastructure'
                },
                {
                    label: 'Milestone'
                },                
                {
                    label: 'Careers',
                    command:() => {
                        this.$router.push({
                            name: "Home"
                        })
                    }
                },
                {
                    label: 'Contact Us'
                },
                {
                    label: "HR",
                    command: () => {
                        this.$router.push({
                            name: "HRHome"
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
 .p-menuitem-link{
    text-decoration: none;
 }

</style>