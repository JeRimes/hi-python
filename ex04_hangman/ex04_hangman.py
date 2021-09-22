import random

player_score = 0
Letter_Choice = []
player_life = 5


def game():
    # Define List of word
    list_word = ["cool", "poutre", "chambre"]
    # Select word
    computer_choice = random.choice(list_word)
    print(computer_choice)
    # print number letter
    print("Nombre de lettres : " + str(len(computer_choice)))
    number = len(computer_choice)
    # ask user a letter
    while(number != 0):
        if(player_life == 0):
            print("you lose !")
            break
        Players_Character = str(input(
            "Type 1 letter"))
        # while(len(Players_Character) != 1 or type(Players_Character) is not str):
        #     Players_Character = input(
        #         "Type 1 letter")
        number = int(IsInTheWord(Players_Character,
                     computer_choice))
        if(number == 0 and player_life > 0):
            print("You win !")
# function check if input letter is in the word with lower case all


def IsInTheWord(Players_Character, computer_choice):
    word_split = split(computer_choice)
    # if yes print letter like ---a---a with - other letter of the word
    if(Players_Character.lower() in computer_choice.lower()):
        # Enregistre toute les bonnes lettres en input
        Letter_Choice.append(Players_Character)
    else:
        global player_life
        player_life -= 1

    word = revealLetter(word_split)
    print(word)
    print("Plus que : " + str(word.count("-")) +
          " lettres et Nombre de vie : " + str(player_life))
    return word.count("-")


def revealLetter(word_split):
    word_to_reavel = ""
    for i in word_split:
        if(i in Letter_Choice):
            word_to_reavel = word_to_reavel+i
        else:
            word_to_reavel = word_to_reavel + "-"
    return word_to_reavel
    # revealLetter.count("-")


def split(word):
    return [char for char in word]


if __name__ == "__main__":
    game()
