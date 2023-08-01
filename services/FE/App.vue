<script setup>
import { ref, computed } from 'vue'
import HelloWorld from './components/AdminLogin.vue'
import ReportForum from './components/ReportForm.vue'
import StudentList from './components/StudentsList.vue'

const routes = {
  '/': HelloWorld,
  '/students': StudentList,
  '/reports': ReportForum,
}

const currentPath = ref(window.location.hash)

window.addEventListener('hashchange', () => {
  currentPath.value = window.location.hash
})

const currentView = computed(() => {
  return routes[currentPath.value.slice(1) || '/'] 
})
</script>

<template>
  <a href="#/">Home</a> |
  <a href="#/students">Students</a> |
  <a href="#/reports">Reports</a>
  <component :is="currentView" />
</template>
