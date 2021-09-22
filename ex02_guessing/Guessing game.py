import random


def askdelimiter():
    first_number = int(input("Enter the first number : "))
    second_number = int(input("Enter the second number : "))
    if(first_number > second_number):
        while(first_number > second_number):
            second_number = int(
                input("Please enter the second number superior to first number : "))
            if first_number < second_number:
                random_number = random.randint(first_number, second_number)
                print(random_number)
                break
    else:
        random_number = random.randint(first_number, second_number)
        print(random_number)
    return random_number


def game(random_number):
    print("Let's game !")
    life = 3
    number = int(input("Enter number : "))
    while(random_number != number):
        if(life < 1):
            print("perdu !")
            break
        elif(random_number > number):
            print("Plus grand !")
            life = life-1
            print("Nombre de vie : " + str(life))
            number = int(input("Enter number : "))
        elif(random_number < number):
            print("Plus petit !")
            life = life-1
            print("Nombre de vie : " + str(life))
            number = int(input("Enter number : "))
        elif(random_number == number):
            print("Bien joué !")
            break


if __name__ == "__main__":

    random_number = askdelimiter()
    game(random_number)
