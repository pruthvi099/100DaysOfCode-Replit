

---

# Day 4 – 100DaysOfCode

📅 **Date:** 2025-07-08
🛠️ **Project/Topic:** Python Adventure Simulator + Colorful Console Output

---

## ✅ **What I Did Today**

* Built an **Interactive Adventure Simulator** in Python
* Used **`input()`** to collect data from the user
* Learned about **ANSI escape codes** to add **colors and bold text** in the terminal

---

## 💡 **What I Learned**

* How to **gather multiple inputs** and use **f-strings** to build a personalized story
* How to make terminal output **colorful and engaging** using **`\033[xxm` ANSI codes**

### 🔧 **Code Example:**

```python
print("\033[96mWelcome to your adventure simulator!\033[0m")
print("\033[93mI am going to ask you a bunch of questions and then create an epic story with you as the star!\033[0m\n")

# Inputs
name = input("\033[1mWhat is your name? \033[0m")
enemy = input("\033[1mWhat is your worst enemy’s name? \033[0m")
superpower = input("\033[1mWhat is your superpower? \033[0m")
location = input("\033[1mWhere do you live? \033[0m")
fav_food = input("\033[1mWhat is your favorite food? \033[0m")

# Story Output
print()
print(f"Hello \033[92m{name}\033[0m! Your ability to \033[95m{superpower}\033[0m will make sure you never have to look at \033[91m{enemy}\033[0m again.")
print(f"Go eat \033[93m{fav_food}\033[0m as you walk down the streets of \033[94m{location}\033[0m and use \033[95m{superpower}\033[0m for good and not evil!")
```

---

## 🎨 **Colors Used:**

| Color  | ANSI Code  |
| ------ | ---------- |
| Cyan   | `\033[96m` |
| Yellow | `\033[93m` |
| Green  | `\033[92m` |
| Purple | `\033[95m` |
| Red    | `\033[91m` |
| Blue   | `\033[94m` |
| Bold   | `\033[1m`  |
| Reset  | `\033[0m`  |

---

## 😓 **Challenges**

* Figuring out how **ANSI codes** work and where to place them inside **f-strings**
* Making sure text resets properly after each color

---

## 🎯 **Goals for Tomorrow**

* Use **`elif` statements** to build a **login system with multiple users**
* Learn about **nested `if` statements** for advanced logic

---

## 💬 **Reflection**

> Today was fun! Adding **colors to the terminal** made my project feel alive.
> It’s cool to see how small details can make a big difference in the user experience! 🚀
> \#Python #100DaysOfCode #Replit #LearningToCode

---


