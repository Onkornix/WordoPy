import words2 as words
import random

def win():
    print('\n##########################\n#CONGRATULATIONS YOU WON!#\n##########################\n')
    exit()

word = str(random.choice(words.list))
correctLetList = [word[0], word[1], word[2], word[3], word[4]]
def play():
    
    guess = input('\nguess a word: ')
    if guess == word:
        win()
    guessletlist = [guess[0], guess[1], guess[2], guess[3], guess[4], ]
    guesscompare = guess in words.list
    if len(guess) < 5:
            print('five letters please')
            play()
    elif guesscompare == False:
        print('that doesn\'t word actually')
        play()
    num=0
    for glet in guessletlist:
        if glet == correctLetList[num]:
            print(glet.upper()+' | green')
        elif glet == correctLetList[1]:
            print(glet.upper()+' | yellow')
        elif glet == correctLetList[2]:
            print(glet.upper()+' | yellow')
        elif glet == correctLetList[3]:
            print(glet.upper()+' | yellow')
        elif glet == correctLetList[4]:
            print(glet.upper()+' | yellow')
        else:
            print(glet.upper()+' | gray')
        num=num+1
    play()
if input('play (y/n)\n' ) == 'y':
    play()
else:
    pass
print('well done!')
exit

