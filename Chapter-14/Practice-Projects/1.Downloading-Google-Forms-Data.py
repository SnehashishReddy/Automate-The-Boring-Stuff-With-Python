import ezsheets, os

ss = ezsheets.Spreadsheet('1ZOqOUGXYU4GsYr8wtcqruVXwo1AfPcUpE1yGgEhQrUc')
ss.downloadAsCSV()

email_list = []
for x in os.listdir():
    if x.endswith('.csv'):
        with open(x,'r') as file:
            k = list(file)
            for i in range(1,len(k)):
                email_list.append(k[i].split(',')[-1])
print(*email_list)