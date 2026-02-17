# Sampling Methods for All Parameters

## [Copied from EPA AQS Feb 2026](https://aqs.epa.gov/aqsweb/documents/codetables/methods_all.html)

_AQS Reference Table_

<table id="csvTable" class="display" style="width:100%"></table>

<script>
document.addEventListener("DOMContentLoaded", function() {
  // Path to your CSV file in the assets folder
  const csvFile = "/aqdx-documentation/assets/methods_all.csv";

  Papa.parse(csvFile, {
    download: true,
    header: true,
    skipEmptyLines: true,
    complete: function(results) {
      // 1. Get the Column Headers from the first row
      const headers = Object.keys(results.data[0]).map(header => ({
        title: header,
        data: header
      }));

      // 2. Initialize DataTables
      $('#csvTable').DataTable({
        data: results.data,
        columns: headers,
        pageLength: 25,       // Default rows per page
        lengthMenu: [10, 25, 50, 100],
        scrollX: true,        // Enable horizontal scrolling for many columns
        deferRender: true,    // Critical for performance with 10k rows
        processing: true
      });
    }
  });
});
</script>
