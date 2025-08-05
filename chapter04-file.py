import pandas as pd

df=pd.read_csv("vgsales.csv") #reading csv
dJson=pd.read_json("EonlineShop.json")

#print(df.to_string()) #printing entire dataFrame
#max row
#print(pd.options.display.max_rows)
pd.options.display.max_rows=10
print(df)
print(dJson)