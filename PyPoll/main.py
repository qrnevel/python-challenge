
# Import dependencies
import os
import csv
import collections
from collections import Counter

#Define PyPoll's variables
voters_cands = []
votes_per_cand = []

#Change directory to the directory of current python script
os.chdir(os.path.dirname(__file__))

#Path to collect data from the Resources folder
election_data_csv = os.path.join("Resources", "election_data.csv")

#Open and read csv
with open(election_data_csv, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    #Read the header row first
    csv_header = next(csvfile)

    #print(f"Header: {csv_header}")
    #This prints -->> Header: Voter ID,Country,Candidate
    #Read through each row of data after the header
    for row in csv_reader:

        voters_cands.append(row[2])

    #Sort the list by default ascending order
    sorted_list = sorted(voters_cands)

    #sorted_list = sorted(voters_candidates, reverse=True) 
    #sorted_list.sort(reverse=True) 

    #for key, group in groupby(sorted_list):
    
    #Arrange the sorted list by most common outcomes
    arrange_list = sorted_list

    #count votes per candidate in most common outcome order and append to a list
    count_cand = Counter (arrange_list) 
    votes_per_cand.append(count_cand.most_common())

    #calculate the % of votes per candicate in 3 digital points
    for item in votes_per_cand:
       
        first = format((item[0][1])*100/(sum(count_cand.values())),'.3f')
        second = format((item[1][1])*100/(sum(count_cand.values())),'.3f')
        third = format((item[2][1])*100/(sum(count_cand.values())),'.3f')
        fourth = format((item[3][1])*100/(sum(count_cand.values())),'.3f')
          
    #print(c.most_common())
    #print(c.values())
    #print(c.keys())
    #print(sum(c.values()))
    
#Print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {sum(count_cand.values())}")
print("-------------------------")
print(f"{votes_per_cand[0][0][0]}: {first}% ({votes_per_cand[0][0][1]})")
print(f"{votes_per_cand[0][1][0]}: {second}% ({votes_per_cand[0][1][1]})")
print(f"{votes_per_cand[0][2][0]}: {third}% ({votes_per_cand[0][2][1]})")
print(f"{votes_per_cand[0][3][0]}: {fourth}% ({votes_per_cand[0][3][1]})")
print("-------------------------")
print(f"Winner:  {votes_per_cand[0][0][0]}")
print("-------------------------")


#Export a text file with the results
election_file = os.path.join("analysis", "election_data.txt")
with open(election_file, "w") as output:

    output.write("Election Results\n")
    output.write("-------------------------\n")
    output.write(f"Total Votes:  {sum(count_cand.values())}\n")
    output.write("-------------------------\n")
    output.write(f"{votes_per_cand[0][0][0]}: {first}% ({votes_per_cand[0][0][1]})\n")
    output.write(f"{votes_per_cand[0][1][0]}: {second}% ({votes_per_cand[0][1][1]})\n")
    output.write(f"{votes_per_cand[0][2][0]}: {third}% ({votes_per_cand[0][2][1]})\n")
    output.write(f"{votes_per_cand[0][3][0]}: {fourth}% ({votes_per_cand[0][3][1]})\n")
    output.write("-------------------------\n")
    output.write(f"Winner: {votes_per_cand[0][0][0]}\n")
    output.write("-------------------------\n")    