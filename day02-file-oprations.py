import pandas as pd

csv_data =pd.read_csv('vgsales.csv')

#print(csv_data.head())
#print(csv_data.head(2))
#print(csv_data.dtypes)///////////////
print(csv_data['dates'].dtypes)