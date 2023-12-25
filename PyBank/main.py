import os
import csv

csvPath = os.path.join("Resources", "budget_data.csv")

monthCount = 0
totalProfitLoss = 0
averageChange = 0
greatestIncrease = ["", 0]
greatestDecrease = ["", 0]

prevTotal = 0
currentTotal = 0
monthlyDifference = []
change = 0



with open(csvPath, 'r') as budgetCSV:
    csvReader = csv.reader(budgetCSV, delimiter=",")
    csvHeader = next(csvReader)
    print(csvHeader)

    for row in csvReader:
        currentTotal= int(row[1])
        if prevTotal != 0:
            monthlyDifference.append(currentTotal - prevTotal)
            change=change+(currentTotal - prevTotal)
            
            #updates greatest increase/decrease
            if currentTotal - prevTotal > greatestIncrease[1]:
                greatestIncrease = [row[0], currentTotal - prevTotal]
            elif currentTotal - prevTotal < greatestDecrease[1]:
                greatestDecrease = [row[0], (currentTotal - prevTotal)]

            



            prevTotal = int(row[1])

        else:      #sets initial values on the first row of data      
            prevTotal = int(row[1])



        monthCount +=1
        totalProfitLoss += int(row[1])



# generate final report
print("Financial Analysis")
print("----------------------------")
print (f"Total Months:  {monthCount}")
print(f"Total:  ${totalProfitLoss}")
print(f"Average Change:  $" + str(round(change/(monthCount-1), 2)))
print(f"Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]})")
print(f"Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]})")


