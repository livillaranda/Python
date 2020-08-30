# Import packages
import os
import csv
from collections import Counter

# Read data file
ed_path = os.path.join("Resources", "election_data.csv")

# Read with CSV functioin
with open(ed_path) as csvfile:
    ed_read = csv.reader(csvfile, delimiter=',')

    # Read Header
    ed_header = next(ed_read)
        
    # Assign Variables
    row_count = 0
    total_votes = 0
    myList = []
    Candidates = list()
    v_percent1 = 0
    v_percent2 = 0
    v_percent3 = 0
    v_percent4 = 0
    c_total1 = 0
    c_total2 = 0
    c_total3 = 0
    c_total4 = 0
    winner = []
       

    # For Loop
    for row in ed_read:
        
        # Count Votes
        row_count += 1
        total_votes = row_count

        # List Candidates [COME BACK TO THIS]
        myList.append(row[2])
        #Candidates = list(dict.fromkeys(myList))

        c_total1 = myList.count("Khan")
        c_total2 = myList.count("Correy")
        c_total3 = myList.count("Li")
        c_total4 = myList.count("O'Tooley")


        # Calculate Vote Percentage
        v_percent1 = (c_total1 / total_votes)
        v_percent2 = (c_total2 / total_votes)
        v_percent3 = (c_total3 / total_votes)
        v_percent4 = (c_total4 / total_votes)

        # Declare Winner
        winner = max(v_percent1, v_percent2, v_percent3, v_percent4)


# Formatting Outputs
v_percent1 = '{:,.3f}%'.format(v_percent1)
v_percent2 = '{:,.3f}%'.format(v_percent2)
v_percent3 = '{:,.3f}%'.format(v_percent3)
v_percent4 = '{:,.3f}%'.format(v_percent4)

# Summary of Analysis
print("Election Results")
print("-" *25)
print("Total Votes: " + str(total_votes))
print("-" *25)
print(str(myList[0]) + ": " + str(v_percent1) + ": " + str(c_total1))
print(myList[1] + ": " + v_percent2 + ": " + c_total2)
print(myList[2] + ": " + v_percent3 + ": " + c_total3)
print(myList[3] + ": " + v_percent4 + ": " + c_total4)
print("-" *25)
print("Winner: " + str(winner))
print("-" * 25)

# Write CSV file output
output_path = os.path.join("Analysis", "Final_Vote.csv")

# Open file in writer mode
with open(output_path, 'w') as csvfile:

    # Start csv.writer
    vote = csv.writer(csvfile)

    # Write Summary into file
    vote.writerow("Election Results")
    vote.writerow("-" *25)
    vote.writerow("Total Votes: " + str(total_votes))
    vote.writerow("-" *25)
    vote.writerow(str(myList[0]) + ": " + str(v_percent1) + ": " + str(c_total1))
    vote.writerow(myList[1] + ": " + v_percent2 + ": " + c_total2)
    vote.writerow(myList[2] + ": " + v_percent3 + ": " + c_total3)
    vote.writerow(myList[3] + ": " + v_percent4 + ": " + c_total4)
    vote.writerow("-" *25)
    vote.writerow("Winner: " + str(winner))
    vote.writerow("-" * 25)