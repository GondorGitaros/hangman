import random

words = ['window', 'cat', 'dog']
word = random.choice(words)
lword = []

for i in range(len(word)):
    print('_', end='')
    lword.append('_')
print()

while True:
    guess = input("guess: ")
    for i in range(len(word)):
        if guess == word[i]:
            lword[i] = guess
    if '_' not in lword:
        print('you won', end='')
        break
    for i in lword:
        print(i, end='')
    print()
