import '@splidejs/splide/css';
import { createApp } from 'vue'
import App from './App.vue'
import router from './routers.js'
import VueSplide from '@splidejs/vue-splide';
import { createPinia } from 'pinia'

import { createVuetify } from 'vuetify'
import 'vuetify/styles'

import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const pinia = createPinia()
const vuetify = createVuetify({
  components,
  directives,
})


createApp(App)
  .use(router)
  .use(VueSplide)
  .use(vuetify)
  .use(pinia)
  .mount('#app')