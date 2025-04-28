import { createRouter, createWebHistory } from "vue-router";

// Import your page components
import Home from "@/views/Home.vue";
import Crawl from "@/views/Crawl.vue";
import CrawlOutput from "@/views/CrawlOutput.vue";
import BruteForce from "@/views/BruteForce.vue";
import BruteForceOutput from "@/views/BruteForceOutput.vue";
import SQLInjection from "@/views/SQLInjection.vue";
import SQLInjectionOutput from "@/views/SQLInjectionOutput.vue";
import XSSAttack from "@/views/XSSAttack.vue";
import XSSAttackOutput from "@/views/XSSAttackOutput.vue";

const routes = [
  { path: "/", name: "Home", component: Home },
  { path: "/crawl", name: "Crawl", component: Crawl },
  { path: "/crawl_output", name: "CrawlOutput", component: CrawlOutput },
  { path: "/brute_force", name: "BruteForce", component: BruteForce },
  {
    path: "/brute_force_output",
    name: "BruteForceOutput",
    component: BruteForceOutput,
  },
  { path: "/sql_injection", name: "SQLInjection", component: SQLInjection },
  {
    path: "/sql_injection_output",
    name: "SQLInjectionOutput",
    component: SQLInjectionOutput,
  },
  { path: "/xss_attack", name: "XSSAttack", component: XSSAttack },
  {
    path: "/xss_attack_output",
    name: "XSSAttackOutput",
    component: XSSAttackOutput,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
