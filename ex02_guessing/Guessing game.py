import random
Constant_life = 3
life = Constant_life


def game():
    first_number = int(input("Enter the first number : "))
    second_number = int(input("Enter the second number : "))
    if(first_number >= second_number):
        while(first_number >= second_number):
            second_number = int(
                input("Please enter the second number superior to first number : "))
            if first_number < second_number:
                random_number = random.randint(first_number, second_number)
                print(random_number)
                break
    else:
        random_number = random.randint(first_number, second_number)
        # print(random_number)
    CheckNumber(random_number)


def playAgain():
    All_possibility = ["y", "n"]
    play_again = (input("Play again ? [Type y for yes] [Type n for no] : "))
    while(not play_again in All_possibility):
        play_again = input(
            "Please : [Type y for yes] [Type n for no] : ")
    if(play_again == "y"):
        global life
        life = Constant_life
        game()
    else:
        print("Good bye !")


def CheckNumber(random_number):
    print("Let's game !")
    global life
    number = int(input("Enter number : "))
    while(random_number != number):
        if(life == 0):
            print("perdu !")
            break
        elif(random_number > number):
            print("Plus grand !")
            life -= 1
            print("Nombre de vie : " + str(life))
            if(life > 0):
                number = int(input("Enter number : "))
        elif(random_number < number):
            print("Plus petit !")
            life -= 1
            print("Nombre de vie : " + str(life))
            if(life > 0):
                number = int(input("Enter number : "))

    if(random_number == number and life > 0):
        print("Bien joué !")
    playAgain()


if __name__ == "__main__":
    game()
