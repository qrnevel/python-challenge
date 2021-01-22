#Import dependencies
import os
import csv

#Define variables
months = []
profit_loss = []

count_months = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss = 0


#Change directory to the directory of current python script
os.chdir(os.path.dirname(__file__))

#Path to collect data from the Resources folder
budget_data_csv_path = os.path.join("Resources", "budget_data.csv")


# Open and read csv
with open(budget_data_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)

    #print(f"Header: {csv_header}")
    #This prints -->> Header: Date, Profit/Losses
             
    #Read through each row of data after the header
    for row in csv_reader:

        #Count of months
        count_months += 1

        #Net total amount of "Profit/Losses" over the entire period
        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss

        if (count_months == 1):
            # Make the value of previous month to be equal to current month
            previous_month_profit_loss = current_month_profit_loss
            continue

        else:

            #Compute change in profit loss 
            profit_loss = current_month_profit_loss - previous_month_profit_loss

            #Append each month to the months[]
            months.append(row[0])

            #Append each profit_loss_change to the profit_loss_changes[]
            profit_loss.append(profit_loss)

            #Make the current_month_loss to be previous_month_profit_loss for the next loop
            previous_month_profit_loss = current_month_profit_loss

    #sum and average of the changes in "Profit/Losses" over the entire period
    sum_profit_loss = sum(profit_loss)
    average_profit_loss = round(sum_profit_loss/(count_months - 1), 2)

    # highest and lowest changes in "Profit/Losses" over the entire period
    highest_change = max(profit_loss)
    lowest_change = min(profit_loss)

    # Locate the index value of highest and lowest changes in "Profit/Losses" over the entire period
    highest_month_index = profit_loss.index(highest_change)
    lowest_month_index = profit_loss.index(lowest_change)

    # Assign best and worst month
    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]

#Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count_months}")
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")


#Export a text file with the results
budget_file = os.path.join("analysis", "budget_data.txt")
with open(budget_file, "w") as output:

    output.write("Financial Analysis\n")
    output.write("----------------------------\n")
    output.write(f"Total Months:  {count_months}\n")
    output.write(f"Total:  ${net_profit_loss}\n")
    output.write(f"Average Change:  ${average_profit_loss}\n")
    output.write(f"Greatest Increase in Profits:  {best_month} (${highest_change})\n")
    output.write(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})\n")