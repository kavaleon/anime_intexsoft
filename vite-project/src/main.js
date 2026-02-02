import '@splidejs/splide/css';
import { createApp } from 'vue'
import App from './App.vue'
import router from './routers.js'
import VueSplide from '@splidejs/vue-splide';


import { createVuetify } from 'vuetify'
import 'vuetify/styles'

import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
  components,
  directives,
})


createApp(App)
  .use(router)
  .use(VueSplide)
  .use(vuetify)
  .mount('#app')