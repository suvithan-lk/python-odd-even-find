number = int(input("Enter a number: "))
if (number % 3 == 0):
    if (number % 5 == 0):
        print(f"{number} is even and divisible by 5 and 3.")
    else:
        print(f"{number} is even but not divisible by 5.")
else:
    print(f"{number} is odd and not divisible by 3.")

# number = int()  # IGNORE ---
# This line is intentionally left as a placeholder and should not be executed.