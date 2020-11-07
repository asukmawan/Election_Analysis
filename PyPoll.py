
# What is the total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate won
# What is the percentage of votes each candidate won
# Who is the winner of the election

# Import dependencies
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Set accumulator variables to zero
total_votes = 0
# Declare list for candidate names
candidate_options = []
# Open the election results and read the file.
with open(file_to_load) as election_data:
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
# Reading the header row using the next() function
    headers = next(file_reader)
# Go through each row in the CSV file    
    for row in file_reader:
    # Add to the total vote count
        total_votes += 1
    # Print the candidate name from each row
        candidate_name = row[2]
    # Add candidate name to the candidate list - only if its not already on the list
        if candidate_name not in candidate_options:  
            candidate_options.append(candidate_name)
# Print the total votes
print(total_votes)
print(candidate_options)    


