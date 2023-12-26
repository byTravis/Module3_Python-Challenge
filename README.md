# Python Challenge
Week 3 - Data Analytics Boot Camp - University of Oregon

![PyBank Challenge](/Images/revenue-per-lead.png)
## PyBank Challenge
### Objective:
You are tasked with creating a Python script to analyze the financial records of your company.

### Instructions
Your task is to create a Python script that analyzes the records to calculate each of the following values:
* The total number of months included in the dataset.
* The net total amount of "Profit/Losses" over the entire period.
* The changes in "Profit/Losses" over the entire period, and then the average of those changes.
* The greatest increase in profits (date and amount) over the entire period.
* The greatest decrease in profits (date and amount) over the entire period.
* Display a report in the terminal.
* Export a report as txt file to the Analysis folder.

### Approach
I iterated through each row of the provided CSV to create a list of differences between the current month and the previous month.  This will be used to calculate the average monthly difference.  I also checked to see if the current record qualifies for the greatest increase or decrease.  If so, I updated the value to reflect the current record’s values.  I also updated the total Profit/Loss, as this is a running total.
Once all the rows have been accounted for, I found the average monthly difference by adding up differences between months and dividing by the number of differences recorded.
I output the report in the terminal, as well as an exported report in txt format.

### Results
![PyBank Challenge Report](/Images/FinancialAnalysisResults.JPG)



---



![PyPoll Challenge](/Images/Vote_counting.png)
## PyPoll Challenge
### Objective:
You are tasked with helping a small, rural town modernize its vote-counting process.

### Instructions
Your task is to create a Python script that analyzes the votes and calculates each of the following values:
* The total number of votes cast
* A complete list of candidates who received votes
* The percentage of votes each candidate won
* The total number of votes each candidate won
* The winner of the election based on popular vote
* Display the election results in the terminal.
* Export the election results as txt file to the Analysis folder.

### Approach
I iterated through each row of the provided CSV to create a list of unique candidates and their vote count.  To make things easier to read, I chose to make the list in a dictionary format, so I can call the value by name, rather than position.  Since I only wanted each candidate to be only listed once, I checked to see if they were already present in the list.  If they were, I recorded their vote by increasing their vote by one.  If they were not in the list, we created a new entry with their starting vote count as 1.  I also increased the total number of votes by one.  All candidate’s votes should add up to the total number of votes for quality assurance.
I created a report of the election results for display in terminal.  I looped through the list of candidates and displayed the number of votes they received.  I also compared each candidate to the current leader of the election.  If their votes are higher, we updated the election winner to reflect the new candidate.  I also exported the report in txt format for easy reference.


### Results
![PyPoll Challenge Report](/Images/ElectionResults.JPG)



