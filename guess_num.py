import random

print("Hello World! Welcome to the Number Guessing Game.")
print("In this game, you will guess a number between a specified range.")
print("You have 7 chances to guess the correct number.")
print("Let's begin!")

num1 = int(input("Enter the Lower Bound: "))
num2 = int(input("Enter the Upper Bound: "))

print(f"\nYou have 7 chances to guess the number between {num1} and {num2}. Let's start!")

num = random.randint(num1, num2) 
chance = 7                       
count = 0                       

while count < chance:
    count += 1
    guess = int(input('Enter your guess: '))

    if guess == num:
        print(f'Correct! The number is {num}. You guessed it in {count} attempts.')
        break

    elif count >= chance and guess != num:
        print(f'orry! The number was {num}. Better luck next time.')

    elif guess > num:
        print('Too high! Try a lower number.')

    elif guess < num:
        print('Too num1! Try a higher number.')