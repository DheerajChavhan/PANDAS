import pandas as pd #type:ignore

Data={
    "Name":["Dheeraj","Prem","Abhiman","Suraj"],
    "Age":[22,21,19,20],
    "Salary":[100000,35000,45000,50000]
}

df=pd.DataFrame(Data)

# Sorting data of 1 Column
# df.sort_values(by="Salary",ascending=False,inplace=True)   
# print(df)


df.sort_values(by=["Age","Salary"],ascending=[False,False],inplace=True)   
print(df)