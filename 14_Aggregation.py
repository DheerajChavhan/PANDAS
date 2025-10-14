import pandas as pd #type:ignore

Data={
    "Name":["Dheeraj","Prem","Abhiman","Suraj","Shravan"],
    "Age":[22,21,19,21,20],
    "Salary":[100000,35000,50000,45000,75000]
}

df=pd.DataFrame(Data)

# Summary
Avg_Age=df["Age"].mean()
Total_Salary=df["Salary"].sum()

print(f"Average Age:{Avg_Age}")
print("Total_Salary:",Total_Salary)


# Grouping
grouped=df.groupby("Age")["Salary"].sum()
print(grouped)

# For Multiple Columns
grouped=df.groupby(["Age","Name"])["Salary"].sum()
print(grouped)

# Common Functions
# sum()
# mean()
# min()
# max()
# std()
# count()