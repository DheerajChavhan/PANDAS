import pandas as pd # type: ignore

Data={
    "Name":["Dheeraj","Prem","Suraj","Abhiman","Aman"],
    "Age":[21,20,19,18,22],
    "Salary":[100000,50000,40000,30000,25000],
    "Performance_Score":[100,90,80,70,60]
}

df=pd.DataFrame(Data)

#Selecting Single Column
print("Name")               #Single column will return series
name=df["Name"]
print(name)

#Selecting Multiple Columns
subset=df[["Name","Age"]]   #We have to pass the list inside df[]
print(subset)

# Filtering the Rows with Single Condition
High_Salary=df[df["Salary"]>30000]
print(High_Salary)

#Filtering the Row with Multiple Conditions
subset=df[(df["Salary"]>30000) & (df["Age"]>19)]
print(subset)

# Filtering Rows with OR Conditon
Subset_or=df[(df["Salary"]>30000) | (df["Age"]>19)]
print(Subset_or)