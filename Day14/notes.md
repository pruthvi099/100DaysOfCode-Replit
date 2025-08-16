# 🧠 100 Days of Code – Replit Challenge

[![100DaysOfCode](https://img.shields.io/badge/-100DaysOfCode-black?style=flat-square&logo=python&logoColor=white)](https://www.100daysofcode.com/)  
[![Replit](https://img.shields.io/badge/-Replit-667881?style=flat-square&logo=replit&logoColor=white)](https://replit.com/@p_r_u_t_h_v_i_0_9)  
[![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/pruthvi099)  

---

# 🗓️ Day 14 / 100 – 100 Days of Code

## 📅 Date: 2025-08-08  
## 🛠️ Project/Topic: Python – Rock, Paper, Scissors (2-Player Edition)

---

## ✅ What I Did Today

- Built a **two-player Rock, Paper, Scissors game** in Python  
- Used `getpass` to hide each player's choice for fair play  
- Added **input validation** so players can use both letters or full words  
- Used **emoji icons** for a fun and visual experience  
- Implemented **winner decision logic** with condition checks  

---

## 💡 What I Learned

### 🎮 Game Logic Essentials  
| Concept | Example | Why it Matters |
|---------|---------|----------------|
| `getpass` | `from getpass import getpass` | Hides input so the second player can’t cheat |
| Input validation | Loop until choice is valid | Prevents errors and enforces rules |
| Normalization | `.strip().lower()` | Handles accidental spaces or capitalization |
| Condition chaining | `(p1 == 'r' and p2 == 's')` | Checks all winning scenarios |
| Mapping choices | `{ 'r': 'Rock', 'p': 'Paper' }` | Makes output user-friendly |

---

## 🔧 Final Code

```python
from getpass import getpass as input

print("🎮 Rock, Paper, Scissors – 2 Player Edition 🪨📄✂️\n")
print("Instructions: Type R for Rock, P for Paper, or S for Scissors.")

# Function to validate and standardize input
def get_choice(player):
    while True:
        choice = input(f"{player}, enter your choice (R/P/S): ").strip().lower()
        if choice in ['r', 'rock']:
            return 'r'
        elif choice in ['p', 'paper']:
            return 'p'
        elif choice in ['s', 'scissors', 'scissor']:
            return 's'
        else:
            print("⚠ Invalid choice! Please enter R, P, or S.")

# Get both players' choices
player1 = get_choice("Player 1")
player2 = get_choice("Player 2")

# Decide the winner
if player1 == player2:
    result = "🤝 It's a tie!"
elif (player1 == 'r' and player2 == 's') or      (player1 == 'p' and player2 == 'r') or      (player1 == 's' and player2 == 'p'):
    result = "🎉 Player 1 wins! 🏆"
else:
    result = "🎉 Player 2 wins! 🏆"

# Show results
choices_map = {'r': '🪨 Rock', 'p': '📄 Paper', 's': '✂️ Scissors'}
print("\n--- Game Results ---")
print(f"Player 1 chose: {choices_map[player1]}")
print(f"Player 2 chose: {choices_map[player2]}")
print(result)
```

---

## 🤔 Why It Matters

- Introduces **two-player game mechanics** in Python  
- Shows the value of **hiding sensitive inputs** in multiplayer scenarios  
- Strengthens **logical thinking** with multiple win/lose/tie conditions  

---

## 😓 Challenges

- Ensuring input was always valid before continuing  
- Remembering **all winning combinations** without missing any  
- Making output clear while keeping code clean  

---

## 🎯 Goals for Tomorrow

- Add a **best-of-3 mode** with score tracking  
- Let players **choose their own names** instead of "Player 1/2"  

---

## 💬 Reflection

> This felt like creating a mini competitive arcade game in the terminal.  
> The `getpass` trick made it surprisingly fair — no more peeking at the screen! 😆  

---

## 🧪 Try It on Replit

[![Run on Replit](https://replit.com/badge/github/pruthvi099/100DaysOfCode-Replit)](https://replit.com/@p_r_u_t_h_v_i_0_9)  
