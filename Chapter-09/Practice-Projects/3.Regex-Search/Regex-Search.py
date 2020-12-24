import os, re
files = os.listdir("3.Regex-Search/")
regex = str(input("Please enter the regular expression: \n"))
for x in files:
    if x[-3:] == 'txt':
        file = open("3.Regex-Search/"+x, 'r')
        content = list(map(str, (file.read().strip().split("\n"))))
        for y in content:
            print((re.search(regex,y)))