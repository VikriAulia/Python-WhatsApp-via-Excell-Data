import pandas as pd
# import os # To hide the sender's number

# excel cols to access
require_cols = [3,4,6,8]
# read by default 1st sheet of an excel file
#df = pd.read_excel('dummy.xlsx')
dataframe1 = pd.read_excel('dummy.xlsx', sheet_name=0, usecols=require_cols, header=0)
print(dataframe1)