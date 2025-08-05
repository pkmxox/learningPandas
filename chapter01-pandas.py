import pandas as pd
#import pandas

#creating data set
my_dataSet ={
    'cars':["BMW", "mercedes", "RR"],
    'passings':[3, 7, 2]
}

#adding dataset to panda and variable
myData = pd.DataFrame(my_dataSet)

#printing the variable
print(myData)

print("checking pandas version",pd.__version__)