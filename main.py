import re


pattern = r'[A-Z][a-z]+'
pattern = r'[A-Z][a-z]+\s'
pattern = r'[1-8][0-9]+'
pattern = r'[0-9]\s'
pattern = r'([A-Z][a-z]+ )+'
pattern = r'([A-Z][A-Za-z]+( [A-Za-z]+)+)' //name
regexp = re.compile(pattern)

csv_file  =  "D:/temp/EM-CT-Marks.csv"
file = open(csv_file, 'r')

data = file.readline()




try:
    while data:
        
        res = re.findall(regexp, data)
        print(res)
        data = file.readline()

except Exception as err:
    print(err)







'''
[a-zA-Z0-9]+.[a-zA-Z0-9]+.@[\.[a-z]*]*

'''
file.close()