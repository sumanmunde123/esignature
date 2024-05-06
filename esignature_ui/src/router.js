import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/pages/Home.vue'),
  },
  {
    path: '/Inbox',
    name: 'Inbox',
    component: () => import('@/pages/Inbox.vue'),
  },
  {
    path: '/Sent',
    name: 'Sent',
    component: () => import('@/pages/Sent.vue'),
  },
  {
    path: '/Documents',
    name: 'Documents',
    component: () => import('@/pages/Documents.vue'),
  },
  {
    path: '/Templates',
    name: 'Templates',
    component: () => import('@/pages/Templates.vue'),
  },
  {
    path: '/New-Templates-Form',
    name: 'TemplatesForm',
    component: () => import('@/pages/TemplateForm.vue'),
  },
  {
    path: '/Test',
    name: 'Test',
    props:true,
    component: () => import('@/pages/Test.vue'),
  },
  {
    path: '/Demo',
    name: 'Demo',
    props:true,
    component: () => import('@/pages/Demo.vue'),
  },
  {
    path: '/Rough',
    name: 'Rough',
    props:true,
    component: () => import('@/pages/Rough.vue'),
  },
]

let router = createRouter({
  history: createWebHistory('/'),
  routes,
})

export default router
