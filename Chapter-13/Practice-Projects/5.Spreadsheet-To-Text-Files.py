# Give File Location using command line argument
import os, openpyxl, sys

wb = openpyxl.load_workbook(sys.argv[1])
sheet = wb.active
i = 0
for x in sheet.columns:
    with open("{}.txt".format(i), 'w') as file:
        for y in x:
            file.write(y.value)
    i+=1