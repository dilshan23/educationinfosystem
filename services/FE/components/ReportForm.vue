<template>
  <div>
    <h2>Generate Report</h2>
    <form @submit.prevent="generateReport">
      <label>
        Student ID:
        <input type="number" v-model="studentId" required />
      </label>
      <br />
      <label>
        Year:
        <input type="number" v-model="year" required />
      </label>
      <br />
      <label>
        Term:
        <input type="text" v-model="term" required />
      </label>
      <br />
      <button type="submit">Generate Report</button>
    </form>
    <a v-if="pdfUrl" :href="pdfUrl" download>Download Report</a>
  </div>
</template>

<script>
export default {
  data() {
    return {
      studentId: 1, // Set the default studentId value
      year: 2023, // Set the default year value
      term: 'Term 1', // Set the default term value
      pdfUrl: null,
    };
  },
  methods: {
    async generateReport() {
      try {
        const response = await fetch('http://localhost:5000/generate_report', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            term: this.term,
            student_id: this.studentId,
            year: this.year,
          }),
        });

        if (response.ok) {
          // Get the PDF data from the response
          const pdfData = await response.blob();
          // Generate the URL for the Blob and set it as pdfUrl
          this.pdfUrl = URL.createObjectURL(pdfData);
        } else {
          alert('Error generating report.');
        }
      } catch (error) {
        console.error('Error generating report:', error);
      }
    },
  },
};
</script>

<style>
form {
  margin-bottom: 20px;
}

button {
  margin-top: 10px;
}
</style>
