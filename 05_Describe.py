# Step-1: Create a sample Dataframe using Dictionary

import pandas as pd # type: ignore

Data={
    "Name":["Dheeraj","Prem","Suraj","Abhiman","Aman"],
    "Age":[21,20,19,18,22],
    "Salary":[100000,50000,40000,30000,25000],
    "Performance_Score":[100,90,80,70,60]
}
df=pd.DataFrame(Data)
print(df.describe())   #Show the Descriptive Statistics of the Data
