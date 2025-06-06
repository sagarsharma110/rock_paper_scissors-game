import random

emojis = {'r': '🪨', 'p': '📝', 's': '✂️'}
choices = ['r', 'p', 's']

while True:
    user_choose = input("Rock, Paper, Scissor? (r/p/s): ").lower()
    
    if user_choose not in choices:
        print("Invalid choice!")

    else:
        computer_choice = random.choice(choices)
        print(f"You choose: {emojis[user_choose]}")
        print(f"Computer choose: {emojis[computer_choice]}")

        if user_choose == computer_choice:
            print("Match Tie!")
        elif ((user_choose == 'r' and computer_choice == 's') or (user_choose == 'p' and computer_choice == 'r') or (user_choose == 's' and computer_choice == 'p')):
            print("You Win!")
        else:
            print("You loose!")

        more = input("Do you wanna to play more or not? (press any key to continue or 'n' for quit the game):").lower()
        if more == 'n':
            break