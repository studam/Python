# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 16:11:16 2022

@author: Asus
"""

#import libraries
import csv
import os

#upload file
file_to_load = os.path.join("election_data.csv")
file_to_output = ("Analysis/election_analysis")

#reader to read data from file #read data without header
with open(file_to_load) as data:
    reader = csv.reader(data)
    header = next(reader)
    
# candidates
    candidate_options = []
    
    #vote counters
    candidate_votes = {}
    
    # winning candidate
    winning_candidate = ""
    winning_count = 0
    
    #total votes
    
    total_votes = 0
    
     # for loop
    for row in reader:
            
        
            
    
           # count total votes
            total_votes = total_votes + 1
    
            # candidate name
            candidate_name = row[2]
    
            
            if candidate_name not in candidate_options:
    
                # add to the list of candidates
                candidate_options.append(candidate_name)
    
                # begin voter count
                candidate_votes[candidate_name] = 0
    
            # candidate's count
            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# results in text file
with open(file_to_output, "w") as txt_file:
    
    

    # final vote count 
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # write vote count to the file
    txt_file.write(election_results)

    # loop for winner
    for candidate in candidate_votes:

        # vote count with percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # winning vote and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # print voter count and percentage 
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # voter count and percentage to the file
        txt_file.write(voter_output)

    # winning candidate 
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # winning candidate's name to the file
    txt_file.write(winning_candidate_summary)



