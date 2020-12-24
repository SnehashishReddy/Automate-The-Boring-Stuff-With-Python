# Solutions for the Practice Questions in Chapter 09

## 1. What is a relative path relative to?
They are relative to the current directory
## 2. What does an absolute path start with?
They always start with the root folder
## 3. What does Path('C:/Users') / 'Al' evaluate to on Windows?
WindowsPath('C:/Users/Al')
## 4. What does 'C:/Users' / 'Al' evaluate to on Windows?
Error, since strings can be concatenated only using \+
## 5. What do the os.getcwd() and os.chdir() functions do?
os.getcwd() gives you the current directory, while os.chdir() changes it
## 6. What are the . and .. folders?
Current and parent directories respectively
## 7. In C:\bacon\eggs\spam.txt, which part is the dir name, and which part is the base name?
C:\bacon\eggs is the dir name, while spam.txt is base name
## 8. What are the three “mode” arguments that can be passed to the open() function?
'r' for read, 'w' for write, 'a' for append
## 9. What happens if an existing file is opened in write mode?
The file is fully overwritten
## 10. What is the difference between the read() and readlines() methods?
read() gives file's whole contents as one string\
readlines() gives list of strings. Each string is a line from the file
## 11. What data structure does a shelf value resemble?
It closely resembles a dictionary.