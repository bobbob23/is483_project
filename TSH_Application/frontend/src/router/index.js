// Composables
import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "Home",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import("@/components/ATRSHome.vue"),
  },
  
  {
    path: "/job/:job_ID",
    name: "JobDetails",
    component: () => import("@/components/JobPage.vue"),
    props: (route) => ({
      job_ID: route.params.job_ID,
    }),
  },

  {
    path: "/apply/:job_ID",
    name: "ApplyForm",
    component: () => import("@/components/JobApplication.vue"),
    props: (route) => ({
      job_ID: route.params.job_ID,
    }),
  },

  {
    path: "/apply2",
    name: "ApplyForm2",
    component: () => import("@/components/JobApplication2.vue"),
    // props: (route) => ({
    //   job_ID: route.params.job_ID,
    // }),
  },

  {
    path: "/success/:job_title",
    name: "Success",
    component: () => import("@/components/ApplySuccess.vue"),
    props: (route) => ({
      job_title: route.params.job_title,
    }),
  },
  {
    path: "/hr_success/:job_title",
    name: "HRSuccess",
    component: () => import("@/components/CreateSuccess.vue"),
    // props: (route) => ({
    //   job_title: route.params.job_title,
    //   opening_date: route.params.opening_date
    // }),
  },
  {
    path:"/hr_previewjob/:jobTitle",
    name:"PreviewNewJob",
    component: () => import("@/components/PreviewNewJob.vue"),
  },
  {
    path:"/hr_createjob",
    name:"CreateJobPage",
    component: () => import("@/components/CreateJobPage.vue"),
  },
  {
    path:"/hr",
    name:"HRHome",
    component: () => import("@/components/HRHome.vue"),
  },
  {
    path:"/hr_jobs",
    name:"HRJobListings",
    component: () => import("@/components/HRJobListings.vue"),
  },
  {
    path:"/applicants/:job_ID/:job_title",
    name:"HRJobApplicants",
    component: () => import("@/components/HRJobApplicants.vue"),
    props: (route) => ({
      job_ID: route.params.job_ID,
      job_title: route.params.job_title,
    }),
  },
  {
    path: "/view/:email/:job_ID",
    name:"ViewApplicant",
    component: () => import("@/components/ViewApplicantPage.vue"),
    props: (route) => ({
      job_ID: route.params.job_ID,
      email: route.params.email,
    }),
  },
  {
    path: "/manager",
    name:"Manager",
    component: () => import("@/components/ManagerDashboard.vue"),
  },
  {
    path: "/hr_dashboard",
    name:"HRDashboard",
    component: () => import("@/components/HRDashboard.vue"),
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
