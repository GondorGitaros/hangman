import random

<<<<<<< HEAD
words = ['windows']
=======
words = ['cat', 'window', 'dog', ]
>>>>>>> 4ef83d075b313010b23b322a6b85777cb7ea0faf
word = random.choice(words)
lword = []

for i in range(len(word)):
    print('_', end=' ')
    lword.append('_')
print()

counter = 0
guessed = False

while not guessed:
    guess = input('Guess a letter: ')
    for i in range(len(lword)):
        if guess == word[i]:
            lword[i] = guess
            print(lword[i], end=' ')
        else:
            print(lword[i], end=' ')
    if '_' not in lword:
        guessed = True
        print('\nYou win!')
    print()
<<<<<<< HEAD
=======

>>>>>>> 4ef83d075b313010b23b322a6b85777cb7ea0faf
