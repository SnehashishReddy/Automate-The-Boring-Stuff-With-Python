import os, openpyxl, csv

for excelFile in os.listdir('.'):
    if excelFile.endwith('.xlsx'):
        wb = openpyxl.load_workbook(excelFile)
    for sheetName in wb.get_sheet_names():
        sheet = wb.get_sheet_by_name(sheetName)
        excelfilename = excelFile[:-5]
        csvFile = open(excelfilename + "_" + sheetName + '.csv', 'w',newline='')
        csvWriter = csv.writer(csvFile)
        for rowNum in range(1, sheet.max_row + 1):
            rowData = []
            for colNum in range(1, sheet.max_column + 1):
                rowData.append(sheet.cell(row=rowNum,column=colNum).value)
            for row in rowData:
                csvWriter.writerow(row)
        csvFile.close()