# Solutions for the Practice Questions in Chapter 16

## 1. What are some features Excel spreadsheets have that CSV spread-sheets don’t?
1. You can change height/width of cells in Excel
2. You can add Pictures/Charts to Excel Spreadsheets
3. You can change the data type of cells to be something other than strings in Excel
4. The cell data can be styled as per requirements in Excel
## 2. What do you pass to csv.reader() and csv.writer() to create reader and writer objects?
We pass a File object, which was obtained from open()
## 3. What modes do File objects for reader and writer objects need to be opened in?
'rb' for reader and 'wb' for writer
## 4. What method takes a list argument and writes it to a CSV file?
the writerow() function
## 5. What do the delimiter and lineterminator keyword arguments do?
A delimiter is the string used to separate cells in a row\
A lineterminator is the string used to separate rows\
The delimiter and lineterminator arguments can change both as per requirement
## 6. What function takes a string of JSON data and returns a Python data structure?
json.loads()
## 7. What function takes a Python data structure and returns a string of JSON data?
json.dumps()