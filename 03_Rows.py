# head(),tail()
# head(n)  display the top n rows from the data if n is not giver by default it will give top 5 rows 
# tail(n)  display the bottom n rows from the data if n is not given by default it will give bottom 5 rows 

import pandas as pd # type: ignore

df=pd.read_json("sample_Data.json")

print("The first 5 rows are:")
print(df.head(5))

print("The last 5 rows are:")
print(df.tail(5))