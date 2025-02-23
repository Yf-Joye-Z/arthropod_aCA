# This script removes all dS value that is lower than 0.0001 or greater than 2 from the analysis. It also removes all dN/dS values that are greater than 3.

import json

# INSERT THE FILE NAME HERE ---> HARD CODED
input_json_path = ""
output_json_path = ""

def filter_json(input_json_path, output_json_path):
    with open(input_json_path, 'r') as f:
        data = json.load(f)
        
    #Iterating through the json file for the correct key and values
    if "branch attributes" in data:
        branch_attitude = data["branch attributes"]
        if "0" in branch_attitude:
            keys_to_remove = []
            for key, value in branch_attitude["0"].items():
                # moving keys with dS smaller than 0.0001 into the keys_to_remove list
                if "dS" in value and value["dS"] < 0.0001:
                    keys_to_remove.append(key)
                # moving keys with dN/dS greater than 3 into the keys_to_remove list
                elif "dN" in value and value["dN"]/value["dS"] >3:
                    keys_to_remove.append(key)
                # moving keys with dS greater than 2 into the keys_to_remove list  
                if "dS" in value and value["dS"] >2:
                    keys_to_remove.append(key)
            
            for key in keys_to_remove:
                # remove all keys from the input json file that has matched with the keys within the "keys_to_remove" list
                del branch_attitude["0"][key]
        else:
            print("no 0")
    else:
        print("no branch attitude")

    with open(output_json_path, 'w') as f:
        json.dump(data, f, indent=4)

filter_json(input_json_path, output_json_path)
