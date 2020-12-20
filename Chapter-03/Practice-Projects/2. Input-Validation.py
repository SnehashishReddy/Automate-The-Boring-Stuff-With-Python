# Input Validation

# Add try and except statements to the previous project to detect whether the user types in a noninteger string.
# Normally, the int() function will raise a ValueError error if it is passed a noninteger string, as in int('puppy'). 
# In the except clause, print a message to the user saying they must enter an integer.

def collatz(number):
    if number % 2 == 0:
        print(number//2)
        return number//2
    else:
        print(3*number + 1)
        return 3*number + 1
try:
    x = int(input())
    while x != 1:
        x = collatz(x)
except ValueError:
    print('Please enter an integer. Not a string literal')