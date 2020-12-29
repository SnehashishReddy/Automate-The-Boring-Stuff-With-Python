import time,pyperclip

print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch.Press Ctrl-C to quit.')
input()
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1
txt = ''
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        string = ('Lap #%s: %s (%s)' % (str(lapNum).rjust(2), str(totalTime).center(6), str(lapTime).rjust(5)))
        print(string,end='')
        txt+=(string + '\n')
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print('\nDone.')
    pyperclip.copy(txt)

# Lap #1: 3.56 (3.56)
# Lap #2: 8.63 (5.07)
# Lap #3: 17.68 (9.05)
# Lap #4: 19.11 (1.43)

# Lap # 1:   3.56 (  3.56)
# Lap # 2:   8.63 (  5.07)
# Lap # 3:  17.68 (  9.05)
# Lap # 4:  19.11 (  1.43)