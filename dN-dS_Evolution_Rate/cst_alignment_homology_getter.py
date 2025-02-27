# This is a python script that takes an amino acid alignment fasta file as an input and output a text file that contains column number of the alignment that show homology more than the percentage that is specified by the user at line 2.
# The utility of this script is to generate a auxillary file for the cst trimming mode of ClipKit (https://jlsteenwyk.com/ClipKIT/)
# This script is designed to be used with cst_aa-to-cds.py. This script will change the amino acid auxillary file into cds auxillary file. 

import csv
import os
from collections import Counter

# HARD CODED. Please insert the percent homology that you would like to retain.
# Ex) if percentage_homology is 50, only the column where 50% of the sequences share one amino acid would be kept. 
percentage_homology = 0
# HARD CODED!! Please insert the path to the fasta_file and name of the output 
fasta_file = ''     
text_with_conserved_column_number= ''  

# Parsing the input fasta file to a list. 
def fasta_parser(fasta_file):
    with open(fasta_file, "r") as file:
        sequences = []
        current_sequence = ""
        for line in file:
            if line.startswith(">"):
                if current_sequence:
                    sequences.append(current_sequence)
                current_sequence = ""
            else:
                current_sequence += line.strip()
        if current_sequence:
            sequences.append(current_sequence)
    return sequences


# Determing the columns within the output_csv file that has a higher conservation than the threshold the user defined. All columns where "-" is the most abundant and is over the threshold is removed
def conserved_column_extractor(sequences, output_text):
    output_csv = 'output.csv'
    # writing the sequences into csv where each column contains homologous residue determined from alignments
    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        for seq in sequences:
            writer.writerow(list(seq))
    # reading the csv file       
    with open(output_csv, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    num_columns = len(rows[0])
    matching_columns = []

    for col in range(num_columns):
        column = [row[col] for row in rows]
        # Count occurrences of each character in the column
        counter = Counter(column)
        most_common = counter.most_common(1)[0][1]  # Get count of the most common amino acid
        # Calculate the percentage of the most common amino acid in the column
        percentage = most_common / len(column) * 100
        # Check if '-' is the majority
        dash_count = sum(1 for row in rows if row[col] == '-')
        if dash_count <= len(rows) / 2:  # Ignore columns where '-' is the majority
            if percentage > percentage_homology:
                matching_columns.append(col + 1)  

    # Writing the column number to the 
    with open(output_text, "w") as text_file:
        for col in matching_columns:
            text_file.write(f"{col}\n")


# Stiching all of the function above together
def main(fasta_file, output_text):
    sequences = fasta_parser(fasta_file)
    conserved_column_extractor(sequences, output_text)

# executing the function
main(fasta_file, text_with_conserved_column_number)

# removing the intermediate file
os.remove('output.csv')


