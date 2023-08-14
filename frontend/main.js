import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'

const el = document.getElementById('app')
if (el){

console.log(el.dataset)

createApp(App).mount('#app')

}