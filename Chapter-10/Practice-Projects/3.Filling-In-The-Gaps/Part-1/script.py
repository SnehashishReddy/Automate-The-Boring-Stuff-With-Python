import os

directory = os.getcwd()
p = os.listdir()
p.sort()
required_files = []
extension = 'txt'
for x in p:
    if x[-3:] == 'txt':
        required_files.append(x)
for x in range(0,len(required_files)-1):
    if int(required_files[x][4:7]) - int(required_files[x+1][4:7]) != -1:
        new_name = required_files[x][:6] + str(int(required_files[x][6:7])+1) + '.' + extension
        os.rename((directory + '/' + required_files[x+1]), new_name)
        required_files[x+1] = new_name
print('Okay done :thumbsup:')