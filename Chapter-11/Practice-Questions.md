# Solutions for the Practice Questions in Chapter 11

## 1. Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10.
```
assert spam >= 10, 'spam is less than 10.'
```
## 2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different (that is, 'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same).
```
assert eggs.lower() != bacon.lower(), 'eggs and bacon have the same string value'
```
## 3. Write an assert statement that always triggers an AssertionError.
```
assert False, 'AssertionError always triggers'
```
## 4. What are the two lines that your program must have in order to be able to call logging.debug()?
```
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s -  %(message)s')
```
## 5. What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt?
```
import logging
logging.basicConfig(filename='programLog.txt', level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
```
## 6. What are the five logging levels?
1. DEBUG
2. INFO
3. WARNING
4. ERROR
5. CRITICAL
## 7. What line of code can you add to disable all logging messages in your program?
```
logging.disable(logging.CRITICAL)
```
## 8. Why is using logging messages better than using print() to display the same message?
Logging messages log timestamps as well.
## 9. What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?
Step Over will execute a function call without stepping into it.\
Step In will move the debugger into a function call.\
Step Out will execute the code until it steps out of the function it is in.
## 10. After you click Continue, when will the debugger stop?
The debugger will stop either when the end of the program is reached or a breakpoint is reached.
## 11. What is a breakpoint?
When the code execution reaches a breakpoint, the debugger is paused.
## 12. How do you set a breakpoint on a line of code in Mu?
Clicking on the line number will set a breakpoint.