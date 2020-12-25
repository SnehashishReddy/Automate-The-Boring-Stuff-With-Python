import os

p = os.getcwd()
for folderName, subfolders, filenames in os.walk(p):
    for filename in filenames:
        absolute_path = folderName + '/' + filename
        if os.path.getsize(absolute_path) > 104857600:
            print(absolute_path)