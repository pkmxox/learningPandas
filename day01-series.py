import pandas as pd
import numpy as np

dataSet=np.arange(20).reshape(5, 4)
dataWNull = [
    [1, 2, 3, 4, 5],
    [6, 7, None, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]


dataSeries =pd.DataFrame(dataSet, index=[1, 2, 3, 4, 5], columns=["col1", "col2", "col3", "col4"])

dataSeriesNull=pd.DataFrame(dataWNull, index=["row1", "row2", "row3", "row4"], columns=["c1", "c2", "c3", "c4", "c5"])
print(dataSeries)
# print(dataSeries.head(2))
# print(dataSeries.tail(2))
# print(dataSeries.info())
# print(dataSeries.describe())

# print(dataSeries["col1"])
# print(dataSeries.loc[4])

# print(dataSeries.iloc[2:4, 2:4])

# print(dataSeries[["col1", "col4"]])

#print(dataSeries.iloc[:, 1:].values)
# print(dataSeries.isnull())
# print(dataSeriesNull.isnull())
# print("total: ", dataSeriesNull.isnull().sum())



