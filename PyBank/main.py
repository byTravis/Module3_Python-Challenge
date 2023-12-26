import os
import csv

# set file paths
csvPath = os.path.join("Resources", "budget_data.csv")
finalReport = os.path.join("analysis", "BudgetData_FinancialAnalysis.txt")

# establish varaibles and default values
monthCount = 0
totalProfitLoss = 0
averageChange = 0
greatestIncrease = ["", 0]
greatestDecrease = ["", 0]

prevTotal = 0
currentTotal = 0
monthlyDifference = []


# iterate through CSV and calculate values
with open(csvPath, 'r') as budgetCSV:
    csvReader = csv.reader(budgetCSV, delimiter=",")
    csvHeader = next(csvReader)

    for row in csvReader:
        currentTotal= int(row[1])
        if prevTotal != 0:  
            monthlyDifference.append(currentTotal - prevTotal)           
            #updates greatest increase/decrease
            if currentTotal - prevTotal > greatestIncrease[1]:  #updates greatest increase
                greatestIncrease = [row[0], currentTotal - prevTotal]
            elif currentTotal - prevTotal < greatestDecrease[1]:  #updates greatest decrease
                greatestDecrease = [row[0], (currentTotal - prevTotal)]

            prevTotal = currentTotal  #sets previos total to currennt total for next loop

        else:      #sets initial values on the first row of data      
            prevTotal = currentTotal  #first record has no previous record and will always be current total

        monthCount +=1
        totalProfitLoss += int(row[1])  #running total for total profit/loss

# calculates average monthly change
for change in monthlyDifference:
    averageChange +=change
averageChange= averageChange/len(monthlyDifference)

# generate final report via terminal
print("Financial Analysis")
print("----------------------------")
print (f"Total Months:  {monthCount}")
print(f"Total:  ${totalProfitLoss}")
print(f"Average Change:  ${str(round(averageChange, 2))}")
print(f"Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]})")
print(f"Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]})")

# generate final report via exported txt report
with open(finalReport, "w") as report:
    report.write("Financial Analysis \n")
    report.write("----------------------------\n")
    report.write (f"Total Months:  {monthCount}\n")
    report.write(f"Total:  ${totalProfitLoss}\n")
    report.write(f"Average Change:  ${str(round(averageChange, 2))}\n")
    report.write(f"Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]})\n")
    report.write(f"Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]})\n")



