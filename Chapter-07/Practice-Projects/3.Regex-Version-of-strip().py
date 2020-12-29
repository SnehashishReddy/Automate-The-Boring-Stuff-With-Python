# Regex Version of the strip() Method

# Write a function that takes a string and does the same thing as the strip() 
# string method. If no other arguments are passed other than the string to strip, 
# then whitespace characters will be removed from the beginning and end of the string. 
# Otherwise, the characters specified in the second argument to the function will be 
# removed from the string.

import re

method = re.compile(r'^\s*(.*?)\s*$')
string = str(input("Please enter the string literal to be stripped: \n"))
character = str(input("Please enter the character to be removed. If None, press Enter: \n"))
if character == '':
    ans = re.sub(method,'',string)
else:
    ans = re.sub(re.compile(character),'',string)
print(ans)