# This codes extracts all MLE (omega)value from the output json of json_parser.py

import json
from openpyxl import Workbook

# HARDCODED here. Please insert the file path and output file path
input_file = ''
output_file = ''

def process_json_file(input_file, output_file):
    # Loading JSON file
    with open(input_file, 'r') as json_file:
        data = json.load(json_file)
    
    # Creating an excel file
    wb = Workbook()
    ws = wb.active
    
    # Add headers
    ws.append(["Original Name", "MLE"])

    # Iterate over keys within "branch attributes" and "0".
    if "branch attributes" in data:
        branch_data = data["branch attributes"].get("0", {})
        # Iterating over the species for MLE value
        for key, value in branch_data.items():
            if "MLE" in value.get("Confidence Intervals", {}):
                mle_value = value["Confidence Intervals"]["MLE"]
                original_name = value.get("original name", "")
                ws.append([original_name, mle_value])
            #else:
                #print("no MLE")

    # Saving the excel
    wb.save(output_file)

# Process JSON file
process_json_file(input_file, output_file)
