# Sampling Methods for All Parameters

## [Copied from EPA AQS Feb 2026](https://aqs.epa.gov/aqsweb/documents/codetables/methods_all.html)

_AQS Reference Table_

<table id="csvTable" class="display" style="width:100%"></table>

<script>
document.addEventListener("DOMContentLoaded", function() {
  const csvFile = "/aqdx-documentation/assets/methods_all.csv";

  Papa.parse(csvFile, {
    download: true,
    header: true,
    skipEmptyLines: true,
    complete: function(results) {
      // 1. Generate headers
      const headers = Object.keys(results.data[0]).map(header => ({
        title: header,
        data: header
      }));

      // 2. Clear old table
      if ($.fn.DataTable.isDataTable('#csvTable')) {
         $('#csvTable').DataTable().destroy();
      }

      // 3. Initialize DataTable
      var table = $('#csvTable').DataTable({
        data: results.data,
        columns: headers,

        // --- LAYOUT & SCROLLING ---
        scrollY: '60vh',
        scrollCollapse: true,
        scrollX: true,
        paging: true,
        pageLength: 50,
        deferRender: true,
        autoWidth: false,

        // --- PINNING COLUMNS ---
        fixedColumns: {
           left: 3   // <--- Pins the first 3 columns
        },

        // --- SEARCH BOXES ---
        initComplete: function () {
            this.api().columns().every(function () {
                var column = this;
                var header = $(column.header());
                var title = header.text().trim();

                // Create input
                var input = $('<input type="text" placeholder="Filter ' + title + '" />')
                    .css({
                        "width": "100%",
                        "box-sizing": "border-box",
                        "font-size": "0.85em",
                        "margin-top": "5px",
                        "padding": "3px",
                        "border": "1px solid #ccc",
                        "border-radius": "3px",
                        "font-weight": "normal" // prevents bold text in input
                    })
                    .appendTo(header)
                    .on('click', function(e) { e.stopPropagation(); })
                    .on('keyup change clear', function () {
                        if (column.search() !== this.value) {
                            column.search(this.value).draw();
                        }
                    });
            });
        }
      });
    }
  });
});
</script>
