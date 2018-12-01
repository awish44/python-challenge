""""
Should look like this:
Election Results
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------
"""

import csv
import os

# Files to load and output
originalfile = os.path.join(".", "election_data.csv")
newfile = os.path.join(".", "election_analysis.txt")

# Read the csv and convert it into a list of dictionaries
with open(originalfile,"r") as election_data:
    reader = csv.reader(election_data)
    next(election_data)

    # Create a dictionary that pulls candidates names and counts how many votes
    # QUESTION: why is the last key of my dictionary printing in double quotes??
    name = {}
    for row in reader:
        VoterID, County, Candidate = row
        name[Candidate] = name.get(Candidate, 0) + 1

# By leveraging the dictionary keys and values, calculate the sum and % TTL
v = name.values()
total = sum(name.values())
p = [value * 100.00 / total for value in v]

pnumber = [int(x) for x in p]

max_votes = max(name.values())
max_candidate = [k for k, v in name.items() if v == max_votes]

# Build the variables for the output
header = "Election Results"
divider = "-----------------------"
totalVotes = (f"Total Votes: {total}")
winner = (f"Winner: {max_candidate[0]}")

C1 = (f"{list(name.keys())[0]}: {pnumber[0]}.000% ({list(name.values())[0]})")
C2 = (f"{list(name.keys())[1]}: {pnumber[1]}.000% ({list(name.values())[1]})")
C3 = (f"{list(name.keys())[2]}: {pnumber[2]}.000% ({list(name.values())[2]})")
C4 = (f"{list(name.keys())[3]}: {pnumber[3]}.000% ({list(name.values())[3]})")

output = (f"\n{header}\n"
          f"{divider}\n"
          f"{totalVotes}\n"
          f"{divider}\n"
          f"{C1}\n"
          f"{C2}\n"
          f"{C3}\n"
          f"{C4}\n"
          f"{divider}\n"
          f"{winner}\n")
print(output)

# Convert the values to a list and output them into a text file
cleaned_output = [header, divider, totalVotes, divider, C1, C2, C3, C4, divider, winner]
#  Open the output file and assign this as write instead of read
with open(newfile, "w") as cleanfile:
    writer = csv.writer(cleanfile)
    # use a forloop to go through the list you created and add "\n" to create a new row
    for n in cleaned_output:
        cleanfile.write(n + '\n')

# Print a dictionary keys/values in a column
#print('\n'.join("{}: {}".format(k, v) for k, v in name.items()))