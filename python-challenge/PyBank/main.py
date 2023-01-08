#Import modules os & csv
import os
import csv

#path for the CSV file in PyBankcsv

PyBankcsv = os.path.join("Resources" ,"budget_data.csv")

#Create lists to store data

months = []
profit_loss_changes = []

# Initialize the variables

count_months = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0

#Open the csv file using the path

with open(PyBankcsv) as csv_file :
    csvreader = csv.reader(csv_file, delimiter = ",")

    #Read the header row first
    csvheader = next(csvreader)

    #Read through each row of data after header
    for row in csvreader:

        # Count of months
        count_months = count_months+1 

        # Net total amount of "Profit/Losses" over the entire period
        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss

        if (count_months == 1):
            # Make the value of previous month to be equal to current month
            previous_month_profit_loss = current_month_profit_loss
            continue

        else:

            # Calculate change in profit loss 
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss

            # Append each month to the months[]
            months.append(row[0])

            # Append each profit_loss_change to the profit_loss_changes[]
            profit_loss_changes.append(profit_loss_change)

            # Make the current_month_loss to be previous_month_profit_loss for the next loop
            previous_month_profit_loss = current_month_profit_loss

    #sum and average of the changes in "Profit/Losses" over the entire period
    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss = round(sum_profit_loss/(count_months - 1), 2)

    # highest and lowest changes in "Profit/Losses" over the entire period
    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)

    # Locate the index value of highest and lowest changes in "Profit/Losses" over the entire period
    highest_month_index = profit_loss_changes.index(highest_change)
    lowest_month_index = profit_loss_changes.index(lowest_change)

    # Assign best and worst month
    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]

#Print the analysis in the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count_months}")
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")

#Export a text file with the results

with open("financial_summary.txt", "w") as file:
    file.write("  Financial Analysis"+ "\n")
    file.write("----------------------------------------------------------\n\n")
    file.write("    Total Months: " + str(count_months) + "\n")
    file.write("    Total: " + "$" + str(net_profit_loss) +"\n")
    file.write("    Average Change: " + '$' + str(int(average_profit_loss)) + "\n")
    file.write("    Greatest Increase in Profits: " + str(best_month) + " ($" + str(highest_change) + ")\n")
    file.write("    Greatest Decrease in Profits: " + str(worst_month) + " ($" + str(lowest_change) + ")\n")
    file.write("----------------------------------------------------------\n")
