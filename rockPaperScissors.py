import random

options=['rock','paper','scissors']
print("Instruction: Type in 'q' to quit.")

while True:
    user_input = input('Rock/Paper/Scissors: ').lower()

    if user_input=='q':
        break

    if user_input not in options:
        print('Your input is not valid.')
        continue

    rand=random.randint(0,2)
    computer_pick= options[rand]
    print(f"Computer picked {computer_pick}.")

    if user_input=='scissors' and computer_pick== 'paper':
        print('You win!')
    elif user_input=='rock' and computer_pick=='scissors':
        print('You win!')  
    elif user_input=='paper' and computer_pick=='rock':
        print('You win!')    
    elif user_input==computer_pick:
        print("It's a tie!!")
    else:
        print('Otu, you lost!!')