import os

file = "D:/temp/Python Processed Data/Yarn-48.csv"

try:

    os.rename(file, "D:/temp/Python Processed Data/Yarn-48.txt")
except Exception as err:
    print(err)