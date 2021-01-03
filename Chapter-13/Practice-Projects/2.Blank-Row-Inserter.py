import sys, openpyxl

n = int(sys.argv[1])
m = int(sys.argv[2])
file = sys.argv[3]

rwb = openpyxl.load_workbook(file)
rsheet = rwb.active

wwb = openpyxl.Workbook()
wsheet = wwb.active

for a in range(1, rsheet.max_row + 1):
    for b in range(1, rsheet.max_column + 1):
        # Write rows normally until n is encountered
        if a < n:
            wsheet.cell(row = a, column = b).value = rsheet.cell(row = a, column = b).value
        # Give gap and start writing once n comes in
        else:
            wsheet.cell(row=(a+m), column=b).value = rsheet.cell(row=a, column=b).value
wwb.save('inserted_{}'.format(file))