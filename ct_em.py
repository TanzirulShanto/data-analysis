import pandas as pd
import matplotlib.pyplot as plt

file = "D:/temp/EM-CT-Marks.csv"

dataframe = pd.read_csv(file)

data = dataframe['Mark'].value_counts()

print(list(data))


print(data)
