import random
def pr_green(skk): print("\033[92m {}\033[00m" .format(skk))
def pr_red(skk): print("\033[91m {}\033[00m" .format(skk))


rock = "Rock"
paper = "Paper"
scissors = "Scissors"
player_score = 0
computer_score = 0

choice = ""
print("Let's play a game!")

while True:
    if choice == "q":
        break

    player_move = input("Please make your choice: [r]ock, [p]aper or [s]cissors: ")

    if player_move == "r":
        player_move = rock
        print("You chose Rock.")
    elif player_move == "p":
        player_move = paper
        print("You chose Paper.")
    elif player_move == "s":
        player_move = scissors
        print("You chose Scissors.")
    else:
        raise SystemExit("Invalid Input. Try again...")

    computer_random_number = random.randint(1, 3)
    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock
        print("Computer chose Rock.")
    elif computer_random_number == 2:
        computer_move = paper
        print("Computer chose Paper.")
    elif computer_random_number == 3:
        computer_move = scissors
        print("Computer chose Scissors.")

    if player_move == rock and computer_move == rock or player_move == paper and computer_move == paper or\
            player_move == scissors and computer_move == scissors:
        print("Draw")
    elif player_move == rock and computer_move == scissors or player_move == paper and computer_move == rock or \
            player_move == scissors and computer_move == paper:
        pr_green("You Win!")
        player_score += 1
    elif player_move == rock and computer_move == paper or player_move == paper and computer_move == scissors or \
            player_move == scissors and computer_move == rock:
        pr_red("You Lose!")
        computer_score += 1

    choice = input("Do you want to [q]uit? ")

winner = "Nobody"
if player_score > computer_score:
    winner = "You"
elif player_score < computer_score:
    winner = "Computer"
print(f"Winner is {winner} with score {max(player_score, computer_score)}:{min(player_score, computer_score)}")
