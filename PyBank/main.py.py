import os
import csv
path= "c:/Users/khinh/Documents/activity/pythondata/test/Assignment/Solved/Resources"
budget_data = os.path.join(path,"budget_data.csv")

Output_file = os.path.join(path, "budget_analysis.txt")

#Set variable
total_months = 0
previous_profitloss= 0
month_change = []
ProfitLoss_change_List = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_profitloss = 0

# Open and read
with open(budget_data) as profitloss_data:
     csv_reader = csv.reader(profitloss_data)
     header = next(csv_reader)

     for row in csv_reader:
          
          # Total number of the months
          total_months = total_months+1
          total_profitloss = total_profitloss + int(row[1])

          # Profit and Loss Change
          ProfitLoss_change = int(row[1]) - previous_profitloss
          previous_profitloss = int(row[1])
          ProfitLoss_change_List = ProfitLoss_change_List + [ProfitLoss_change]
          month_change = month_change + [row[1]]

       
          #Greatest increase in profits
          if (ProfitLoss_change > greatest_increase[1]):
               greatest_increase[0] = row[0]
               greatest_increase[1] = ProfitLoss_change

          #Greatest decrease in profits
          if (ProfitLoss_change < greatest_decrease[1]):
               greatest_decrease[0] = row[0]
               greatest_decrease[1] = ProfitLoss_change

#Profit and Loss Changes in average
ProfitLoss_change_avg = sum(ProfitLoss_change_List) / len(ProfitLoss_change_List)

#Analysis Output 
Output = (
     f"\nFinancial Analysis\n"
     f"-----------------------------------------------\n"
     f"Total_Months: {total_months}\n"
     f"Total: ${total_profitloss}\n"
     f"Average Change: ${ProfitLoss_change_avg}\n"
     f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
     f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)
print(Output)
# Export the results to text file
with open(Output_file, "w") as txt_file:
     txt_file.write(Output)





 
 
