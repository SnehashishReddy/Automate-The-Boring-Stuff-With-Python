# Strong Password Detection

# Write a function that uses regular expressions to make sure the password 
# string it is passed is strong. A strong password is defined as one that is at 
# least eight characters long, contains both uppercase and lowercase characters, 
# and has at least one digit. You may need to test the string against multiple 
# regex patterns to validate its strength.

import re

password_format = re.compile(r'^(?=.*([A-Z]){1,})(?=.*[!@#$&*]{1,})(?=.*[0-9]{1,})(?=.*[a-z]{1,}).{8,100}$')
password = str(input("Please enter the password to be checked: \n"))
matchObject = password_format.search(password)
if matchObject == None:
    print("The password {} is not a strong password.".format(password))
else:
    print("The password {} is a strong password".format(matchObject.group(0)))