import random

def diceroll():
    roll = random.randint(1, 6) + random.randint(1, 6)
    return roll

def main():
    player1 = input("Enter Player1 name: ")
    player2 = input("Enter Player2 name: ")

    roll1 = diceroll()
    roll2 = diceroll()

    print(player1, "rolled", roll1)
    print(player2, "rolled", roll2)
    if roll2 > roll1:
        print(player2, "won!!")
    elif roll1 > roll2:
        print(player1, "won!!")
    else:
        print("It's a draw between two players")


main()


