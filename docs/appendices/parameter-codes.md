# Sampling Methods for All Parameters

## [Copied from EPA AQS Feb 2026](https://aqs.epa.gov/aqsweb/documents/codetables/methods_all.html)

_AQS Reference Table_

<table id="csvTable" class="display" style="width:100%"></table>

<script>
document.addEventListener("DOMContentLoaded", function() {
  // Path to your CSV file
  const csvFile = "/aqdx-documentation/assets/methods_all.csv";

  Papa.parse(csvFile, {
    download: true,
    header: true,
    skipEmptyLines: true,
    error: function(err, file) {
      console.error("Error:", err, file);
    },
    complete: function(results) {
      if (!results.data || results.data.length === 0) {
        console.error("CSV is empty");
        return;
      }

      // Generate headers
      const headers = Object.keys(results.data[0]).map(header => ({
        title: header,
        data: header
      }));

      // Initialize DataTables
      if ($.fn.DataTable.isDataTable('#csvTable')) {
         $('#csvTable').DataTable().destroy();
      }

      $('#csvTable').DataTable({
        data: results.data,
        columns: headers,
        pageLength: 25,
        deferRender: true,
        scrollX: true,
        autoWidth: false,

        // --- NEW: Add search boxes to headers ---
        initComplete: function () {
            this.api().columns().every(function () {
                var column = this;
                var title = column.header().textContent;

                // 1. Create the input element
                var input = document.createElement("input");
                input.placeholder = "Filter " + title;
                input.style.width = "100%";
                input.style.boxSizing = "border-box";
                input.style.fontSize = "0.9em";
                input.style.marginTop = "4px";
                input.style.padding = "4px";
                input.style.borderRadius = "4px";
                input.style.border = "1px solid #ddd";

                // 2. Append it to the header cell
                column.header().appendChild(input);

                // 3. Add the search logic
                $(input).on('keyup change clear', function () {
                    if (column.search() !== this.value) {
                        column.search(this.value).draw();
                    }
                });

                // 4. Stop clicks on input from sorting the column
                $(input).on('click', function(e) {
                    e.stopPropagation();
                });
            });
        }
      });
    }
  });
});
</script>
