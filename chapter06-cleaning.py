import pandas as pd

dataSet =pd.read_csv("newUnFilteredData.csv")

#removing all the null value

dataSet.dropna(inplace=True)

print(dataSet.to_string())

#dataSet.fillna(10, inplace=True)
#dataSet.fillna({"email":"nomail@gmail.com"}, inplace=True)

print("second time\n ",dataSet.to_string())

#mean median mode

dataJson = pd.read_json("withNullValue.json")

meanStock=dataJson["stock"].mean()
medianStock =dataJson["stock"].median()
modeStock =dataJson["stock"].mode()
print(meanStock)
print(medianStock)
print(modeStock)

