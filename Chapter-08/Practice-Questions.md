# Solutions for the Practice Questions in Chapter 08

## 1. Does PyInputPlus come with the Python Standard Library?
No, it doesn't
## 2. Why is PyInputPlus commonly imported with import pyinputplus as pyip?
So that the code is easier to type
## 3. What is the difference between inputInt() and inputFloat()?
inputInt() returns an integer, while inputFloat() returns a floating point number
## 4. How can you ensure that the user enters a whole number between 0 and 99 using PyInputPlus?
By using inputInt(min=0,max=99)
## 5. What is passed to the allowRegexes and blockRegexes keyword arguments?
A list of regex strings
## 6. What does inputStr(limit=3) do if blank input is entered three times?
The RetryLimitException will be generated
## 7. What does inputStr(limit=3, default='hello') do if blank input is entered three times?
It will print out 'hello'