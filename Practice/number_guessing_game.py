import random

from art import  logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("Think of aNumber between 1 an 100.")
level = input("Choose difficulty . Type 'easy' or 'hard' : ").lower()

Correct_number = random.randrange(1,100)

print(Correct_number)
i=10
j=5
if level=='easy':
    while i > 0 :
        print(f"You have {i} attempts remaining to guess the number.")
        user_guess=int(input("Make a guess : "))
        if user_guess == Correct_number:
            print("You Guessed Correctly , You WON")
            break
        elif user_guess > Correct_number:
            print("Too High")
            print("Guess Again!")
        else:
            print("Too Low")
            print("Guess Again!")
        i=i-1
    print("You've run out of guesses.Run the code to run again.")
elif level == 'hard':
    while j > 0 :
        print(f"You have {j} attempts remaining to guess the number.")
        user_guess=int(input("Make a guess : "))
        if user_guess == Correct_number:
            print("You Guessed Correctly , You WON")
            break
        elif user_guess > Correct_number:
            print("Too High")
            print("Guess Again!")
        else:
            print("Too Low")
            print("Guess Again!")
        j=j-1
    print("You've run out of guesses.Run the code to run again.")
else :
    print("Error While Selecting level")
    print("Please Select the level correctly")

