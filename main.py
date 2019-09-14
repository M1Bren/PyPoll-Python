# Import the relevant dependencies
import os
import csv

# Signal the path to reach the election data in the same folder
csvpath = os.path.join("election_data.csv")

# Open the csvpath with proper notation and delimitation
with open(csvpath, newline='') as csvfile:  
    csvreader = csv.reader(csvfile, delimiter=',')
    # Make csvheader the row list for the header
    csvheader = next(csvreader)

    # Define the relevant variables based on candidates in election
    Kcount = 0
    Ccount = 0
    Lcount = 0
    Ocount = 0
    Tcount = 0

    # Go through every row in csvreader (the file) completing the instructed calculations
    for row in csvreader:
        Tcount += 1
        if row[2] == "Khan":
            Kcount += 1
        elif row[2] == "Correy":
            Ccount += 1
        elif row[2] == "Li":
            Lcount += 1
        elif row[2] == "O'Tooley":
            Ocount += 1

# Calculate percentages based on data collected from file
Kper = str(round((Kcount / Tcount)*100, 3)) + "%"
Cper = str(round((Ccount / Tcount)*100, 3)) + "%"
Lper = str(round((Lcount / Tcount)*100, 3)) + "%"
Oper = str(round((Ocount / Tcount)*100, 3)) + "%"

# Calculate the winner based on highest vote count
Candidates = {Kcount: "Khan", Ccount: "Correy", Lcount: "Li", Ocount: "O'Tooley"}
Winner = max([Kcount, Ccount, Lcount, Ocount])

# Print the results
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {Tcount}")
print(f"-------------------------")
print(f"Khan: {Kper} ({Kcount})")
print(f"Correy: {Cper} ({Kcount})")
print(f"Li: {Lper} ({Lcount})")
print(f"O'Tooley: {Oper} ({Ocount})")
print(f"-------------------------")
print(f"Winner: {Candidates[Winner]}")

# Write the file with the values calculated
output_file = os.path.join("pypoll_final.csv")
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow([f"Election Results"])
    writer.writerow([f"-------------------------"])
    writer.writerow([f"Total Votes: {Tcount}"])
    writer.writerow([f"-------------------------"])
    writer.writerow([f"Khan: {Kper} ({Kcount})"])
    writer.writerow([f"Correy: {Cper} ({Kcount})"])
    writer.writerow([f"Li: {Lper} ({Lcount})"])
    writer.writerow([f"O'Tooley: {Oper} ({Ocount})"])
    writer.writerow([f"-------------------------"])
    writer.writerow([f"Winner: {Candidates[Winner]}"])
