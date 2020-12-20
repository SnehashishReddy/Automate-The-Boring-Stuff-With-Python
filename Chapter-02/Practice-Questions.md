# Solutions for the Practice Questions in Chapter 02

## 1. What are the two values of the Boolean data type? How do you write them?
True and False are the two values of the Boolean data type

## 2. What are the three Boolean operators?
The 3 boolean operators are: AND, OR, NOT

## 3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).
1.\
The AND operator takes 2 booleans on either side and returns True only if both sides are True\
True and True => True\
True and False => False\
False and True => False\
False and False => False

2.\
The OR operator takes 2 booleans on either side and returns True if either of those sides are True\
True or True => True\
True or False => True\
False or True => True\
False or False => False

3.\
The NOT operator takes 1 boolean and inverts it\
not True => False\
not False => True

## 4. What do the following expressions evaluate to?
5>4 and 3==5 will evaluate to False\
not 5>4 will evaluate to False\
5>4 or 3==5 will evaluate to True\
not ((5>4) or (3==5)) will evaluate to False\
(True and True) and (True==False) will evaluate to True\
(not False) or (not True)

## 5. What are the six comparison operators?
The six comparison operators are:\
\==\
\!=\
\<=\
\>=\
\>\
\<

## 6. What is the difference between the equal to operator and the assignment operator?
The equal to(==) operator compares both of the sides of the operator and checks if they're equal to each other\
The assignment(=) operator assigns the value on the right side to the variable on the left side

## 7. Explain what a condition is and where you would use one.
A Condition is a special operation used to compare the booleans given to it and return the respective boolean\
Conditions can be used when we need to execute only one block of code out of 2 depending on what we what the output to be

## 8. Identify the three blocks in this code:
```
spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam')
```

As seen above clearly, the three blocks of code can be found at line 2, line 3 and line 5

## 9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
```
spam = int(input())
if spam == 1:`
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')
```

## 10. What keys can you press if your program is stuck in an infinite loop?
Ctrl + C can be used to break out of an infinite loop\

## 11. What is the difference between break and continue?
break stops the execution of further code in the loop and proceeds downward out of the loop\
continue stops the execution of further code in the loop and returns control to the beginning of the loop,i.e. still in the loop.

## 12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
There's no difference, all three perform the exact same thing

## 13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
```
Program 1:
for x in range(1,11):
    print(x)

Program 2:
x = 1
while x <= 10:
    print(x)
    x+=1
```
## 14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
```
import spam
spam.bacon()

OR

from spam import bacon
bacon()
```