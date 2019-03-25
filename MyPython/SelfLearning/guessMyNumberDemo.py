'''
Created on 25-Mar-2019

@author: guruk
'''
import random

print('Hello, I am Python. What is your name?')
name = input()
print("Hello, {} Let's play a game. Can you guess my number between 1 and 20?".format(name))
secretnum = random.randint(1,20)

for i in range(6):
    k = 0;
    try:
        num = int(input("Please take a guess"))
    except Exception as e:
        print('Enter an integer Value')
    if num!=secretnum:
        print("Wrong guess. ", end="")
        if num<secretnum:
            print('Too low.Try again')
        else:
            print("Too high. Try again")
    else:
        print("Right Guess. Well done. You guessed right in {} guesses".format(i+1))
        k =1
        break;

if k ==1:
    pass
else:
    print("The number i was thinking of was ", secretnum)
    print("You have run out of guesses. Bye")
    
        
        
    