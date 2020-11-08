# Colorado Congressional Election Analysis
## Project Overview 
A Colorado Board of Elections employee has requested the following tasks to be done to complete the election audit of a recent local congressional election.
1. Calculate the total number of votes cast. 
2. Get a complete list of each county and its total vote and percentage of votes.
3. Determine the county with the highest turnout
4. Get a complete list of candidates who received votes and calculate the total number of votes, and their percentage of total votes each candidate received. 
4. Determine the winner of the election based on popular vote.

## Resources 
- Data Source: [election_results.csv](Resources/election_results.csv)
- Software: Python 3.7.6, Visual Studio Code, 1.51.0

## Summary 
The analysis of the election show that: 
- There were "369,711" votes cast in the election. 
- Votes by county:
    - Jefferson had a turnout of 38,855 votes cast, 10.5% of total votes in the precinct.
    - Denver had a turnout of 306,055 votes cast, 73.8% of the total votes in the precinct.
    - Arapahoe had a turnout of 24,801 votes cast, 3.1% of the total votes in the precinct.
- Denver had the largest number of votes cast in this congressional election

- The candidate results were:
    - Charles Casper Stockham received "23.0%" of the vote and "85,213" number of votes. 
    - Diana DeGette received "73.8%" of the vote and "272,892" number of votes.
    - Raymon Anthony Doane received "3.1%" of the vote and "11,606" number of votes. 
- The winner of the election was:
    - Diana DeGette, who received "73.8%" of the vote and "272,892" number of votes.

The election results summary can be found saved in the [election_results.txt](analysis/election_analysis.net)

    <img src="Resources/election_results.png></img>
## Challenge Overview

The purpose of the election analysis audit was to write a script to deliver the following information:
1. To find the total number of votes cast, a for loop with an accumulator variable was used to increase the variable incrementally as the loop goes through each row in the csv file

        for row in reader:
            total_votes = total_votes + 1

2. A complete list of candidates who received votes:
    - using a list, we will store the candidate name with a conditional that its is 'not in' the list already. and have this nested in the for loop we created earlier
3. Total number of votes each candidate received
    - using a dictionary, we store the amount of votes each candidate received as we go through the for loop
        - to do this we have to create a key for each unique candidate
        - first we have to set each candidate vote count to 0 whenever we encounter a new candidate - do this in the if conditional when it encounters a new candidate
        - back outside of the if conditional and in the for loop, we want to have an incremental for the candidate vote dictionary for the correct candidate key

                use candidate_votes[candidate_name] += 1

4. Percentage of votes each candidate won
    - we need to divide the candidate's vote count by the total vote count and multiply by 100
    - equation:

            vote_percentage = (vote/total_votes)  * 100

    - But before we can calculate it, our current counts are in integers and we won't be able to get a percentage answer unless we change them to floating-point decimal numbers
    - change candidate_votes and total_votes to floating-point before we calculate percentage
5. The winner of the election based on popular vote
    - we can see if who the winner is just by looking at the result, but for the script to determine the winner we can use an if statement to check each candidate vote count and compare it to the next candidate and do a check if its higher than the current highest candidate
    - use an if statement first to check if the current candidate in the candidate_votes dictionary its greater than zero, if it is store their vote count and vote percentage as the winning count and percentage

## Challenge Summary

This analysis could have been just as easily done using Microsoft Excel. The .csv format is easily formatted to be readable without data loss, and analysis could have been done in a pivot table to find out total votes, percentages for each candidate and county. 

But the the benefit in using Python to do this analysis, is that this script can be used with any election just so long as the .csv file holds the same format of ballot ID, County and Candidate. 

While this can be an issue when handling many different precincts which may not follow the same format of .csv as Colorado, we can modify the script to handle the different format by utilizing the `input()` function. The problem with the current script is that we have county names assigned to the 2nd column in each row, and candidate names in the 3rd. If we ask the user that is running the script to specify which column each heading is under, the script will be able to adapt to any election.

For example we can use the following input:

        candidate_column = int(input("Which number column contains the candidate's name?"))
We then can use the variable as an index to get the candidate's name from each row in our for loop:

        for row in reader:
            candidate_name = row[candidate_column]

Regardless of how many different candidates and counties there are, the script will take all of them into account and create lists and dictionaries and determine total votes and percentages for all of them. This is done because of the following conditional:

        if county_name not in counties_list:

            # Add the existing county to the list of counties.
            counties_list.append(county_name)

            # Begin tracking the county's vote count.
            county_votes[county_name] = 0

    # Add a vote to that county's vote count.
        county_votes[county_name] += 1

This is also done with candidate's names, just so long as the script encounters a new name or county, it will add to the number of votes for that county or candidate.