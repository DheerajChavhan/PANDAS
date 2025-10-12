import pandas as pd # type: ignore

Data={
    "Name":["Dheeraj","Prem","Suraj","Abhiman","Aman"],
    "Age":[21,20,19,18,22],
    "Salary":[100000,50000,40000,30000,25000],
    "Performance_Score":[100,90,80,70,60]
}

df=pd.DataFrame(Data)

# Updating Salary by 5 percent 
df["Salary"]=df["Salary"]*1.05
print("After Updating All values of Column")
print(df)

#Updating the Salary of a Specific person
#Syntax: df.loc(row_index,column_name)=new_value 
df.loc[0,"Salary"]=110000
print(df)


