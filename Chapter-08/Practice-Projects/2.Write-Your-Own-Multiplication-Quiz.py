# Write Your Own Multiplication Quiz

# To see how much PyInputPlus is doing for you, try re-creating the multiplication quiz project on your 
# own without importing it. This program will prompt the user with 10 multiplication questions, 
# ranging from 0 × 0 to 9 × 9. You’ll need to implement the following features:

# If the user enters the correct answer, the program displays “Correct!” for 1 second and moves on to the next question.
# The user gets three tries to enter the correct answer before the program moves on to the next question.
# Eight seconds after first displaying the question, the question is marked as incorrect even if the user
# enters the correct answer after the 8-second limit.


from random import randint
import time

score = 0
for x in range(0,10):
    starttime = time.time()
    n1 = randint(0,9)
    n2 = randint(0,9)
    print(str(n1)+' x '+str(n2))
    tries = 0
    identifier = 0
    while tries < 3 and identifier == 0:
        try:
            ans = int(input("Please enter your answer: "))
            if ans == n1*n2:
                if ((time.time()-starttime)>=8):
                    print('The answer was correct but, you\'ve timed out')
                    time.sleep(1.0)
                    break
                else:
                    print("Correct")
                    score+=1
                    time.sleep(1.0)
                    identifier = 1
            elif ans != n1*n2:
                print("Your answer was incorrect. You currently have " + str(2-tries) + " more tries left.")
                tries+=1
            elif((time.time()-starttime)>=8):
                print('Time\'s up.')
                break
            if tries == 3:
                break
        except ValueError:
            print("You have not entered a valid integer")
            continue
print('You\'ve successfully answered ' + str(score) + '/10 ' + 'questions right!'   )