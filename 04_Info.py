import pandas as pd # type: ignore

Data={
    "Name":["Dheeraj","Prem","Suraj"],
    "Age":[21,20,19],
    "City":["Pune","Sambhajinagar","Satara"]
}
df=pd.DataFrame(Data)
print(df.info())

# info() method

# 1-No.of Rows and Columns
# 2-Name of Columns
# 3-Data type(int,float)
# 4-Not Null Counts
# 5-Memory usage of Data