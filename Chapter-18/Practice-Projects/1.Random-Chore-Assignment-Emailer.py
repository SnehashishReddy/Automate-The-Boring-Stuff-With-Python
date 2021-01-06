import ezgmail, random

chores = ['dishes', 'bathroom', 'vaccum', 'walk dog']
emailAddresses = ['abcd@gmail.com','abcdefg@gmail.com','abc123@gmail.com','aabbcc@gmail.com']
while len(emailAddresses) != 0:
    randomChore = random.choice(chores)
    randomEmail = random.choice(emailAddresses)
    chores.remove(randomChore)
    emailAddresses.remove(randomEmail)
    ezgmail.send(randomEmail, 'Your Random Chore', randomChore)