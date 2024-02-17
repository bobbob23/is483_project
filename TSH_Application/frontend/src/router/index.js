// Composables
import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "Home",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "home" */ "@/components/ATRSHome.vue"),
  },

  {
    path: "/Job",
    name: "JobDetails",
    component: () =>
      import(/* webpackChunkName: "job" */ "@/components/JobPage.vue"),
  },

  {
    path: "/Apply",
    name: "ApplyForm",
    component: () =>
      import(/* webpackChunkName: "job" */ "@/components/JobApplication.vue"),
  },

  {
    path: "/Success",
    name: "Success",
    component: () =>
      import(/* webpackChunkName: "job" */ "@/components/ApplySuccess.vue"),
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
