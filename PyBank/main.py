"""
Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)

"""



import os
import csv

# Import the file and define the name of the file
originalfile = os.path.join(".", "budget_data.csv")
newfile = os.path.join("budget_final.txt")

row_counter = 0
total_sum = 0
avrg_list = []
current_max = 0
month = []
current_min = 0

# 1. The total number of months included in the dataset
# Logic: open the file delimiating the columns by "," and then iterate thru to sum each row in the file
with open(originalfile, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip the header so it isn't counted in Total Months
    next(csvfile)

    for row in csvreader:
        row_counter += 1
        total_sum += int(row[1])

        if int(row[1]) > current_max:
            current_max = int(row[1])
            maxMonth = row[0]

        if int(row[1]) < current_min:
            current_min = int(row[1])
            minMonth = row[0]

        avrg_list.append(row[1])
        avrg_list = [int(z) for z in avrg_list]
    calc = [y -x for x, y in zip(avrg_list, avrg_list[1:])]
    # Import statistics as mean
    from statistics import *
    x = mean(calc)
    minProfit = min(calc)
    maxProfit = max(calc)

# total_months = total month calulation
# total_sum = total sum calculation
# avrg_calc = the average calculation
# max_calc & month = maxMonthProfit
# min_cal & month = minMonthProfit
header = "Financial Analysis:"
seperator = "----------------------------"
total_months = (f"Total Months: {row_counter}")
total_sum = ("Total: ${:,}".format(total_sum))
avrg_calc = (f"Average Change: ${round(x,2)}")
max_month = ("Max Profit: " + maxMonth + " (${:,}".format(maxProfit) + ")")
min_month = ("Min Profit: " + minMonth + " (${:,}".format(minProfit) + ")")

output = (f"\nFinancial Analysis:\n"
          f"----------------------------\n"
          f"{total_months}\n"
          f"{total_sum}\n"
          f"{avrg_calc}\n"
          f"{max_month}\n"
          f"{min_month}\n")
print(output)

# Convert the values to a list and output them into a text file
cleaned_output = [header, seperator, total_sum, avrg_calc, max_month, min_month]
#  Open the output file and assign this as write instead of read
with open(newfile, "w") as cleanfile:
    writer = csv.writer(cleanfile)
    # use a forloop to go through the list you created and add "\n" to create a new row
    for n in cleaned_output:
        cleanfile.write(n + '\n')