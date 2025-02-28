# This python script takes the output auxillary text from cst_alignment_homology_getter.py and generate a cds_auxillary file to get the corresponding codons of the conserved columns of the amino acid alignment.

# HARD CODED. Please input the name of the output amino acid auxillary file from cst_alignment_homology_getter.py as input.
amino_acid_column_number_text = ""  
nucleotide_column_number_text = ""  


def cds_auxillary_generator(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    
    with open(output_file, 'w') as output:
        for line in lines:
            line = line.strip()

            num = int(line)  # Try converting to an integer

            num_times_3 = num * 3
            # the number of column in amino acid *3 will be the column number of the last nucleotide of the corresponding codon
            # Therefore, we write the column number of column in amino acid *3 , (column in amino acid *3)-1, and (column in amino acid *3)-2
            output.write(f"{num_times_3 - 2}\tkeep\n")
            output.write(f"{num_times_3 - 1}\tkeep\n")
            output.write(f"{num_times_3}\tkeep\n")


cds_auxillary_generator(amino_acid_column_number_text, nucleotide_column_number_text)


