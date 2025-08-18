# 🧠 100 Days of Code – Replit Challenge

[![100DaysOfCode](https://img.shields.io/badge/-100DaysOfCode-black?style=flat-square&logo=python&logoColor=white)](https://www.100daysofcode.com/)  
[![Replit](https://img.shields.io/badge/-Replit-667881?style=flat-square&logo=replit&logoColor=white)](https://replit.com/@p_r_u_t_h_v_i_0_9)  
[![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/pruthvi099)  

---

# 🗓️ Day 15 / 100 – 100 Days of Code

## 📅 Date: 2025-08-09  
## 🛠️ Project/Topic: Python – Guess the Number (Replay Mode)

---

## ✅ What I Did Today

- Built a **Guess the Number game** in Python  
- Used `random.randint()` to generate a hidden number  
- Implemented **while loops** for repeated guessing  
- Added **feedback messages** (`Too high!`, `Too low!`)  
- Included a **play again option** so users can retry multiple times  

---

## 💡 What I Learned

### 🔢 Game Mechanics Essentials  
| Concept | Example | Why it Matters |
|---------|---------|----------------|
| `random.randint(1, 100)` | Picks a number between 1–100 | Creates unpredictability |
| While loop | `while True:` | Keeps the game running until user wins or quits |
| Input casting | `int(input())` | Converts user guess to integer for comparison |
| Feedback system | `if guess < number:` | Guides the player closer to the answer |
| Replay option | `play_again = input(...)` | Makes the game more fun and reusable |

---

## 🔧 Final Code

```python
import random

print("🎯 Welcome to the Guess the Number Game!\n")

# Main game loop
while True:
    number = random.randint(1, 100)
    attempts = 0

    print("I have chosen a number between 1 and 100. Can you guess it?")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("📉 Too low! Try again.")
        elif guess > number:
            print("📈 Too high! Try again.")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts! 🏆")
            break

    # Replay option
    play_again = input("\nDo you want to play again? (Y/N): ").strip().lower()
    if play_again != 'y':
        print("👋 Thanks for playing! Goodbye!")
        break
```

---

## 🤔 Why It Matters

- Strengthens understanding of **loops** and **conditional logic**  
- Reinforces **user interaction** and **input handling**  
- Demonstrates how **randomness** makes games engaging  

---

## 😓 Challenges

- Preventing program crash if user entered non-numeric input  
- Balancing difficulty (deciding range 1–100 felt right)  
- Ensuring replay loop didn’t restart incorrectly  

---

## 🎯 Goals for Tomorrow

- Add **difficulty levels** (Easy: 1–20, Hard: 1–200)  
- Handle **invalid inputs** gracefully (no crashes)  
- Track **best score (fewest attempts)** across rounds  

---

## 💬 Reflection

> This project felt rewarding — small changes like replay mode made it way more fun.  
> Guessing games really helped me see the power of **loops + conditions + randomness** in action! 🎲  

---

## 🧪 Try It on Replit

[![Run on Replit](https://replit.com/badge/github/pruthvi099/100DaysOfCode-Replit)](https://replit.com/@p_r_u_t_h_v_i_0_9)  
