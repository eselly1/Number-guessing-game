import random 
print('Welcome to the number guessing game!')
difficulty=input("I'm thinking of a number between 1 and 100. Type 'easy' for easy difficulty or type 'hard' for hard difficulty.\n")
while difficulty!='easy' and difficulty!='hard':difficulty=input("I'm thinking of a number between 1 and 100. Type 'easy' for easy difficulty or type 'hard' for hard difficulty.")
if difficulty=='easy':
    attempts=10
else:
    attempts=5

def guess_num(num):
    guess=int(input("Enter a number: "))
    if guess==num:
        print(f'The number was {num}. You guessed it right!')
        return -20
    elif guess>num:
        print('Too high! Try again.')
        return -1
    else: 
        print("Too low! Try again.")
        return -1
    
num=random.randint(0,100)
while attempts>0:
    print(f'Attempts: {attempts}')
    attempts+=guess_num(num)
if attempts==0:
    print(f"Sorry, the number was {num}! You didn't guess in time! Thanks for playing!")
else:
    print('Good game! Thanks for playing!')
playagain=input("Would you like to play again?\n").lower()
while playagain!='y' and playagain!='yes'and playagain!='n' and playagain!='no':playagain=input("Would you like to play again?\n").lower()

while playagain=='y' or playagain=='yes':
    difficulty=input("I'm thinking of a number between 1 and 100. Type 'easy' for easy difficulty or type 'hard' for hard difficulty.\n")
    while difficulty!='easy' and difficulty!='hard':difficulty=input("I'm thinking of a number between 1 and 100. Type 'easy' for easy difficulty or type 'hard' for hard difficulty.")
    if difficulty=='easy':
        attempts=10
    else:
        attempts=5
    num=random.randint(0,100)
    while attempts>0:
        print(f'Attempts: {attempts}')
        attempts+=guess_num(num)
    if attempts==0:
        print(f"Sorry, the number was {num}! You didn't guess in time! Thanks for playing!")
    else:
        print('Good game! Thanks for playing!')
    playagain=input("Would you like to play again?\n").lower()
    while playagain!='y' and playagain!='yes'and playagain!='n' and playagain!='no':playagain=input("Would you like to play again?\n").lower()
print('Thanks for playing!')