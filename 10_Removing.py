import pandas as pd # type: ignore

Data={
    "Name":["Dheeraj","Prem","Suraj","Abhiman","Aman","Shravan"],
    "Age":[21,20,19,18,22,20],
    "Salary":[100000,50000,40000,30000,25000,20000],
    "Performance_Score":[100,90,80,70,60,50]
}

df=pd.DataFrame(Data)
print(df)

# Deleting the single column
# Syntax: df.drop(columns=["Column_Name",inplace=True])  inplace=True will update the existing column and inplace=Falce will give new Data
df.drop(columns=["Performance_Score"],inplace=True) 
print("Mpdified Data")
print(df)