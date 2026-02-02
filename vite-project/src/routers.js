import { createRouter, createWebHistory } from 'vue-router'
import AuthLayout from './layouts/AuthLayout.vue'
import login from './views/auth/login.vue'
import register from './views/auth/register.vue'
import NotFoundPage from './views/NotFoundPage.vue'
import LandingPage from './views/LandingPage.vue';
import { components } from 'vuetify/dist/vuetify.js'
import HomePage from './views/HomePage.vue'

const routes = [
  {
    path: '/auth',
    component: AuthLayout,
    children: [
      {
        path: 'login',
        name: 'login',
        component: login,
      },
      {
        path: 'register',
        name: 'register',
        component: register,
      },
    ],
  },
  {
    path: '/:pathMatch(.*)*',
    component: NotFoundPage
  },

  {
      path: '/',
      name: 'LandingPage',
      component: LandingPage,
    },

  {
    path: '/home',
    name: "HomePage",
    component: HomePage,
  },
  {
    path: '/quiz/:id',
    component: QuizPage,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router