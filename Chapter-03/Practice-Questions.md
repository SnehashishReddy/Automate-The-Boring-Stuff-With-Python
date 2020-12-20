# Solutions for the Practice Questions in Chapter 03

## 1. Why are functions advantageous to have in your programs?
Functions reduce the need for duplicate code thus, making the project more readable and cleaner

## 2. When does the code in a function execute: when the function is defined or when the function is called?
The code in a function executes when the function is called

## 3. What statement creates a function?
the def statement creates a function

## 4. What is the difference between a function and a function call?
In a function, the code that's supposed to be executed is written.\
When that function is called in the code, the code will be redirected to the point where the code for the function was written and then, executes it.

## 5. How many global scopes are there in a Python program? How many local scopes?
1 Global Scope and any no. of Local Scopes depending on the no. of functions

## 6. What happens to variables in a local scope when the function call returns?
The variables are destroyed

## 7. What is a return value? Can a return value be part of an expression?
A return value is used to end the execution of a function\
After ending the execution, a value is returned which would be the result of the function's execution\
Yes, a return value can be part of an expression

## 8. If a function does not have a return statement, what is the return value of a call to that function?
None will be returned

## 9. How can you force a variable in a function to refer to the global variable?
We can use the global keyword

## 10. What is the data type of None?
It's a null value/no value

## 11. What does the import areallyourpetsnamederic statement do?
It imports the areallyourpetsnamederic library into your code so, that you can call the functions in the library

## 12. If you had a function named bacon() in a module named spam, how would you call it after importing spam?
```
import spam
spam.bacon()
```
## 13. How can you prevent a program from crashing when it gets an error?
We can use the try/except statements to handle the error

## 14. What goes in the try clause? What goes in the except clause?
The code we're supposed to use goes in the try clause\
The error that needs to be handled goes into the except clause