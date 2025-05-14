import random

ROCK = 'r'
PAPER = 'p'
SCISSOR = 's'

print("Welcome to Rock, Paper, Scissors!")
emojis = {ROCK: '🪨', PAPER: '📃', SCISSOR: '✂️'}
choices = tuple(emojis.keys())


def get_user_choice():
    while True:
        user_choice = input("Enter your choice (r for rock, p for paper, s for scissors): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice. Please try again.")


def display_choices(user_choice, computer_choice):
    print(f'Your choice {emojis[user_choice]}')
    print(f'Computer choice {emojis[computer_choice]}')


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Draw')
    elif ((user_choice == ROCK and computer_choice == PAPER) or
          (user_choice == PAPER and computer_choice == SCISSOR) or
          (user_choice == SCISSOR and computer_choice == ROCK)):
        print('You lose')
    elif ((user_choice == PAPER and computer_choice == ROCK) or
          (user_choice == SCISSOR and computer_choice == PAPER) or
          (user_choice == ROCK and computer_choice == SCISSOR)):
        print('You win')


def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        play_again = input("Do you want to continue? (y/n): ").lower()
        if play_again == 'n':
            break

play_game()



