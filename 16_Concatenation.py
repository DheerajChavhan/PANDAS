import pandas as pd #type:ignore

df_Region1=pd.DataFrame({
    "Customer_Id":[1,2,3,4],
    "Name":["Dheeraj","Prem","Suraj","Abhiman"]
})

df_Region2=pd.DataFrame({
    "Customer_Id":[5,6,7,8],
    "Name":["Raju","Shyam","Baburao","Gopal"]
})  

# Concatenating Vertically  
df_concat=pd.concat([df_Region1,df_Region2],axis=0,ignore_index=True)
print("Concatenating Vertically ")
print(df_concat)

# Concatenating Horizontally  
df_concat=pd.concat([df_Region1,df_Region2],axis=1,ignore_index=True)
print("Concatenating Horizontally")
print(df_concat)