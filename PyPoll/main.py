import os
import csv

# set file paths
csvPath = os.path.join("Resources", "election_data.csv")


totalVotes = 0
candidateTally = []
electionWinner = ["", 0]



with open(csvPath, "r") as electionData:
    csvReader = csv.reader(electionData, delimiter=",")
    csvHeader = next(csvReader, None)

    for row in csvReader:
        candidateName=row[2]

        #creates list of candidates and their votes

        for entry in candidateTally:
            if entry["name"] == candidateName:  #if candidate is already in candidateTally list, increments their vote by 1
                entry["votes"] += 1
                break
        else:  # if candidate is not in the list, it creates an entry for candidateTally
            newEntry = {"name": candidateName, "votes": 1}
            candidateTally.append(newEntry)

        totalVotes+=1


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

