import pandas as pd

myData=pd.read_csv("vgsales.csv")

print("with 10 head data\n",myData.head(10))
print(myData.head())

print("with 10 tail data\n",myData.tail(10))
print(myData.tail())

#checking the data head and tail above
#below we have info about dataSet

print(myData.info())