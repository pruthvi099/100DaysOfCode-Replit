import random

# Pick a random number between 0 and 1,000,000
secret_number = random.randint(0, 1000000)

attempts = 0

while True:
    guess = int(input("Guess a number between 0 and 1,000,000: "))
    
    # Exit if user enters negative number
    if guess < 0:
        print("🚪 You quit the game. Goodbye!")
        break

    attempts += 1

    if guess < secret_number:
        print("Too low! 📉")
    elif guess > secret_number:
        print("Too high! 📈")
    else:
        print(f"🎉 You got it! The number was {secret_number}.")
        print(f"✅ It took you {attempts} attempts.")
        break

# OUTPUT
# Guess a number between 0 and 1,000,000: 500000
# Too high! 📈
# Guess a number between 0 and 1,000,000: 200000
# Too low! 📉
# Guess a number between 0 and 1,000,000: 350000
# 🎉 You got it! The number was 350000.
# ✅ It took you 3 attempts.
