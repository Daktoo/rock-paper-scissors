import random
import time

def greeting():
    print("--------------------------------------------------")
    print(" ")
    print('Welcome to the Dakto INC Rock Paper Scissors game!')
    print(" ")
    print("--------------------------------------------------")
    print(" ")

def farewell():
    print(" ")
    print("-------------------------------------------------------------")
    print(" ")
    print('Thank you for playing the Dakto INC Rock Paper Scissors game.')
    print('Website: https://www.daktoinc.co.uk')
    print('GitHub: https://github.com/Daktoo')
    print(" ")
    print("-------------------------------------------------------------")

def computer_chooses():
    return random.choice(['rock', 'paper', 'scissors', 'shoot'])

def user_chooses():
    choice = input("Rock, Paper, Scissors or Shoot?: ").strip().lower()
    while choice not in ['rock', 'paper', 'scissors', 'shoot']:
        choice = input("Invalid choice. Please enter rock, paper, scissors or shoot: ").strip().lower()
    return choice

def who_wins(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'shoot' and computer_choice == 'paper') or \
         (user_choice == 'shoot' and computer_choice == 'scissors'):
        return "win"
    else:
        return "lose"

def play_game():
    score = 0
    rounds = 20

    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}")
        user_choice = user_chooses()
        computer_choice = computer_chooses()
        print(f"Computer chose: {computer_choice}")

        result = who_wins(user_choice, computer_choice)
        if result == "win":
            print("You win this round! :D")
            score += 1
        elif result == "lose":
            print("You lose this round! :(")
        else:
            print("It's a tie!")
        time.sleep(0.5)

    print("\nGame Over!")
    print(f"Your final score: {score}/{rounds}")

greeting()
time.sleep(1)
play_game()
time.sleep(1)
farewell()
