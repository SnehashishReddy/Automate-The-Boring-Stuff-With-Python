file = list(open('Mad-Libs.txt', 'r'))
nfile = open('Input-Mad-Libs.txt','w+')
sentence = (str(file[0])).split()
adjective = (str(input('Enter an adjective: \n'))).lower()
noun1 = (str(input('Enter a noun: \n'))).lower()
verb = (str(input('Enter a verb: \n'))).lower()
noun2 = (str(input('Enter a noun: \n'))).lower()
noun = [noun1,noun2]
y = 0
for x in range(0,len(sentence)):
    if sentence[x] == 'ADJECTIVE':
        sentence[x]  = adjective
    elif sentence[x]  == 'NOUN':
        sentence[x]  = noun[y]
        y+=1
    elif sentence[x]  == 'VERB.':
        sentence[x]  = verb + '.'
for x in sentence:
    nfile.write(x + ' ')
print(*sentence)