from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from ruamel.yaml import YAML


def extract_comment(node, key):
    """Safely extracts the inline comment for a given key from a ruamel.yaml node."""
    try:
        comments = node.ca.items.get(key)
        # Inline comments are typically in the 3rd position of the comment array
        if comments and len(comments) >= 3 and comments[2]:
            raw_comment = comments[2].value.strip("# \n")
            return raw_comment
    except (AttributeError, TypeError):
        pass
    return ""


def split_instruction(comment):
    """Splits the YAML comment into General Instructions and Format rules."""
    parts = [p.strip() for p in comment.split("|")]
    if not parts or parts == [""]:
        return "", ""

    # Extract the format part if it exists
    format_rule = ""
    general_inst = []
    for part in parts:
        if part.lower().startswith("format:"):
            format_rule = part
        else:
            general_inst.append(part)

    return " | ".join(general_inst), format_rule


def format_instruction_rows(ws, end_col_letter, num_rows=2):
    """Applies gray background, italics, and freezes panes for instruction rows."""
    gray_fill = PatternFill(start_color="F2F2F2", end_color="F2F2F2", fill_type="solid")
    italic_font = Font(italic=True, color="555555")

    for row in range(1, num_rows + 1):
        for col in range(1, ws.max_column + 1):
            cell = ws.cell(row=row, column=col)
            cell.fill = gray_fill
            cell.font = italic_font

    # Freeze panes so user scrolling doesn't hide headers
    ws.freeze_panes = ws.cell(row=num_rows + 2, column=1)


def autofit_columns(ws):
    """Iterates through all columns in a worksheet and adjusts the width to fit the longest string."""
    for column in ws.columns:
        max_length = 0
        # Get the column letter (e.g., 'A', 'B', 'C')
        column_letter = get_column_letter(column[0].column)

        for cell in column:
            try:
                # Find the length of the string in the cell
                if cell.value and len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass

        # Add a little extra padding so it doesn't look too cramped
        adjusted_width = max_length + 2
        ws.column_dimensions[column_letter].width = adjusted_width


def main():
    yaml = YAML()
    yaml.preserve_quotes = True

    # Load your YAML template
    # Replace 'AQDx_metadata_form_v3.yaml' with your actual file path
    with open("../../docs/assets/AQDx_metadata_form_v3.yaml", "r") as f:
        data = yaml.load(f)

    wb = Workbook()

    # --------------------------------------------------------------------------
    # TAB 1: Project_Info (Vertical Layout)
    # --------------------------------------------------------------------------
    ws_proj = wb.active
    ws_proj.title = "Project_Info"
    ws_proj.append(["Metadata Field", "Response", "Instructions"])

    # Collect root keys, data_steward, and dataset_quality
    proj_sections = [
        (data, ["dataset_id", "aqdx_metadata_version", "aqdx_data_version"]),
        (data["data_steward"], data["data_steward"].keys()),
        (data["dataset_quality"], data["dataset_quality"].keys()),
    ]

    for node, keys in proj_sections:
        for key in keys:
            comment = extract_comment(node, key)
            ws_proj.append([key, "", comment])

    # Format Tab 1
    for col in range(1, 4):
        ws_proj.cell(row=1, column=col).font = Font(bold=True)
    ws_proj.freeze_panes = "A2"

    # --------------------------------------------------------------------------
    # TAB 2: Sites (Horizontal Layout)
    # --------------------------------------------------------------------------
    ws_sites = wb.create_sheet(title="Sites")
    site_node = data["sites"][0]  # Grab the first item to get the keys

    instructions, formats, headers = [], [], []
    for key in site_node.keys():
        comment = extract_comment(site_node, key)
        inst, fmt = split_instruction(comment)
        instructions.append(inst)
        formats.append(fmt)
        headers.append(key)

    ws_sites.append(instructions)
    ws_sites.append(formats)
    ws_sites.append(headers)

    # Bold the headers
    for cell in ws_sites[3]:
        cell.font = Font(bold=True)
    format_instruction_rows(ws_sites, "Z", num_rows=2)

    # --------------------------------------------------------------------------
    # TAB 3: Instruments (Horizontal Layout)
    # --------------------------------------------------------------------------
    ws_inst = wb.create_sheet(title="Instruments")
    inst_node = data["instruments"][0]

    instructions, formats, headers = [], [], []
    for key in inst_node.keys():
        if key == "parameters":
            continue  # Handle parameters in the next tab
        comment = extract_comment(inst_node, key)
        inst, fmt = split_instruction(comment)
        instructions.append(inst)
        formats.append(fmt)
        headers.append(key)

    ws_inst.append(instructions)
    ws_inst.append(formats)
    ws_inst.append(headers)

    for cell in ws_inst[3]:
        cell.font = Font(bold=True)
    format_instruction_rows(ws_inst, "Z", num_rows=2)

    # Add Data Validation for site_name (Column B in Instruments) pointing to Sites Tab
    dv_site = DataValidation(
        type="list", formula1="=Sites!$A$4:$A$1000", allow_blank=True
    )
    ws_inst.add_data_validation(dv_site)
    dv_site.add("B4:B1000")  # Apply to the site_name rows

    # --------------------------------------------------------------------------
    # TAB 4: Parameters (Horizontal Layout)
    # --------------------------------------------------------------------------
    ws_params = wb.create_sheet(title="Parameters")
    param_node = data["instruments"][0]["parameters"][0]

    # Explicitly add device_id to link it back to the instrument
    instructions = ["REQUIRED | Matches tabular data"]
    formats = ["Format: string"]
    headers = ["device_id"]

    for key in param_node.keys():
        comment = extract_comment(param_node, key)
        inst, fmt = split_instruction(comment)
        instructions.append(inst)
        formats.append(fmt)
        headers.append(key)

    ws_params.append(instructions)
    ws_params.append(formats)
    ws_params.append(headers)

    for cell in ws_params[3]:
        cell.font = Font(bold=True)
    format_instruction_rows(ws_params, "Z", num_rows=2)

    # Add Data Validation for device_id (Column A in Parameters) pointing to Instruments Tab
    dv_device = DataValidation(
        type="list", formula1="=Instruments!$A$4:$A$1000", allow_blank=True
    )
    ws_params.add_data_validation(dv_device)
    dv_device.add("A4:A1000")

    # Auto-fit columns for all sheets before saving
    autofit_columns(ws_proj)
    autofit_columns(ws_sites)
    autofit_columns(ws_inst)
    autofit_columns(ws_params)

    # --------------------------------------------------------------------------
    # Save the Workbook
    # --------------------------------------------------------------------------
    output_filename = "AQDx_metadata_template.xlsx"
    wb.save(output_filename)
    print(f"Spreadsheet generated successfully: {output_filename}")


if __name__ == "__main__":
    main()
