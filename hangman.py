import random

words = ['window', 'cat', 'dog']
word = random.choice(words)

wordinl = []
for i in range(len(word)):
    print('_', end='')
    wordinl.append('_')
print()

guessed = False

while not guessed:
    guess = input('Guess: ')
    for i in range(len(word)):
        if word[i] == guess:
            wordinl[i] = guess
    for i in wordinl:
        print(i, end='')
    print()
    if '_' not in wordinl:
        print('YOU WON')
        guessed = True
