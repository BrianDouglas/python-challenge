import os
import csv

#prep the data file and load it into a list of tuples
budget_path = os.path.join("resources","budget_data.csv")
budget_data = []

with open(budget_path) as budget_file:
    budget_reader = csv.reader(budget_file, delimiter = ",")
    #discard header
    next(budget_reader)

    for row in budget_reader:
        budget_data.append((row[0], int(row[1])))

#initialize tabulation variables    
total_months = len(budget_data)
total_monies = budget_data[0][1]
changes = []
greatest_increase = [budget_data[0][0], 0]
greatest_decrease = [budget_data[0][0], 0]

#loop through remaining data
for i in range(1,len(budget_data)):
    #sum our money
    total_monies += budget_data[i][1]
    #append to list of changes
    changes.append(budget_data[i][1] -  budget_data[i-1][1])
    #check for possible change in greatest increase/decrease
    if changes[i-1] > greatest_increase[1]:
        greatest_increase[0] = budget_data[i][0]
        greatest_increase[1] = changes[i-1]
    if changes[i-1] < greatest_decrease[1]:
        greatest_decrease[0] = budget_data[i][0]
        greatest_decrease[1] = changes[i-1]

#output    
print("Financial Analysis")
print("-------------------------------")
print(f"Total Months: {total_months}")
print("Total: ${:,}".format(total_monies))
print("Average Change: ${:,.2f}".format(sum(changes)/len(changes)))
print("Greatest Increase in Profits: {} (${:,})".format(greatest_increase[0], greatest_increase[1]))
print("Greatest Decrease in Profits: {} (${:,})".format(greatest_decrease[0], greatest_decrease[1]))

output_path = os.path.join("analysis", "output.txt")
f = open(output_path, "w")

f.write("Financial Analysis\r")
f.write("-------------------------------\r")
f.write(f"Total Months: {total_months}\r")
f.write("Total: ${:,}\r".format(total_monies))
f.write("Average Change: ${:,.2f}\r".format(sum(changes)/len(changes)))
f.write("Greatest Increase in Profits: {} (${:,})\r".format(greatest_increase[0], greatest_increase[1]))
f.write("Greatest Decrease in Profits: {} (${:,})".format(greatest_decrease[0], greatest_decrease[1]))

f.close()