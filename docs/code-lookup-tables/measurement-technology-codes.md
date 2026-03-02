---
hide:
  - toc
---

# Measurement Technology Codes

This table contains the approved, active `measurement_technology_code` combinations for the AQDx standard.

These 8-to-14 character codes chronologically categorize the physical journey of a sample from acquisition to the final analytical signal. Rather than naming specific brand-name instruments, this taxonomy breaks the measurement down into three functional, hyphen-delimited blocks:

**`[Acquisition] - [Conditioning] - [Detection]`**

For complete instructions on how to construct these codes, the strict rules for system boundaries, and the "00" bright-line rule, please refer to the `measurement_technology_code` section in the [Field Dictionary](../standard-format/field-dictionary.md).

> **Need a new code?** > If your specific hardware configuration is not listed below, please submit a "New Code Request" via the project's GitHub Issue Tracker. Do not invent custom codes outside of the `X-` provisional extension rules.

<br>

<table id="csvTable" class="display" style="width:100%"></table>

<script>
document.addEventListener("DOMContentLoaded", function() {
  const csvFile = "/aqdx-documentation/assets/measurement_tech_codes.csv";

  Papa.parse(csvFile, {
    download: true,
    header: true,
    skipEmptyLines: true,
    comments: "#", // Crucial: Skips the warning header in the auto-generated CSV
    complete: function(results) {
      // --- Define columns to hide ---
      const hiddenCols = []; // All columns are useful here

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
        pageLength: 10,                 // Default to 10 rows for this table
        lengthMenu: [5, 10, 25, 50, 100], // Options in the dropdown
        lengthChange: true,             // Show the dropdown
        paging: true,                   // Enable pagination

        // --- LAYOUT ---
        scrollX: true,                  // Keep horizontal scroll
        deferRender: true,
        autoWidth: false,

        // --- PINNING ---
        fixedColumns: {
           left: 1 // Only pin the 1st column (the code itself)
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
