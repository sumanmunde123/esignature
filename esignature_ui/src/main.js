import './index.css'

import { createApp } from 'vue'
import router from './router'
import App from './App.vue'
import { createPinia } from 'pinia';
import { Button, setConfig, frappeRequest, resourcesPlugin } from 'frappe-ui'

let app = createApp(App)
const pinia = createPinia()


setConfig('resourceFetcher', frappeRequest)
app.config.unwrapInjectedRef = true
app.use(router)
app.use(resourcesPlugin)

app.component('Button', Button)
app.use(pinia)
app.mount('#app')
