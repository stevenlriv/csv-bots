import csv
import random

# Reads a CSV file and returns an array of the rows
# Need to provode: file path
def read_csv(file_path):
    rows = []
    
    # Open the CSV file
    with open(file_path, 'r') as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)

        # Read the header row
        header = next(csv_reader)
        
        # Iterate over each row in the CSV file
        for row in csv_reader:
            rows.append(row)
    
    return header, rows

# Returns a random line from a text file
# Need to provode: file path
def read_random_line(file_path):
    # Open the file
    with open(file_path, "r") as file:
        lines = file.readlines()

    # Choose a random lime from the file
    random_line = random.choice(lines).strip()
    
    return random_line