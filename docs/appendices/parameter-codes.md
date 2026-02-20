---
hide:
  - toc
---

<table id="csvTable" class="display" style="width:100%"></table>

<script>
document.addEventListener("DOMContentLoaded", function() {
  const csvFile = "/aqdx-documentation/assets/parameters.csv";

  Papa.parse(csvFile, {
    download: true,
    header: true,
    skipEmptyLines: true,
    complete: function(results) {
      // --- Define columns to hide ---
      const hiddenCols = [
        "Round or Truncate"
      ];

      // --- Generate headers with visibility logic ---
      const headers = Object.keys(results.data[0]).map(header => ({
        title: header,
        data: header,
        visible: !hiddenCols.includes(header)
      }));

      // Clear old table
      if ($.fn.DataTable.isDataTable('#csvTable')) {
         $('#csvTable').DataTable().destroy();
      }

      // Initialize DataTable
      var table = $('#csvTable').DataTable({
        data: results.data,
        columns: headers,

        // --- ROW LIMITS & DROPDOWN ---
        pageLength: 5,                  // Default to 5 rows
        lengthMenu: [5, 10, 25, 50],    // Options in the dropdown
        lengthChange: true,             // Show the dropdown
        paging: true,                   // Enable pagination

        // --- LAYOUT ---
        // scrollY: '50vh',             // REMOVED (No vertical scrollbar)
        scrollX: true,                  // Keep horizontal scroll
        deferRender: true,
        autoWidth: false,

        // --- PINNING ---
        fixedColumns: {
           left: 3
        },

        // --- SEARCH BOXES ---
        initComplete: function () {
            this.api().columns().every(function () {
                var column = this;

                if (!column.visible()) return;

                var header = $(column.header());
                var title = header.text().trim();

                var input = $('<input type="text" placeholder="Filter ' + title + '" />')
                    .css({
                        "width": "100%",
                        "box-sizing": "border-box",
                        "font-size": "0.85em",
                        "margin-top": "5px",
                        "padding": "3px",
                        "border": "1px solid #ccc",
                        "border-radius": "3px",
                        "font-weight": "normal"
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

# [Copied from US EPA AQS Feb 2026](https://aqs.epa.gov/aqsweb/documents/codetables/methods_all.html)
