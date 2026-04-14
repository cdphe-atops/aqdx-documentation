---
hide:
  - toc
---

# Measurement Technology Codes

The `measurement_technology_code` categorizes the physical journey of an air sample from acquisition to the final analytical signal using a flexible, "building block" taxonomy.

Rather than relying on an exhaustive list of every possible instrument brand or configuration, you construct an 8-to-14 character code by selecting the specific functional steps your measurement system utilizes: **`[Acquisition] - [Conditioning] - [Detection]`**.

> For detailed "Bright Line" rules on how to classify complex setups (like when to use `00` vs. a conditioning step), please refer to the [Field Dictionary](../standard-format/field-dictionary.md#measurement_technology_code).

---

## Code Builder

Use the dropdowns below to accurately map your instrument's physical process to an AQDx `measurement_technology_code`.

<div class="admonition info">
  <p class="admonition-title">Your Generated Code</p>
  <div id="code-output" style="font-family: monospace; font-size: 2em; font-weight: bold; text-align: center; margin: 15px 0; color: var(--md-code-hl-string-color, #009688);">
    Loading definitions...
  </div>
  <button id="copy-btn" class="md-button md-button--primary" style="display: block; margin: 0 auto;" disabled>Copy Code</button>
</div>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-top: 20px;">

  <div style="background: var(--md-default-bg-color); padding: 15px; border-radius: 5px; border: 1px solid var(--md-default-fg-color--light);">
    <h3 style="margin-top: 0;">1. Acquisition</h3>
    <label for="acq-main" style="font-weight: bold; font-size: 0.9em;">Broad Method (XX)</label>
    <select id="acq-main" style="width: 100%; padding: 8px; margin-bottom: 10px;" disabled></select>

    <div id="acq-detail-container" style="display: none;">
      <label for="acq-detail" style="font-weight: bold; font-size: 0.9em;">Subtype (xx)</label>
      <select id="acq-detail" style="width: 100%; padding: 8px;"></select>
    </div>

  </div>

  <div style="background: var(--md-default-bg-color); padding: 15px; border-radius: 5px; border: 1px solid var(--md-default-fg-color--light);">
    <h3 style="margin-top: 0;">2. Conditioning</h3>
    <label for="cond-main" style="font-weight: bold; font-size: 0.9em;">Treatment Step (XX)</label>
    <select id="cond-main" style="width: 100%; padding: 8px; margin-bottom: 10px;" disabled></select>

    <div id="cond-detail-container" style="display: none;">
      <label for="cond-detail" style="font-weight: bold; font-size: 0.9em;">Subtype (xx)</label>
      <select id="cond-detail" style="width: 100%; padding: 8px;"></select>
    </div>

  </div>

  <div style="background: var(--md-default-bg-color); padding: 15px; border-radius: 5px; border: 1px solid var(--md-default-fg-color--light);">
    <h3 style="margin-top: 0;">3. Detection</h3>
    <label for="det-main" style="font-weight: bold; font-size: 0.9em;">Detector Tech (XX)</label>
    <select id="det-main" style="width: 100%; padding: 8px; margin-bottom: 10px;" disabled></select>

    <div id="det-detail-container" style="display: none;">
      <label for="det-detail" style="font-weight: bold; font-size: 0.9em;">Subtype (xx)</label>
      <select id="det-detail" style="width: 100%; padding: 8px;"></select>
    </div>

  </div>

</div>

---

## Example Configurations

If you are using standard, widely adopted equipment, you can reference these common configurations.

<table>
  <thead>
    <tr>
      <th>Instrument / Setup</th>
      <th>Code</th>
    </tr>
  </thead>
  <tbody id="example-table-body">
    <tr>
      <td colspan="2" style="text-align: center; color: gray;">Loading examples...</td>
    </tr>
  </tbody>
</table>

<script src="https://cdnjs.cloudflare.com/ajax/libs/js-yaml/4.1.0/js-yaml.min.js"></script>

<script>
document.addEventListener("DOMContentLoaded", function() {

  // DOM Elements
  const acqMain = document.getElementById('acq-main');
  const acqDetail = document.getElementById('acq-detail');
  const acqDetailCont = document.getElementById('acq-detail-container');

  const condMain = document.getElementById('cond-main');
  const condDetail = document.getElementById('cond-detail');
  const condDetailCont = document.getElementById('cond-detail-container');

  const detMain = document.getElementById('det-main');
  const detDetail = document.getElementById('det-detail');
  const detDetailCont = document.getElementById('det-detail-container');

  const outputField = document.getElementById('code-output');
  const copyBtn = document.getElementById('copy-btn');
  const tableBody = document.getElementById('example-table-body');

  // The parsed YAML taxonomy will live here
  let taxonomy = {};

  // Fetch the YAML file from the MkDocs assets directory
  const yamlUrl = "/aqdx-documentation/assets/measurement_technology_codes.yaml";

  fetch(yamlUrl)
    .then(response => {
      if (!response.ok) {
        throw new Error("Network response was not ok: " + response.statusText);
      }
      return response.text();
    })
    .then(yamlText => {
      // Parse the YAML text into a JS object
      const parsedData = jsyaml.load(yamlText);
      taxonomy = parsedData.taxonomy;

      // Enable the dropdowns and button now that data is loaded
      acqMain.disabled = false;
      condMain.disabled = false;
      detMain.disabled = false;
      copyBtn.disabled = false;

      // Populate the Example Configurations table
      if (parsedData.example_configurations) {
        tableBody.innerHTML = ''; // Clear loading text
        parsedData.example_configurations.forEach(item => {
          let tr = document.createElement('tr');
          tr.innerHTML = `<td><strong>${item.setup}</strong></td><td><code>${item.code}</code></td>`;
          tableBody.appendChild(tr);
        });
      } else {
        tableBody.innerHTML = '<tr><td colspan="2" style="text-align: center;">No examples found.</td></tr>';
      }

      // Initialize the dropdowns with data
      populateSelect(acqMain, taxonomy.acquisition, "DA");
      populateSelect(condMain, taxonomy.conditioning, "00");
      populateSelect(detMain, taxonomy.detection, "SC");

      // Update subtypes based on the new nested YAML structure
      updateDetails("DA", acqDetail, acqDetailCont, "acquisition");
      updateDetails("00", condDetail, condDetailCont, "conditioning");
      updateDetails("SC", detDetail, detDetailCont, "detection");

      updateCode(); // Generate initial string
    })
    .catch(error => {
      console.error("Error loading taxonomy YAML:", error);
      outputField.innerText = "Error loading codes.";
      outputField.style.color = "red";
      tableBody.innerHTML = '<tr><td colspan="2" style="text-align: center; color: red;">Failed to load examples.</td></tr>';
    });

  // Populate primary selects
  function populateSelect(selectElem, dataObj, defaultVal) {
    selectElem.innerHTML = '';
    for (const [key, val] of Object.entries(dataObj)) {
      let option = document.createElement('option');
      option.value = key;
      // Navigate to val.name because of the nested YAML structure
      option.text = `${key} - ${val.name}`;
      selectElem.appendChild(option);
    }
    if (defaultVal) selectElem.value = defaultVal;
  }

  // Handle subtype generation using the category to locate it in the taxonomy
  function updateDetails(mainVal, detailElem, detailCont, category) {
    detailElem.innerHTML = '<option value="">-- None / General --</option>';

    // Check if the selected broad code has a subtypes object
    if (taxonomy[category][mainVal] && taxonomy[category][mainVal].subtypes) {
      for (const [key, val] of Object.entries(taxonomy[category][mainVal].subtypes)) {
        let option = document.createElement('option');
        option.value = key;
        option.text = `${key} - ${val}`;
        detailElem.appendChild(option);
      }
      detailCont.style.display = 'block';
    } else {
      detailCont.style.display = 'none';
      detailElem.value = "";
    }
  }

  // Calculate and display the final string
  function updateCode() {
    const acq = acqMain.value + (acqDetail.value || '');
    const cond = condMain.value + (condDetail.value || '');
    const det = detMain.value + (detDetail.value || '');
    outputField.innerText = `${acq}-${cond}-${det}`;
  }

  // Event Listeners (Passing the category explicitly to updateDetails)
  acqMain.addEventListener('change', (e) => { updateDetails(e.target.value, acqDetail, acqDetailCont, "acquisition"); updateCode(); });
  condMain.addEventListener('change', (e) => { updateDetails(e.target.value, condDetail, condDetailCont, "conditioning"); updateCode(); });
  detMain.addEventListener('change', (e) => { updateDetails(e.target.value, detDetail, detDetailCont, "detection"); updateCode(); });

  acqDetail.addEventListener('change', updateCode);
  condDetail.addEventListener('change', updateCode);
  detDetail.addEventListener('change', updateCode);

  copyBtn.addEventListener('click', () => {
    navigator.clipboard.writeText(outputField.innerText).then(() => {
      const originalText = copyBtn.innerText;
      copyBtn.innerText = "Copied!";
      setTimeout(() => { copyBtn.innerText = originalText; }, 2000);
    });
  });

});
</script>
