# Sandwich Maker

# Write a program that asks users for their sandwich preferences. The program should use PyInputPlus to 
# ensure that they enter valid input, such as:

# Using inputMenu() for a bread type: wheat, white, or sourdough.
# Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
# Using inputYesNo() to ask if they want cheese.
# If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
# Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
# Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.

# Come up with prices for each of these options, and have your program display a total cost after 
# the user enters their selection.

import pyinputplus as pyin

price = 0

bread = pyin.inputMenu(choices=['wheat','white','sourdough'],prompt='Please enter your choice of bread: \n')
if bread.lower() == 'wheat':
    price+=3
elif bread.lower() == 'white':
    price+=1
else:
    price+=2

protein = pyin.inputMenu(choices=['chicken','turkey','ham','tofu'],prompt="Please enter your choice of protein: \n")
if protein.lower() == 'chicken':
    price+=3
elif protein.lower() == 'turkey':
    price+=4
elif protein.lower() == 'ham':
    price+=2
else:
    price+=1

cheese = pyin.inputYesNo(prompt="Do you want cheese in your sandwich? Yes or No: \n")
if cheese.lower() == 'yes':
    cheese_type = pyin.inputMenu(choices=['cheddar','Swiss','mozzarella'],prompt='What type of cheese do you prefer? \n')
    if cheese_type.lower() == 'cheddar':
        price+=1
    elif cheese_type.lower() == 'swiss':
        price+=3
    else:
        price+=2

mayo = pyin.inputYesNo(prompt="Do you want mayo in your sandwich? Yes or No: \n")
if mayo.lower() == 'yes':
    price+=1

mustard = pyin.inputYesNo(prompt="Do you want mustard in your sandwich? Yes or No: \n")
if mustard.lower() == 'yes':
    price+=1

lettuce = pyin.inputYesNo(prompt="Do you want lettuce in your sandwich? Yes or No: \n")
if lettuce.lower() == 'yes':
    price+=1

tomato = pyin.inputYesNo(prompt="Do you want tomatoes in your sandwich? Yes or No: \n")
if tomato.lower() == 'yes':
    price+=1

amount = pyin.inputInt(prompt="How many such sandwiches do you want? \n",min=1)
print("The total cost of your order stands at " + str(amount*price) + ' durums')