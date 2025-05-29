import pandas as pd
# To access xlsx file , need to import openpyxl package

#Data  = {"Name" : ["R","J","V"],
#        "Age" : [19,20,30]}

#data = pd.DataFrame(Data)
#print(data)

#Excel_Data = pd.read_csv("C:/Users/Riddhi/Downloads/hotel_booking/hotel_booking.csv")
Excel_Data = pd.read_excel("C:/Users/Riddhi/Downloads/Datasets-main/Datasets-main/expense3.xlsx")
data = pd.DataFrame(Excel_Data)
print(Excel_Data.info())
print(Excel_Data.describe())
print(Excel_Data.isnull())
print(Excel_Data.isnull().sum())
print(Excel_Data)
print(Excel_Data.head(5))
print(Excel_Data.tail(5))
print(Excel_Data["Category"].duplicated().sum())
print(Excel_Data["EID"].drop_duplicates())

import numpy as np
print(Excel_Data.replace(np.nan,"demo1"))
Excel_Data.loc[(Excel_Data["Amount"] < 50), "Discount"] = "0 %"
Excel_Data.loc[(Excel_Data["Amount"] > 50), "Discount"] = "10 %"
print(Excel_Data)