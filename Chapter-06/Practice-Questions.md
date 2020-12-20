# Solutions for the Practice Questions in Chapter 06

## 1. What are escape characters?
Escape characters are used to insert illegal characters into a string
## 2. What do the \n and \t escape characters represent?
The '\n' escape character is used to create a new line in a string\
The '\t' escape character is used to create a tab (usually 4 spaces) in a string
## 3. How can you put a \ backslash character in a string?
By using '\\\\'
## 4. The string value "Howl's Moving Castle" is a valid string. Why isn’t it a problem that the single quote character in the word Howl's isn’t escaped?
The quotes using to represent the string here are double quotes, so single quotes can be freely used inside the string without needing to use an escape character
## 5. If you don’t want to put \n in your string, how can you write a string with newlines in it?
You could use multiline strings. Like this:
```
multiline_string = '''
This is a
multiline
string
'''
```
## 6. What do the following expressions evaluate to?
```
'Hello, world!'[1]
'Hello, world!'[0:5]
'Hello, world!'[:5]
'Hello, world!'[3:]
```
The first statement will evaluate to 'e'\
The second statement will evaluate to 'Hello'\
The third statement will evaluate to 'Hello' as well\
The fourth statement will evaluate to 'lo, world!'
## 7. What do the following expressions evaluate to?
```
'Hello'.upper()
'Hello'.upper().isupper()
'Hello'.upper().lower()
```
The first statement will convert 'Hello' into 'HELLO'\
The second statement will first convert 'Hello' into 'HELLO' and then, check if it's fully in uppercase or not. As it has already been converted into upper case, the statement will be returning True\
The third statement will first convert 'Hello' into 'HELLO' and then, convert 'HELLO' into 'hello'
## 8. What do the following expressions evaluate to?
```
'Remember, remember, the fifth of November.'.split()
'-'.join('There can be only one.'.split())
```
The first statement will be splitting the string's spaces and then, return a list. ['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']\
The second statement will be first splitting the string's spaces and then, join them back again using a '-'. There-can-be-only-one.
## 9. What string methods can you use to right-justify, left-justify, and center a string?
string.rjust()\
string.ljust()\
string.center()
## 10. How can you trim whitespace characters from the beginning or end of a string?
We can use string.lstrip() and string.rstrip()