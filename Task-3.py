import random

def get_computer_choice():
    choices = ['stone', 'paper', 'scissors']
    return random.choice(choices)

def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'stone' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'stone') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

def main():
    print("Welcome to Stone, Paper, Scissors!")
    
    while True:
        player_choice = input("Enter your choice (stone, paper, or scissors): ").lower()
        
        if player_choice not in ['stone', 'paper', 'scissors']:
            print("Invalid choice, please try again.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = get_winner(player_choice, computer_choice)
        print(result)
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()
