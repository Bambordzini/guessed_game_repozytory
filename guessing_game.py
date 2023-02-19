import random

def guess_game(numbers, max_num):
    secret_numbers = [random.randint(1, max_num) for i in range(numbers)]
    for i in range(numbers):
        guess = int(input(f"Enter an integer from 1 to {max_num}: "))
        while secret_numbers[i] != guess:
            if guess < secret_numbers[i]:
                print("guess is low")
                guess = int(input(f"Enter an integer from 1 to {max_num}: "))
            elif guess > secret_numbers[i]:
                print("guess is high")
                guess = int(input(f"Enter an integer from 1 to {max_num}: "))
            else:
                break
        print("you guessed it!")

guess_game(10, 99)
guess_game(10, 49)
