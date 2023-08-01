<!-- src/App.vue -->
<template>
  <div id="app">
    <StudentsList />
    <ReportForm />
    <AdminLogin />
  </div>
</template>

<script>
import StudentsList from './components/StudentsList.vue';
import ReportForm from './components/ReportForm.vue';
import AdminLogin from './components/AdminLogin.vue';


export default {
  name: 'App',
  components: {
    StudentsList,
    ReportForm,
    AdminLogin
  },
};
</script>

<style>
#app {
  font-family: Arial, Helvetica, sans-serif;
  padding: 20px;
}
</style>
