
#Import Dependencies
import os
import csv

#path for the CSV file in PyPollcsv

PyPollcsv = os.path.join("Resources", "election_data.csv")

#Create a lists to store and initialize data

count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

#Open and read the csv using the path

with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    # Conduct the ask
    for row in csvreader:

        # Count the total number of votes
        count = count + 1
        
        # Set the candidate names to candidate list
        candidatelist.append(row[2])
        
    # Create a set from the candidate list to get the unique candidate names
    for x in set(candidatelist):
        unique_candidate.append(x)
        
        # y is the total number of votes per candidate
        y = candidatelist.count(x)
        vote_count.append(y)
        
        # z is the percent of total votes per candidate
        z = (y/count)*100
        vote_percent.append(z)
        
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]

# Print to terminal
 
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(round(vote_percent[i], 3)) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

#Export a text file with the results

with open("election_summary.txt", "w") as file:
    file.write("Election Results\n")
    file.write("---------------------------------------\n")
    file.write("Total Votes: " + str(count) + "\n")
    file.write("---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
        file.write(unique_candidate[i] + ": " + str(round(vote_percent[i], 3)) +"% (" + str(vote_count[i]) + ")\n")
    file.write("---------------------------------------\n")
    file.write("Winner: " + winner + "\n")
    file.write("---------------------------------------\n") 