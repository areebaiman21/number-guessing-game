import random
n = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
p = input("which level do you want to play? Type 'easy' or 'hard': ").lower()
print("I'm thinking of a number between 1 and 100.")

if p in ["easy", "EASY", "Easy"]:
    attempts = 10
elif p in ["hard", "HARD", "Hard"]:
    attempts = 5
else:
    print("Invalid input. Please type 'easy' or 'hard'.")
    exit()

g = int(input("Enter your guess: "))

while True:
    if g < n:
        g = int(input("Too low! Try again: "))
    elif g > n:
        g = int(input("Too high! Try again: "))
    else:
        print("Congratulations! You guessed it!")
        break
    attempts -= 1
    if attempts == 0:
        print("You've run out of attempts. The number was:", n)
        break