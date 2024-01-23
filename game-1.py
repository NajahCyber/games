def get_player_move(player):
    while True:
        move = input(f"Player {player}, enter your move (rock/paper/scissors): ").lower()
        if move in ['rock', 'paper', 'scissors']:
            return move
        else:
            print("Invalid move. Please enter rock, paper, or scissors.")

def determine_winner(player1, player2):
    if player1 == player2:
        return "It's a tie!"
    elif (player1 == 'rock' and player2 == 'scissors') or \
         (player1 == 'paper' and player2 == 'rock') or \
         (player1 == 'scissors' and player2 == 'paper'):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

def main():
    print("Welcome to the Rock-Paper-Scissors Game!")

    while True:
        player1_move = get_player_move(1)
        player2_move = get_player_move(2)

        print(f"Player 1 chose {player1_move}")
        print(f"Player 2 chose {player2_move}")

        result = determine_winner(player1_move, player2_move)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    main()
def get_player_move(player):
    while True:
        move = input(f"Player {player}, enter your move (rock/paper/scissors): ").lower()
        if move in ['rock', 'paper', 'scissors']:
            return move
        else:
            print("Invalid move. Please enter rock, paper, or scissors.")

def determine_winner(player1, player2):
    if player1 == player2:
        return "It's a tie!"
    elif (player1 == 'rock' and player2 == 'scissors') or \
         (player1 == 'paper' and player2 == 'rock') or \
         (player1 == 'scissors' and player2 == 'paper'):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

def main():
    print("Welcome to the Rock-Paper-Scissors Game!")

    while True:
        player1_move = get_player_move(1)
        player2_move = get_player_move(2)

        print(f"Player 1 chose {player1_move}")
        print(f"Player 2 chose {player2_move}")

        result = determine_winner(player1_move, player2_move)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    main()
