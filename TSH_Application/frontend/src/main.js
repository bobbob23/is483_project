import './assets/main.css'
import { createApp } from 'vue';
import App from './App.vue';
import { registerPlugins } from '@/plugins';
import { createStore } from 'vuex';
import VueCookies from 'vue-cookies'
const app = createApp(App);
registerPlugins(app);

/* import primevue ui components */
import 'primevue/resources/primevue.min.css';
import 'primevue/resources/themes/bootstrap4-light-blue/theme.css';
import "@lottiefiles/lottie-player";
import HighchartsVue from 'highcharts-vue'
import PrimeVue from 'primevue/config';
import Card from 'primevue/card';
import Toolbar from 'primevue/toolbar';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';
import Listbox from 'primevue/listbox';
import AutoComplete from 'primevue/autocomplete';
import FileUpload from 'primevue/fileupload';
import Dropdown from 'primevue/dropdown';
import Menubar from 'primevue/menubar';
import Message from 'primevue/message';
import Calendar from 'primevue/calendar';
import VirtualScroller from 'primevue/virtualscroller';
import MultiSelect from 'primevue/multiselect';
import Textarea from 'primevue/textarea';
import Dialog from 'primevue/dialog';
import Editor from 'primevue/editor';
import ProgressSpinner from 'primevue/progressspinner';


const store = createStore({
    state () {
        return {
            formData: {}
        }
    },
    mutations: {
        setFormData(state, formData) {
            state.formData = formData;
        }
    },
    actions: {
        updateFormData({commit}, formData) {
            commit('setFormData', formData);
        }
    },
    getters: {
        formData(state) {
            return state.formData;
        }
    }
});

/* use imported primevue components */
app.component('Card', Card);
app.component('Toolbar', Toolbar)
app.component('InputText', InputText)
app.component('Button', Button)
app.component('Listbox', Listbox)
app.component('AutoComplete', AutoComplete)
app.component("FileUpload", FileUpload)
app.component("Dropdown", Dropdown)
app.component("Menubar", Menubar)
app.component("Message", Message)
app.component("Calendar", Calendar)
app.component("VirtualScroller", VirtualScroller)
app.component("MultiSelect", MultiSelect)
app.component("Textarea", Textarea)
app.component("Dialog", Dialog)
app.component("Editor", Editor)
app.component("ProgressSpinner", ProgressSpinner)

app.use(PrimeVue)
app.use(HighchartsVue)
app.use(store)
app.use(VueCookies)

app.mount('#app')

