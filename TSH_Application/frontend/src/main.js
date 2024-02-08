import './assets/main.css'
import { createApp } from 'vue';
import App from './App.vue';
import { registerPlugins } from '@/plugins'
const app = createApp(App);
registerPlugins(app);

/* import primevue ui components */
import 'primevue/resources/primevue.min.css';
import 'primevue/resources/themes/bootstrap4-light-blue/theme.css';
import PrimeVue from 'primevue/config';
import Card from 'primevue/card';
import Toolbar from 'primevue/toolbar';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';
import Listbox from 'primevue/listbox';
import AutoComplete from 'primevue/autocomplete';

/* use imported primevue components */
app.component('Card', Card);
app.component('Toolbar', Toolbar)
app.component('InputText', InputText)
app.component('Button', Button)
app.component('Listbox', Listbox)
app.component('AutoComplete', AutoComplete)

app.use(PrimeVue).mount('#app')