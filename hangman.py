import random as rand

"""
status = True
with open('sowpods.txt', 'r') as f:
    all_words = f.readlines()
    random_word = rand.choice(all_words).strip()
#print('The random word selected from the text file is:', random_word)
print('Welcom to Hangman!')

for word in random_word:
    print('_ ', end = '')
user_input = input('\n >>> Guess the Letter: ')

while status:
    for word2 in user_input:
        if word2 in word:
            print(word2, end = '')
        else: 
            print('Incorrect!')
"""

"""
counter = {}
with open('sowpods.txt') as fp:
    line = fp.readline()
    while line:
        line = line.strip()
        if line in counter:
            counter[line] += 1
        else:
            counter[line] = 1
        line = fp.readline()
print(counter)

####################################

#        print(line)
#        line = fp.readline()

####################################

#    for count, line in enumerate(fp):
#        pass
#print("Total lines", count + 1)
"""
