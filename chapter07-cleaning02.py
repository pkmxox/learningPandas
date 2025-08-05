import pandas as pd
import matplotlib.pyplot as pt

dataSet = pd.read_json("withNullValue.json")

#checking all the data
print(dataSet.head())
print(dataSet.info())
print(dataSet.describe())
print("duplicated data: ", dataSet.duplicated().sum())
print("="*30)

#handling data to null value and mising value
print("checking null", "="*30)
print(dataSet.isnull().sum())
print("checking empty space", "="*30)
print((dataSet=="").sum())
dataSet.replace("", pd.NA, inplace=True)
dataSet.dropna(subset=['order_date'], inplace=True)
print("final result", "="*30)
print(dataSet.isnull().sum())

print("cleaning data", "="*80)
#cleaning data

data_qty_num =pd.to_numeric(dataSet["quantity"], errors='coerce')
data_price_num=pd.to_numeric(dataSet["price_per_unit"], errors='coerce')

dataSet["quantity"] =pd.to_numeric(dataSet["quantity"], errors='coerce')
dataSet["price_per_unit"]=pd.to_numeric(dataSet["price_per_unit"], errors='coerce')

invalid_qty =dataSet[data_qty_num<=0]
invalid_price =dataSet[data_price_num<=0]
print("invalid quantity", "="*80)
print(invalid_qty)
print("invalid price", "="*80)
print(invalid_price)

dataSet.loc[dataSet["quantity"]<=0, 'quantity']=pd.NA
dataSet.loc[dataSet["price_per_unit"]<=0, 'price_per_unit']=pd.NA

print("removing duplicate", "="*80)
#removing data

print("before", dataSet.duplicated().sum())
dataSet.drop_duplicates(inplace=True)
print("after", dataSet.duplicated().sum())

print("overview", "="*80)
#order
print(dataSet['status'].value_counts(dropna=False))
print(dataSet.groupby('category')['price_per_unit'].mean())
print(dataSet.groupby('customer_name')['price_per_unit'].sum())

dataSet['status'].value_counts().plot(kind='bar', title="order by status")
pt.show()