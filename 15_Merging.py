import pandas as pd #type:ignore

df_Customer=pd.DataFrame({
    "Customer_Id":[1,2,3,4,5,6,7,8],
    "Name":["Dheeraj","Prem","Suraj","Abhiman","Shravan","Vivek","Prajwal","Ganesh"],
    })

df_Orders=pd.DataFrame({
    "Customer_Id":[1,2,3,4,5,6],
    "Amount_Order":[1000,3000,2000,4000,7000,3500]
})

# MERGING

# 1-Inner Join(Merge only common values)
df_Merge=pd.merge(df_Customer,df_Orders,on="Customer_Id",how="inner")
print("Inner_Join")
print(df_Merge)

# 2-Outer Join(Merge all and replace NaN where data is not there)
df_Merge=pd.merge(df_Customer,df_Orders,on="Customer_Id",how="outer")
print("Outer_Join")
print(df_Merge)

# 3-Left Join(Merge all elements from left and replace NaN where needed)
df_Merge=pd.merge(df_Customer,df_Orders,on="Customer_Id",how="left")
print("Left_Join")
print(df_Merge)

# 4-Right Join(Merge all elements from Right and replace NaN where needed)
df_Merge=pd.merge(df_Customer,df_Orders,on="Customer_Id",how="right")
print("Right_Join")
print(df_Merge)

# 5-Right Join(Merge all elements from Right and replace NaN where needed)
df_Merge=pd.merge(df_Customer,df_Orders,on="Customer_Id",how="cross")
print("Cross_Join")
print(df_Merge)