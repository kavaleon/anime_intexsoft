import { createRouter, createWebHistory } from 'vue-router'
import AuthLayout from './layouts/AuthLayout.vue'
import login from './views/auth/login.vue'
import register from './views/auth/register.vue'
import NotFoundPage from './views/NotFoundPage.vue'
import QuestionPage from './views/types/QuestionPage.vue'
import QuizLayout from './layouts/QuizLayout.vue'
import LandingPage from './views/LandingPage.vue'
import HomePage from './views/HomePage.vue'
import ResultPage from './views/ResultPage.vue'
import { components } from 'vuetify/dist/vuetify.js'
import UserResultsPage from './views/UserResultsPage.vue'

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
    name: 'HomePage',
    component: HomePage,
  },
  {
    path: '/quiz/:id/',
    component: QuizLayout,
    props: true,
    children:[
      {
        path: 'question/:pk',
        name: 'question',
        component: QuestionPage,
      },
    ]
  },
  {
    path: '/quiz/:id/result',
    name: 'ResultPage',
    component: ResultPage,
  },
  {
    path: '/user/:id/results',
    name: 'UserResultsPage',
    component: UserResultsPage,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router