import pandas as pd # type: ignore

Data={
    "Name":["Dheeraj",None,"Suraj","Abhiman","Aman","Shravan"],
    "Age":[21,20,19,18,22,None],
    "Salary":[100000,50000,40000,30000,25000,20000],
    "Performance_Score":[100,90,80,70,60,50]
}

# Finding the Missing Values
df=pd.DataFrame(Data)
print(df)
print(df.isnull())          #Return True if value is not there
print(df.isnull().sum())    #Returns the number of null values in each column

# Deleting the Missing Values
# df.dropna(axis=0,inplace=True)   #axis=0 will remove the row and axis=1 will remove th column of none values  
# print(df)

#Filling the Missing data
# df.fillna(0,inplace=True)
df["Age"].fillna(df["Age"].mean(),inplace=True)   #To Fill the missing value with certain value rather than 0
print(df)