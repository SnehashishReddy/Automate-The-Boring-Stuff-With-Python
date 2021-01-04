# Solutions for the Practice Questions in Chapter 14

## 1. What three files do you need for EZSheets to access Google Sheets?
1. A Credentials File
2. A Token for Google Sheets
3. A Token for Google Drive
## 2. What two types of objects does EZSheets have?
A Spreadsheet object and a Sheet object
## 3. How can you create an Excel file from a Google Sheet spreadsheet?
downloadasExcel() on ezsheets.Spreadsheet()
# 4. How can you create a Google Sheet spreadsheet from an Excel file?
ezsheets.upload() with the file name
## 5. The ss variable contains a Spreadsheet object. What code will read data from the cell B2 in a sheet titled “Students”?
```
ss['Students']['B2']
```
## 6. How can you find the column letters for column 999?
```
ezsheets.getColumnLetterOf(999)
```
## 7. How can you find out how many rows and columns a sheet has?
The rowCount and columnCount should give us the no. of rows and columns
## 8. How do you delete a spreadsheet? Is this deletion permanent?
We can use delete(). It won't be permanent until permanent=True is passed
## 9. What functions will create a new Spreadsheet object and a new Sheet object, respectively?
createSpreadsheet() and createSheet()
## 10. What will happen if, by making frequent read and write requests with EZSheets, you exceed your Google account’s quota?
The requests will get throttled.