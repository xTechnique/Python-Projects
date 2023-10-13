import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
attempts = 0
play = True
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "hard":
    attempts += 5
    print("you have 5 attempts")
else:
    attempts += 10
    print("you have 10 attempts")
ran_number = random.choice(range(0, 101))
while play == True:
    for i in range(1):
        player_guess = int(input("Make a guess: "))
        if ran_number == player_guess:
            print("You win, good guess!")
            play = False
        if attempts == 1:
            print("You ran out of attempts! The number was", ran_number)
            play = False
        if ran_number > player_guess:
            attempts -= 1
            print("Too low, guess again")
            print(f"{attempts} left")
        if ran_number < player_guess:
            attempts -= 1
            print("Too high, guess again")
            print(f"{attempts} left")

