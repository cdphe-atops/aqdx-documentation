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
      // --- Define columns to hide ---
      const hiddenCols = [
        "Federal MDL",
        "Min Value",
        "Max Value",
        "Digits",
        "Round Truncate Indicator"
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

        // --- UI CLEANUP ---
        lengthChange: false,   // <--- HIDES THE "SHOW ENTRIES" DROPDOWN

        // --- LAYOUT & SCROLLING ---
        scrollY: '50vh',
        scrollCollapse: true,
        scrollX: true,
        paging: true,
        pageLength: 50,
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

                // If column is hidden, don't generate a search box
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
