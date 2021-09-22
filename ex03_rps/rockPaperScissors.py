import random

player_score = 0
computer_score = 0


def game():
    All_Moves = ["r", "p", "s"]
    Players_Moves = input(
        "How to Play : [Type r for Rock] [Type p for Paper] [Type s for Scissors]")
    while(not Players_Moves in All_Moves):
        Players_Moves = input(
            "Please : [Type r for Rock] [Type p for Paper] [Type s for Scissors]")

    Computer_Moves = random.choice(All_Moves)
    print("Player : " + Players_Moves + " vs Computer : "+Computer_Moves)
    battle(Computer_Moves, Players_Moves)
    playAgain()


def playAgain():
    All_possibility = ["y", "n"]
    play_again = (input("Play again ? [Type y for yes] [Type n for no]"))
    while(not play_again in All_possibility):
        play_again = input(
            "Please : [Type y for yes] [Type n for no]")

    if(play_again == "y"):
        game()
    else:
        print("Good bye !")


def battle(Computer_Moves, Players_Moves):
    c_win = "Computer win"
    p_win = "Player win"
    equal = "Nobody win"

    if(Players_Moves == "r" and Computer_Moves == "s"):
        +(+player_score + str(player_score))
        print(p_win)
    elif(Players_Moves == "r" and Computer_Moves == "p"):
        +(+computer_score + str(computer_score))
        print(c_win)
    elif(Players_Moves == "r" and Computer_Moves == "r"):
        print(equal)

    if(Players_Moves == "p" and Computer_Moves == "r"):
        +(+player_score)
        print(p_win + str(player_score))
    elif(Players_Moves == "p" and Computer_Moves == "s"):
        +(+computer_score + str(computer_score))
        print(c_win)
    elif(Players_Moves == "p" and Computer_Moves == "p"):
        print(equal)

    if(Players_Moves == "s" and Computer_Moves == "p"):
        +(+player_score)
        print(p_win + str(player_score))
    elif(Players_Moves == "s" and Computer_Moves == "r"):
        +(+computer_score)
        print(c_win + str(computer_score))
    elif(Players_Moves == "s" and Computer_Moves == "s"):
        print(equal)


if __name__ == "__main__":
    game()
