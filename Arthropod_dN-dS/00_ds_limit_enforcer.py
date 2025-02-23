# This script removes all dS value that is lower than 0.0001 or greater than 2 from the analysis. It also removes all dN/dS values that are greater than 3.
import json

def filter_json(input_json_path, output_json_path):
    with open(input_json_path, 'r') as f:
        data = json.load(f)

    if "branch attributes" in data:
        branch_attitude = data["branch attributes"]
        if "0" in branch_attitude:
            keys_to_remove = []
            for key, value in branch_attitude["0"].items():
               # print(value)
                if "dS" in value and value["dS"] < 0.0001:
                    keys_to_remove.append(key)
                if "dS" in value and value["dS"] >2:
                    keys_to_remove.append(key)
                if "dN" in value and value["dN"]/value["dS"] >3:
                    keys_to_remove.append(key)
            
            for key in keys_to_remove:
                del branch_attitude["0"][key]
        else:
            print("no 0")
    else:
        print("no branch attitude")

    with open(output_json_path, 'w') as f:
        json.dump(data, f, indent=4)

# Example usage
input_json_path = "Extracellular_dn-ds.json"
output_json_path = "output.json"
filter_json(input_json_path, output_json_path)
