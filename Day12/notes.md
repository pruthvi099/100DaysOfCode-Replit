# 🧠 100 Days of Code – Replit Challenge

[![100DaysOfCode](https://img.shields.io/badge/-100DaysOfCode-black?style=flat-square&logo=python&logoColor=white)](https://www.100daysofcode.com/)  
[![Replit](https://img.shields.io/badge/-Replit-667881?style=flat-square&logo=replit&logoColor=white)](https://replit.com/@p_r_u_t_h_v_i_0_9)  
[![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/pruthvi099)

---

# 🗓️ Day 12 / 100 – 100 Days of Code

## 📅 Date: 2025-08-06  
## 🛠️ Project/Topic: Python – Debugging & Fixing Errors

---

## ✅ What I Did Today

- Fixed a **buggy quiz program**
- Practiced identifying **syntax errors**, **logical errors**, and **input handling issues**
- Learned proper **if-elif-else** structure in Python

---

## 💡 What I Learned

### 🐛 Common Debugging Lessons
| Bug Type             | Example in Code | Fix |
|----------------------|-----------------|-----|
| Missing quotes       | `print("Hello)` | Add closing quote |
| Missing parentheses  | `print "Hi"`    | Use `print("Hi")` |
| Wrong function usage | `ans1 = "text"` instead of `input()` | Use `input()` for user input |
| Wrong condition order| `else` before `elif` | Correct to `if → elif → else` |
| Wrong data type in comparison | Comparing `str` to `int` | Convert input with `int()` |

---

## 🔧 Fixed Code

```python
print("100 Days of Code QUIZ")
print()
print("How many can you answer correctly?")

ans1 = input("What language are we writing in? ").lower()
if ans1 == "python":
    print("Correct")
else:
    print("Nope🙈")

ans2 = int(input("Which lesson number is this? "))

if ans2 > 12:
    print("We're not quite that far yet")
elif ans2 == 12:
    print("That's right!")
else:
    print("We've gone well past that!")
```

---

## 🤔 Why It Matters

- Debugging is **essential** for every programmer  
- Helps **prevent program crashes** and ensures correct logic  
- Builds skill in reading error messages and correcting them efficiently

---

## 😓 Challenges

- Remembering to **check input types** before comparing  
- Finding the **root cause** when multiple errors exist in the same program

---

## 🎯 Goals for Tomorrow

- Start **loop-based programs**
- Create **quiz programs** that repeat until correct answer is given

---

## 💬 Reflection

> Debugging feels like detective work 🔍 — searching for clues in code.  
> Fixing this small quiz program was a good exercise in **careful reading** and **structured problem-solving**.

---

## 🧪 Try It on Replit

[![Run on Replit](https://replit.com/badge/github/pruthvi099/100DaysOfCode-Replit)](https://replit.com/@p_r_u_t_h_v_i_0_9)

---

## 🌐 Connect With Me

* 🧵 Threads: [@p\_r\_u\_t\_h\_v\_i\_0\_9](https://www.threads.com/@iampruthvi_09)  
* 🧑‍💻 GitHub: [pruthvi099](https://github.com/pruthvi099)

---

> 💬 *"A bug is just a puzzle waiting to be solved."*
