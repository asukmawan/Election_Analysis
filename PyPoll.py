
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
# Declare dictionary to store the candidate votes
candidate_votes = {}
# Declare a variable that will hold the empty string for the winning candidate
winning_candidate = ""
# Declare a variable for the winning count equal to zero
winning_count = 0
# Declare a variable for the winning percentage equal to zero
winning_percentage = 0
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
            # start of tracking the new candidate vote
            candidate_votes[candidate_name] = 0
        # add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
#Determine the percentage of votes for each candidate by looping through the counts.
#1. Iterate through the candidate list
for candidate_name in candidate_votes:
    #2. Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    #3. Calculate the percentage of votes
    vote_percentage = float(votes)/float(total_votes) * 100
    #4. Print the candidate name and percentage of votes.
    print(f"{candidate_name} received {vote_percentage:.1f}% of the vote.")
# Determine the winner

# Print the total votes
print(total_votes)
print(candidate_options)    
print(candidate_votes)


