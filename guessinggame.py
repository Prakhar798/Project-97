number = 14
print("Number Guessing Game")
print("Guess a number between 1 and 20")
chances = 0

while chances < 5:
    guess = int(input("Enter your guess :"))
    if guess > 14:
        print("Your guess was too high.")
        chances += 1
    if guess < 14:
        print("Your guess was too low.")
        chances += 1
    if not chances < 5:
        print("You lose the number is 14.")
    if guess == number:
        print("Congratulations you won!!!")
        break