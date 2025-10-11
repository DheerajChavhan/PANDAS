import pandas as pd # type: ignore

Data={
    "Name":["Dheeraj","Prem","Suraj","Abhiman","Aman"],
    "Age":[21,20,19,18,22],
    "Salary":[100000,50000,40000,30000,25000],
    "Performance_Score":[100,90,80,70,60]
}

df=pd.DataFrame(Data)

# df["Bonus"]=df["Salary"]*0.1   #The new Column named Bonus will be Created
# print(df)

# Using Insert method
# Syntax: df.insert(Location,Column Name,Data) 

df.insert(3,"Bonus",df["Salary"]*0.1)
df.insert(0,"Employee_Id",[10,20,30,40,50])

print(df)
