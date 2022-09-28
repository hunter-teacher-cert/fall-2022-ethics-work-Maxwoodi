import re


   
def find_names(line):
    pattern = r"(M\w+\.|D\w+\.|[a-zA-Z]\w*\S)"     ###M\w+\.|D\w+\.|[a-zA-Z]\w*\S
    result = re.findall(pattern,line)
    return result


f = open(r'C:\Users\Tashema Bholanath\Documents\DeskTop\JAVA\RemoteLearning2020_2021\APCS_A\MECPS2021_2022\JavaResources\hunterSummer2022\CSCI77800\names.txt', 'r')
#print(f.read())
for line in f.readlines():
    #print(line)
    result = find_names(line)
    if (len(result)>0):
        print(result)
