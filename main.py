#read csv
#locate customer IDs by grouping
#Check if all dates are consecutive
# Sort the customer IDs with the consecutive dates
# Select number of customers

import pandas as pd
import numpy as np
from datetime import date, datetime
from collections import Counter

def transaction(payment_data, n):
    data = pd.read_csv(payment_data)

    data = data.rename(columns={"Customer ID": "Customer_ID", "Transaction Amount": "Transaction_Amount", "Transaction Date": "Transaction_Date"})
#change dates to datetime
    data["Transaction_Date"] = data["Transaction_Date"].apply(pd.to_datetime)
   
#grouping customerIds 
# changing dates to integers
# use numpy to find consecutive differences
#count the differences and append customer ID into a list
# return n customerIds
    for group,name in data.groupby("Customer_ID"):        
        date_num = [item.toordinal() for item in name.Transaction_Date]
        date_num = np.diff(sorted(date_num))
        print(date_num)
        counter = 0
        l = []
        customer = []
        for item in date_num:           
            if item == 1:
                counter += 1
                l.append(counter)
                
                if max(l):
                    customer.append(name.Customer_ID)
                    if len(customer) == n:
                        print(customer)
                
            else:
                counter = 0

  

transaction("transaction_data_1.csv", 1)    
# data= pd.read_csv("transaction_data_2.csv")
# print(data)