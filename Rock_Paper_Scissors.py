# Rock, paper, scissors game
import random
computer_wins = 0
user_wins = 0
list = ["rock", "paper", "scissors"]


def computer_pick():
    r = random.randint(0, 2)
    comp_pick = list[r]
    return comp_pick

print("Welcome to Rock, Paper, Scissors!")
while True:

    n = computer_pick()

    answer = input("\nType in rock, paper, scissors or q to quit: ").lower()
    if answer == "q":
        print("     Goodbye")
        break
    if answer not in list:
        print("Invalid input")
        continue

    # generate a random number that a computer will index from a list... as a function

    # conditions
    if answer == "rock" and n == "scissors":
        user_wins += 1
        print("     You win! Computer picked", n)
    elif answer == "paper" and n == "rock":
        user_wins += 1
        print("     You win! Computer picked", n)
    elif answer == "scissors" and n == "paper":
        user_wins += 1
        print("     You win! Computer picked", n)
    elif answer == n:
        print("     You tied, Computer picked", n)
    else:
        computer_wins += 1
        print("     You lose, Computer picked", n)

print("     You won", user_wins, "times!")
print("     Computer won", computer_wins, "times.")

