import os

directory = os.getcwd()
p = os.listdir()
p.sort()
required_files = []
extension = 'txt'
gap_index = int(input("Please input the number of the file after which you want to insert a new element: \n"))
for x in p:
    if x[-3:] == 'txt':
        required_files.append(x)
new_name = 'spam00' + str(int(required_files[gap_index-2][6:7])+2) + '.' + extension
os.rename((directory + '/' + required_files[gap_index-1]), new_name)
required_files[gap_index-1] = new_name
for x in range(gap_index,len(required_files)-1):
    if int(required_files[x][4:7]) - int(required_files[x+1][4:7]) == -1:
        new_name = required_files[x][:6] + str(int(required_files[x][6:7])+1) + '.' + extension
        os.rename((directory + '/' + required_files[x+1]), new_name)
        required_files[x+1] = new_name
print('Okay done :thumbsup:')