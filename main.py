# Name: Sothea Sorn, Amy Igarashi, Akshar Mehta
# Date: 1/27/25
# Description: This program takes user input to guess the location of the queen in a set of three cards.
# The player also bets an amount out of $100 on their guess. The player can continue to play rounds until they run
# out of money to bet or they quit the program.
import random
import check_input

def main():
    print("-Three Card Monte-")
    print("Find the queen to double your bet!")

    # Initialize user's money
    money = 100

    # Game loops until player runs out of money to bet
    while money > 0:
        print(f"You have ${money}.")

        # Get user's bet
        bet = check_input.get_int_range(f"How much do you want to bet? ", 1, money)

        # Randomize queen's position within the three cards.
        queen_position = random.randint(1, 3)

        # Display the cards
        print("+-----+ +-----+ +-----+")
        print("|     | |     | |     |")
        print("|  1  | |  2  | |  3  |")
        print("+-----+ +-----+ +-----+")

        # Get user's guess
        guess = check_input.get_int_range("Find the queen (1, 2, or 3): ", 1, 3)

        # Reveal the cards
        print("+-----+ +-----+ +-----+")
        for i in range(1, 4):
            if i == queen_position:
                print("|  Q  |", end=" ")
            else:
                print("|  K  |", end=" ")
        print()
        print("+-----+ +-----+ +-----+")

        # Check if user guessed correctly
        if guess == queen_position:
            print("You got lucky this time...")
            money += bet
        else:
            print("Sorry... you lose.")
            money -= bet

        # Check if user wants to play again
        if money > 0:
            if not check_input.get_yes_no("Play again? (Y/N): "):
                break

    print("You're out of money. Beat it, loser!")


if __name__ == "__main__":
    main()
