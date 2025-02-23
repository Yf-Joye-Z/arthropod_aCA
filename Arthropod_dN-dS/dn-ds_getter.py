# This codes extracts all MLE (omega)value from the output text from json_parser.py

import json
from openpyxl import Workbook

def process_json_file(input_file, output_file):
    # Load JSON data
    with open(input_file, 'r') as json_file:
        data = json.load(json_file)
    
    # Create a new Excel workbook
    wb = Workbook()
    ws = wb.active
    
    # Add headers
    ws.append(["Original Name", "MLE"])

    # Iterate over keys within "branch attributes"->"0"
    if "branch attributes" in data:
        branch_data = data["branch attributes"].get("0", {})
        for key, value in branch_data.items():
            print(key)
            if "MLE" in value.get("Confidence Intervals", {}):
                mle_value = value["Confidence Intervals"]["MLE"]
                original_name = value.get("original name", "")
                ws.append([original_name, mle_value])
            else:
                print("no MLE")

    # Save the workbook
    wb.save(output_file)

# Input and output file paths
input_file = 'output.json'
output_file = 'Extracellular_omega.xlsx'

# Process JSON file
process_json_file(input_file, output_file)
