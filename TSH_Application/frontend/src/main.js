import './assets/main.css'
import { createApp } from 'vue';
import App from './App.vue';
const app = createApp(App);

/* import primevue ui components */
import 'primevue/resources/primevue.min.css';
import 'primevue/resources/themes/bootstrap4-light-blue/theme.css';
import PrimeVue from 'primevue/config';
import Card from 'primevue/card';
import Toolbar from 'primevue/toolbar';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';

/* use imported primevue components */
app.component('Card', Card);
app.component('Toolbar', Toolbar)
app.component('InputText', InputText)
app.component('Button', Button)

app.use(PrimeVue).mount('#app')