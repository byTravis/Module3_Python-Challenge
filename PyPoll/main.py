import os
import csv

# set file paths
csvPath = os.path.join("Resources", "election_data.csv")
finalReport = os.path.join("analysis", "ElectionResults.txt")

# establish varaibles and default values
totalVotes = 0
candidateTally = []
electionWinner = ["", 0]


with open(csvPath, "r") as electionData:
    csvReader = csv.reader(electionData, delimiter=",")
    csvHeader = next(csvReader, None)

    #loops through CSV and pulls candidatename and vote record.
    for row in csvReader:
        candidateName=row[2]

        #creates list of candidates and their votes in dictionary format
        for entry in candidateTally:
            if entry["name"] == candidateName:  #if candidate is already in candidateTally list, increments their vote by 1
                entry["votes"] += 1
                break
        else:  # if candidate is not in the candidateTally list, it creates a new entry
            newEntry = {"name": candidateName, "votes": 1}
            candidateTally.append(newEntry)

        totalVotes+=1 #counts total votes



# generate final report via terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {totalVotes}")
print("-------------------------")

for each in candidateTally:
    name = each["name"]
    percent = round((each["votes"]/totalVotes)*100, 3)
    votes = each["votes"]

    if votes > electionWinner[1]:
        electionWinner = [name, votes]

    print(f"{name}:  {str(percent)}%  ({str(votes)})")

print("-------------------------")
print(f"Winner:  {electionWinner[0]}")
print("-------------------------")



# generate final report via exported txt report
with open(finalReport, "w") as report:
    report.write("Election Results\n")
    report.write("-------------------------\n")
    report.write(f"Total Votes:  {totalVotes}\n")
    report.write("-------------------------\n")

    for each in candidateTally:
        name = each["name"]
        percent = round((each["votes"]/totalVotes)*100, 3)
        votes = each["votes"]
        report.write(f"{name}:  {str(percent)}%  ({str(votes)})\n")

    report.write("-------------------------\n")
    report.write(f"Winner:  {electionWinner[0]}\n")
    report.write("-------------------------\n")