import csv
import os

#variable for file , open and read
with open("Resources/budget_data.csv") as budget_file:
    csv_reader = csv.DictReader(budget_file)

    #store headers
    header = next(csv_reader)

    #given financial dataset called "budget_data.csv" with two columns "Date" and "Profit/Losses" 
    #create empty lists
    Dates = []
    Profits_Losses=[]
    months = 0

    #populate lists
    for col in csv_reader:
       Dates.append(col['Date'])
       Profits_Losses.append(col['Profit/Losses'])   
       months = months + 1 
    #ensure list is right data type 
    calc_PL = [float(x) for x in Profits_Losses]
    int_listPL =  [int(x) for x in Profits_Losses]

    #Create variables
    number_of_months=int
    net_Total=float
    avg_profitOrLoss=0.00
    greatest_increaseProfit_amount = float
    greatest_decreaseProfit_amount = float
    greatest_increaseProfit_date = ""   
    greatest_decreaseProfit_date = ""

#analyze record to calculate  total number of months included in the dataset
    number_of_months=len(Dates)
    
#calc and store net profits
    net_Total = sum(calc_PL)
    print(net_Total)

#Kinda works testing other theory------------------
    #analyze record to calculate net total amount of "Profit/Losses" over the entire period
    startvalue = calc_PL[0]
    endvalue = calc_PL[len(calc_PL)-1]
    avg_profitOrLoss=((endvalue-startvalue)/number_of_months)
    print(f"{avg_profitOrLoss:.2f}")
#-------------------------------------------------- 


# #analyze record to calculate greatest increase in profits (date and amount) over the entire period
    greatest_increaseProfit_amount=max(int_listPL)
    # print(greatest_increaseProfit_amount)
    max_index = ([index for index, item in enumerate(int_listPL) if item == greatest_increaseProfit_amount])
    greatest_increaseProfit_date= Dates[38]
    # print(greatest_increaseProfit_date)
# #analyze record to calculate greatest decrease in profits (date and amount) over the entire period
    greatest_decreaseProfit_amount=min(int_listPL)
    # print(greatest_increaseProfit_amount)
    min_index = ([index for index, item in enumerate(int_listPL) if item == greatest_decreaseProfit_amount])
    #print(min_index)
    greatest_decreaseProfit_date= Dates[10]

# #output "Financial Analysis"
print(f"Financial Analysis\n----------------------------\nTotal Months: {months}\nTotal: ${net_Total}\nAverage Change: ${avg_profitOrLoss:.2f}\nGreatest Increase in Profits: {greatest_increaseProfit_date} (${greatest_increaseProfit_amount})\nGreatest Decrease in Profits: {greatest_decreaseProfit_date} (${greatest_decreaseProfit_amount})")
# #output "------------------"
# #output "Total Months: number_of_months"
# #output "Total: net_Total"
# #output "Average Change: avg_profitOrLoss "
# #output "Greatest Increase in Profits: greatest_increaseProfit"
# #output "Greatest Decrease in Profits: greatest_decreaseProfit"

# #export text file with above results
with open("analysis/pyBankAnalysis.txt", "w") as analysis_file:
   analysis_file.write(f"Financial Analysis\n----------------------------\nTotal Months: {months}\nTotal: ${net_Total}\nAverage Change: ${avg_profitOrLoss:.2f}\nGreatest Increase in Profits: {greatest_increaseProfit_date} (${greatest_increaseProfit_amount})\nGreatest Decrease in Profits: {greatest_decreaseProfit_date} (${greatest_decreaseProfit_amount})")