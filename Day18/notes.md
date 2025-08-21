# 🧠 100 Days of Code -- Replit Challenge

[![100DaysOfCode](https://img.shields.io/badge/-100DaysOfCode-black?style=flat-square&logo=python&logoColor=white)](https://www.100daysofcode.com/)
[![Replit](https://img.shields.io/badge/-Replit-667881?style=flat-square&logo=replit&logoColor=white)](https://replit.com/)

------------------------------------------------------------------------

## 📅 Day 18 / 100 -- Guess the Number 🎮

### 🚀 Challenge of the Day:

Built a **guessing game** where the computer picks a number and the user
keeps guessing until they get it right! Learned how to use loops,
counters, and exit conditions.

------------------------------------------------------------------------

### 💻 Code Written:

``` python
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
```

------------------------------------------------------------------------

### 🎯 Example Output:

    Guess a number between 0 and 1,000,000: 500000
    Too high! 📈
    Guess a number between 0 and 1,000,000: 200000
    Too low! 📉
    Guess a number between 0 and 1,000,000: 350000
    🎉 You got it! The number was 350000.
    ✅ It took you 3 attempts.

------------------------------------------------------------------------

### ✅ Win of the Day:

-   Practiced **random numbers** with `random.randint()`
-   Used a **counter** to track attempts
-   Added a **special exit condition** with negative numbers
-   Built a fully working **guessing game** 🕹️

------------------------------------------------------------------------

### 🎯 Next Goal:

Enhance the game with **difficulty levels** (easy, medium, hard) that
change the number range!
