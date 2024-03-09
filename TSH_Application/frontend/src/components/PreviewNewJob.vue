<template>
    <div>
        <HRNavBar/>
        
        <div>
            <Button label="< Back" class="mt-2 mx-2"
            style="border-radius: 20%; border: lightgrey; height: 35px; background-color: white; color: black "
            @click="$router.go(-1)" />
        </div>
        
    </div>
</template>

<script>
import HRNavBar from './HRNavBar.vue';
import axios from "axios";

export default {
    components: {
        HRNavBar
    },
}
</script>

<style>
.row {
  padding-top: 10px;
}
</style>