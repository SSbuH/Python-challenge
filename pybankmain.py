from email.header import Header
import os
import csv

# Path to collect data from the Resources folder
pybank_csvpath = os.path.join('..', 'Resources', 'budget_data.csv')


# Assigning and identifying variables
total_months = 0
total_prolos = 0
changes =[]
date_count = []
greatest_incr = 0
greatest_incr_month = 0
greatest_decr = 0
greatest_decr_month = 0

# Open the csv
with open(pybank_csvpath, newline = '') as csvfile:
    csvreader =csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)
    row = next(csvreader)

#analysis of data by calculation of total number of months and total revenue (profit/loss)
    intial_profit = int(row[1]) 
    total_months = total_months + 1
    total_prolos = total_prolos + int(row[1])
    greatest_incr = int(row[1])
    greatest_incr_month = row[0]

    for row in csvreader:
        total_months = total_months + 1
        total_prolos = total_prolos + int(row[1])

    # Calculating changes in profit/losses from month to month
    change = int(row[1]) - initial_profit
    changes.append(cahnge)
    initial_profit = int(row[1])
    date_count.append(row[0])

    # Calculating increase in profit (date and amount) from month to month
    if int(row[1]) > greatest_incr:
        greatest_incr = int(row[1])
        greatest_incr_month = row[0]

    # Calculating decrease in profit (date and amount) from month to month
    if int(row[1]) < greatest_decr:
        greatest_decr = int(row[1])
        greatest_decr_month = row[0]

# Calculating the average for profit/losses changes month to month
average_change = sum(changes)/len(changes)

highest = max(changes)
lowest = min(changes)

# Print out the Financial Analysis and information on pybank file
print("Financial Analysis")
print("Total Months:" + str(total_months))
print("Total Amount:" + str(total_prolos))
print(average_change)
print(greatest_incr_month, max(changes))
print(greatest_decr_month, min(changes))

Header
 # writing output files as a text file

PyBank = open("output.txt","w+")
PyBank.write("Financial Analysis")
PyBank.write('\n' + "Total Months" + str(total_months))
PyBank.write('\n' + "Total Amount" + str(total_prolos))
PyBank.write('\n' + "Average Change" + str(average_change))
PyBank.write('\n' + greatest_incr_month)
PyBank.write('\n' + str(highest)) 
PyBank.write('\n' + greatest_decr_month) 
PyBank.write('\n' + str(lowest))