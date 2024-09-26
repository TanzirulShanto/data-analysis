import pandas as pd

file = "D:/temp/Python Processed Data/YARN - 48.xlsx"

data = pd.read_excel(file, sheet_name='Sheet1')
data.to_csv("D:/temp/Python Processed Data/Yarn-48.csv", index=False)

print(data)