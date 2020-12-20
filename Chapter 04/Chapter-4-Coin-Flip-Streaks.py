import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    random_list = []
    for x in range(0,100):
        random_list.append(random.choice(['heads','tails']))
    for x in range(0,95):
        buffer_list = random_list[x:x+6]
        if ('tails' not in buffer_list) or ('heads' not in buffer_list):
            numberOfStreaks+=1
print('Chance of streak: %s%%' % (numberOfStreaks / (100*10000)))