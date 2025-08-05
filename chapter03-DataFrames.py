import pandas as pd


#dataFrames
data={
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

#load data into a DataFrame object:

df=pd.DataFrame(data)

print(df.loc[0]) # Accessing the first row
print(df.loc[[0, 2]]) # Accessing the index[] row
print(df.loc[[0, 2, 1]]) # Accessing the index[] row

newDataFrames = pd.DataFrame(data, index=["day01", "day02", "day03"])

print(newDataFrames)
print(df.loc[0])
print(newDataFrames.loc["day01"])