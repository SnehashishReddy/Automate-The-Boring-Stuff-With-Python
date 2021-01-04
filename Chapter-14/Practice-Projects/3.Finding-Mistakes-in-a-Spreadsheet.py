import ezsheets

ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')

ss.downloadAsCSV()

file = list(open('Bean_Count.csv'))
row_count = 1
for x in range(1, len(file)):
    row_count+=1
    lst = (file[x].strip()).split(',')
    if int(lst[0])*int(lst[1]) != int(lst[2]):
        print("There's a mistake at row {} where, it's been calculated that {} multiplied by {} is {} but, it's actually {}".format(row_count, lst[0],lst[1],lst[2],(int(lst[0])*int(lst[1]))))
        break