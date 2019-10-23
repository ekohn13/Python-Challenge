


import pandas as pd
import os

py_bank_df = pd.read_csv('/Users/edwardkohn/Desktop/Homeworks/Python/budget_data.csv')


py_bank_df.head()






Total_months = py_bank_df.Date.count()





net_sum = py_bank_df['Profit/Losses'].sum()





py_bank_df['Average_change'] = py_bank_df['Profit/Losses'] - py_bank_df['Profit/Losses'].shift(+1)
average_change= py_bank_df.Average_change.mean()
rounded_avg=(round(average_change,2))





mc = py_bank_df.Average_change.max()




mini = py_bank_df.Average_change.min()





max_with_date = py_bank_df.loc[py_bank_df['Average_change'] == mc, 'Date'].iloc[0]





min_with_date = py_bank_df.loc[py_bank_df['Average_change'] == mini , 'Date'].iloc[0]





print("Financial Analysis")
print('---------------------------')
print("Total months:"+ str(Total_months))
print("Total: "+str(net_sum))
print("Average Change: $:"  + str(rounded_avg))
print(f'Greatest Increase in Profits : {max_with_date} (${mc})' )
print(f'Greatest Decrease in Profits : {min_with_date} (${mini})' )





n1 = "Financial Analysis"
n2 = "Total: "+ str(net_sum)
n3 = "Average Change: $:"  + str(rounded_avg)
n4 = "Greatest Increase in Profits : " + str(max_with_date) + str(mc)
n5 = "Greatest Decrease in Profits : " + str(min_with_date) + str(mini)


mm = {'str': [n1,n2,n3,n4,n5]}
      
output = pd.DataFrame(mm)

output.to_csv('Py_bank.txt',header=False,index=False)

