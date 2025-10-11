import pandas as pd # pyright: ignore[reportMissingModuleSource]

Data={
    "Name":["Dheeraj","Prem","Suraj"],
    "Age":[21,20,19],
    "City":["Pune","Sambhajinagar","Satara"]
}

df=pd.DataFrame(Data)
print(df)

# df.to_csv("Data.csv",index=False)
# df.to_excel("Data.xlsx",index=False)
df.to_json("Data.json",index=False)