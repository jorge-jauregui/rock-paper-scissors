print("Hello, I'm in the mood to play rock-paper-scissors. Let's play!")

import random
a = ('Rock', 'Paper', 'Scissors') #computer choice
chances = 0
ai_choice = random.choice(a)

while chances < 10000000:
    user_choice = input("Type your choice (rock, paper, or scissors): " ) #player choice
    if ai_choice == 'Rock' and user_choice == 'paper':
        print("My choice was rock. You won!") #user won
        break
    if ai_choice == 'Paper' and user_choice == 'scissors':
        print("My choice was paper. You won!") #user won
        break
    if ai_choice == 'Scissors' and user_choice == 'rock':
        print("My choice was scissors. You won!") #user won
        break
    elif ai_choice == 'Rock' and user_choice == 'scissors':
        print("My choice was rock. You lost!") #user lost
        break
    elif ai_choice == 'Paper' and user_choice == 'rock':
        print("My choice was paper. You lost!") #user lost
        break
    elif ai_choice == 'Scissors' and user_choice == 'paper':
        print("My choice was scissors. You lost!")
        break
    else:
        print("My choice was also " + str(ai_choice) + ". Again?")
        break



#if i'm feeling ambitious: make the game 'best of three'
