import './assets/main.css'
import { createApp } from 'vue';
import App from './App.vue';
const app = createApp(App);

/* import primevue ui components */
import PrimeVue from 'primevue/config';
import Card from 'primevue/card';
import 'primevue/resources/primevue.min.css';
import 'primevue/resources/themes/bootstrap4-light-blue/theme.css';

/* use imported primevue components */
app.component('Card', Card);

app.use(PrimeVue).mount('#app')