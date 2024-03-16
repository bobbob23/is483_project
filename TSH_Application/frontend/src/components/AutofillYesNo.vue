<template>
    <div>
        <NavBar />
            <Button label="< Back" class="mt-2 mx-2"
                style="border-radius: 20%; border: lightgrey; height: 35px; background-color: white; color: black "
                @click="$router.go(-1)"></Button>
        
        </div>
</template>

<script>
import NavBar from './NavBar.vue'

export default {
    components: {
        NavBar
    }
}
</script>