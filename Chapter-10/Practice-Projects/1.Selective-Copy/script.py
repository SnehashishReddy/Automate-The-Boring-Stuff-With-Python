import shutil, os
from pathlib import Path

p = os.getcwd()
for folderName, subfolders, filenames in os.walk(p):
    for filename in filenames:
        if filename[-3:] == 'pdf':
            try:
                shutil.copy(folderName + '/' + filename, p + '/' + 'Copied-Folder')
            except shutil.SameFileError:
                pass
print('Success Senor!')