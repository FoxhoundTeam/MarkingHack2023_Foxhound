import Vue from 'vue'
import VueRouter from 'vue-router'

import LoginView from '@/views/LoginView.vue'

import PlotView from '@/views/PlotView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView,
    // beforeEnter: (/*to, from*/) => {},
  }, 

  {
    path: '/',
    name: 'PlotView',
    component: PlotView,
    // beforeEnter: (/*to, from*/) => {},
  },
  
]

const router = new VueRouter({
  routes
})

// router.beforeResolve((/*to, from, next*/)=>{console.log("router.beforeResolve");})
// router.beforeEach((to , from, next)=>{
//   console.log("router.beforeEach");
//   next();
//   // return false; // прервать переход
//   // return { name: 'Name' } или return '/url'
// });
// router.afterEach((/*to, from, failure*/)=>{console.log("router.afterEach");})

export default router
