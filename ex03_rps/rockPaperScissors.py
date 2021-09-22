import random

player_score = 0
computer_score = 0


def game():
    All_Moves = ["r", "p", "s"]
    Players_Moves = input(
        "How to Play : [Type r for Rock] [Type p for Paper] [Type s for Scissors] : ")
    while(not Players_Moves in All_Moves):
        Players_Moves = input(
            "Please : [Type r for Rock] [Type p for Paper] [Type s for Scissors] :")

    Computer_Moves = random.choice(All_Moves)
    print("Player : " + Players_Moves + " vs Computer : "+Computer_Moves)
    battle(Computer_Moves, Players_Moves)
    playAgain()


def playAgain():
    All_possibility = ["y", "n"]
    play_again = (input("Play again ? [Type y for yes] [Type n for no] : "))
    while(not play_again in All_possibility):
        play_again = input(
            "Please : [Type y for yes] [Type n for no] : ")

    if(play_again == "y"):
        game()
    else:
        print("Good bye !")


def battle(Computer_Moves, Players_Moves):
    global player_score
    global computer_score
    if(Players_Moves == "r" and Computer_Moves == "s" or Players_Moves == "p" and Computer_Moves == "r" or Players_Moves == "s" and Computer_Moves == "p"):
        player_score += 1
        print("Player win - player score: " + str(player_score))
        print("computer score : " + str(computer_score))
    elif(Players_Moves == "r" and Computer_Moves == "p" or Players_Moves == "p" and Computer_Moves == "s" or Players_Moves == "s" and Computer_Moves == "r"):
        computer_score += 1
        print("Computer win  - player score: " + str(player_score))
        print("computer score : " + str(computer_score))
    elif(Players_Moves == "r" and Computer_Moves == "r" or Players_Moves == "p" and Computer_Moves == "p" or Players_Moves == "s" and Computer_Moves == "s"):
        print("Nobody win")


if __name__ == "__main__":
    game()
