import ezsheets, sys

file_name = sys.argv[1]
ss = ezsheets.upload(file_name)
spreadsheet_id = list(ezsheets.listSpreadsheets())[0]
ss = ezsheets.Spreadsheet(spreadsheet_id)

# ss.downloadAsExcel()
# ss.downloadAsODS()
# ss.downloadAsCSV()
# ss.downloadAsTSV()
# ss.downloadAsPDF()
# ss.downloadAsHTML()