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
      import("@/components/ATRSHome.vue"),
  },
  {
    path: "/job/:job_ID",
    name: "JobDetails",
    component: () =>
      import("@/components/JobPage.vue"),
      props: (route) => ({
        job_ID: route.params.job_ID,
    })
  },

  {
    path: "/apply/:job_ID",
    name: "ApplyForm",
    component: () =>
      import("@/components/JobApplication.vue"),
      props: (route) => ({
        job_ID: route.params.job_ID,
    })
  },

  {
    path: "/success",
    name: "Success",
    component: () =>
      import("@/components/ApplySuccess.vue"),
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
