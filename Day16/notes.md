# 🧠 100 Days of Code – Replit Challenge

[![100DaysOfCode](https://img.shields.io/badge/-100DaysOfCode-black?style=flat-square&logo=python&logoColor=white)](https://www.100daysofcode.com/)
[![Replit](https://img.shields.io/badge/-Replit-667881?style=flat-square&logo=replit&logoColor=white)](https://replit.com/)

---

## 📅 Day 16 / 100 – While Loops (Continue or Exit Program)

### 🚀 Challenge of the Day:
Learned how to use **while loops** to keep a program running until the user decides to exit.  
Created a simple program that asks the user if they want to continue, and only stops when they type `n`.

---

### 💻 Code Written:

```python
while True:
    answer = input("Do you want to continue? (y/n): ").strip().lower()
    if answer == "n":
        print("👋 Goodbye!")
        break  # exits the loop
    else:
        print("🚀 Let's keep going!")
```

---

### 🎯 Example Output:

```
Do you want to continue? (y/n): y
🚀 Let's keep going!
Do you want to continue? (y/n): y
🚀 Let's keep going!
Do you want to continue? (y/n): n
👋 Goodbye!
```

---

### ✅ Win of the Day:
- Practiced **infinite loops** with `while True`
- Learned how to **break out of loops**
- Made my program feel interactive 🔄

---

### 🎯 Next Goal:
Use `while` loops to build a **guessing game** with attempts counter! 🎮

---
