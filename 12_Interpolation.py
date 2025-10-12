import pandas as pd #type:ignore

Data={
    "Time":[1,2,3,4,5],
    "Value":[10,None,30,None,50]
}

df=pd.DataFrame(Data)
print("Before interpolation")
print(df)

df["Value"]=df["Value"].interpolate(method="linear")     #Interpolation fill the null value using some pattern observed in it
print("After interpolation")
print(df)

#Interpolation
# Use when working with numeric values which follow some trend
# Use for Time Series Data