import random

player_score = 0
Letter_Choice = []
player_life = 5


def game():
    # Define List of word
    list_word = ["aback", "abaft", "abandoned", "abashed", "aberrant", "abhorrent", "abiding", "abject", "ablaze",
                 "able", "abnormal", "aboard", "aboriginal", "abortive", "abounding", "abrasive", "abrupt", "absent",
                 "absorbed", "absorbing", "abstracted", "absurd", "abundant", "abusive", "accept", "acceptable",
                 "accessible", "accidental", "account", "accurate", "achiever", "acid", "acidic", "acoustic",
                 "acoustics", "acrid", "act", "action", "activity", "actor", "actually", "ad hoc", "adamant",
                 "adaptable", "add", "addicted", "addition", "adhesive", "adjoining", "adjustment", "admire", "admit",
                 "adorable", "adventurous", "advertisement", "advice", "advise", "afford", "afraid", "aftermath",
                 "afternoon", "afterthought", "aggressive", "agonizing", "agree", "agreeable", "agreement", "ahead",
                 "air", "airplane", "airport", "ajar", "alarm", "alcoholic", "alert", "alike", "alive", "alleged",
                 "allow", "alluring", "aloof", "amazing", "ambiguous", "ambitious", "amount", "amuck", "amuse",
                 "amused", "amusement", "amusing", "analyze", "ancient", "anger", "angle", "angry", "animal",
                 "animated", "announce", "annoy", "annoyed", "annoying", "answer", "ants", "anxious", "apathetic",
                 "apologise", "apparatus", "apparel", "appear", "applaud", "appliance", "appreciate", "approval",
                 "approve", "aquatic", "arch", "argue", "argument", "arithmetic", "arm", "army", "aromatic", "arrange",
                 "arrest", "arrive", "arrogant", "art", "ashamed", "ask", "aspiring", "assorted", "astonishing",
                 "attach", "attack", "attempt", "attend", "attract", "attraction", "attractive", "aunt", "auspicious",
                 "authority", "automatic", "available", "average", "avoid", "awake", "aware", "awesome", "awful",
                 "axiomatic", "babies", "baby", "back", "bad", "badge", "bag", "bait", "bake", "balance", "ball", "ban",
                 "bang", "barbarous", "bare", "base", "baseball", "bashful", "basin", "basket", "basketball", "bat",
                 "bath", "bathe", "battle", "bawdy", "bead", "beam", "bear", "beautiful", "bed", "bedroom", "beds",
                 "bee", "beef", "befitting", "beg", "beginner", "behave", "behavior", "belief", "believe", "bell"]
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
            playAgain()
            break
        Players_Character = str(input(
            "Type 1 letter : "))
        while(len(Players_Character) != 1 or not Players_Character.isalpha()):
            Players_Character = input(
                "Please type 1 letter alpha : ")
        number = int(IsInTheWord(Players_Character,
                     computer_choice))
        if(number == 0 and player_life > 0):
            print("You win !")
            playAgain()


def playAgain():
    All_possibility = ["y", "n"]
    play_again = (input("Play again ? [Type y for yes] [Type n for no] : "))
    while(not play_again in All_possibility):
        play_again = input(
            "Please : [Type y for yes] [Type n for no] :")
    if(play_again == "y"):
        global player_life
        player_life = 5
        game()
    else:
        print("Good bye !")

# function check if input letter is in the word with lower case all


def IsInTheWord(Players_Character, computer_choice):
    word_split = split(computer_choice)
    # if yes print letter like ---a---a with - other letter of the word
    # To do : check if letter already use
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


def split(word):
    return [char for char in word]


if __name__ == "__main__":
    game()
