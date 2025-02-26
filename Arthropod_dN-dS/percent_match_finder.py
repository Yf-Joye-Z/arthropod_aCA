import csv
from collections import Counter

def parse_fasta(fasta_file):
    """
    Parse the FASTA file and return the sequences in a list.
    """
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

def write_csv(sequences, output_csv):
    """
    Convert the sequences to a CSV file where each row is one amino acid sequence.
    """
    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        for seq in sequences:
            writer.writerow(list(seq))

def compare_columns(csv_file, output_text):
    """
    Compare columns in the CSV and find columns where more than 60% of the letters are the same (including '-').
    Ignore columns where '-' is the majority. Write the column numbers to a text file.
    """
    with open(csv_file, mode='r') as file:
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
            if percentage > 50:
                matching_columns.append(col + 1)  # Store column number (1-indexed)

    # Write the matching column numbers to the output text file
    with open(output_text, "w") as text_file:
        for col in matching_columns:
            text_file.write(f"{col}\n")

def main(fasta_file, output_csv, output_text):
    # Step 1: Parse the FASTA file to get sequences
    sequences = parse_fasta(fasta_file)
    
    # Step 2: Write sequences to a CSV file
    write_csv(sequences, output_csv)
    
    # Step 3: Compare the columns and find matching ones
    compare_columns(output_csv, output_text)

# Usage example
fasta_file = 'MAFFT_CARP_arthropod-chordate_aCA_aa.fasta'  # Replace with your FASTA file path
output_csv = 'MAFFT_CARP_arthropod-chordate_aCA_aa.csv'    # Output CSV file
output_text = 'AA_auxillary_2.txt'  # Output text file with matching column numbers

main(fasta_file, output_csv, output_text)

print(f"Matching column numbers have been written to: {output_text}")
