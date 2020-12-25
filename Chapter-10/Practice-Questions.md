# Solutions for the Practice Questions in Chapter 10

## 1. What is the difference between shutil.copy() and shutil.copytree()?
shutilcopy() can be used for a single file. shutil.copytree() will copy the whole folder tree.
## 2. What function is used to rename files?
os.rename()
## 3. What is the difference between the delete functions in the send2trash and shutil modules?
send2trash will send a file to the recycle bin while, shutil will unlink the file permanently deleting it
## 4. ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is equivalent to File objects’ open() method?
The zip.ZipFile() function can be considered equivalent to the File objects' open() method.