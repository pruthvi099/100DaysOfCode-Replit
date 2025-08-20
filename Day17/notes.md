# 🧠 100 Days of Code -- Replit Challenge

[![100DaysOfCode](https://img.shields.io/badge/-100DaysOfCode-black?style=flat-square&logo=python&logoColor=white)](https://www.100daysofcode.com/)
[![Replit](https://img.shields.io/badge/-Replit-667881?style=flat-square&logo=replit&logoColor=white)](https://replit.com/)

------------------------------------------------------------------------

## 📅 Day 17 / 100 -- Corridor Adventure with While Loops

### 🚀 Challenge of the Day:

Built an **interactive corridor adventure game** using `while True`,
`break`, and `continue`.\
The program loops until the player makes a choice that ends the game.

------------------------------------------------------------------------

### 💻 Code Written:

``` python
while True:
    print("You are in a corridor, do you go left or right?")
    direction = input("> ").lower()

    if direction == "left":
        print("You have fallen to your death 💀")
        break
    elif direction == "right":
        print("You move forward into the darkness... 🌌")
        continue
    else:
        print("That's not a valid choice, try again!")
```

------------------------------------------------------------------------

### 🎯 Example Output:

    You are in a corridor, do you go left or right?
    > right
    You move forward into the darkness... 🌌
    You are in a corridor, do you go left or right?
    > right
    You move forward into the darkness... 🌌
    You are in a corridor, do you go left or right?
    > left
    You have fallen to your death 💀

------------------------------------------------------------------------

### ✅ Win of the Day:

-   Practiced **infinite loops** with `while True`
-   Learned the difference between **break** (exit loop) and
    **continue** (repeat loop)
-   Built a **mini text adventure game** 🕹️

------------------------------------------------------------------------

### 🎯 Next Goal:

Create a **number guessing game** with `while` loops and attempt
tracking! 🔢
