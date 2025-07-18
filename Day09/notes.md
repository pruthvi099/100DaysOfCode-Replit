Here’s your **Day 9 – 100 Days of Code** markdown file (complete and ready to add beside your other logs):

---

````markdown
# 🧠 100 Days of Code – Replit Challenge

[![100DaysOfCode](https://img.shields.io/badge/-100DaysOfCode-black?style=flat-square&logo=python&logoColor=white)](https://www.100daysofcode.com/)
[![Replit](https://img.shields.io/badge/-Replit-667881?style=flat-square&logo=replit&logoColor=white)](https://replit.com/@p_r_u_t_h_v_i_0_9)
[![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/pruthvi099)

---

# 🗓️ Day 9 / 100 – 100 Days of Code

## 📅 Date: 2025-07-12  
## 🛠️ Project/Topic: Python – `int()` vs `float()` (Type Casting)

---

## ✅ What I Did Today

- Learned how to **compare numbers using `if` statements**
- Practiced **type casting** using `int()` and `float()`
- Understood why `input()` returns a **string** by default
- Fixed a **type error** by converting string input to numbers before comparison

---

## 💡 What I Learned

### 🧠 **Type Casting Basics**

| Function  | Use For          | Example    |
|-----------|-----------------|------------|
| `int()`   | Whole numbers    | 10, 42     |
| `float()` | Decimal numbers  | 3.14, 2.75 |
| `str()`   | Text conversion  | "100"      |

---

### 🔧 **Code Example – Score Checker**

#### Without Casting (Error)

```python
myScore = input("Your score: ")

if myScore > 100000:
    print("Winner!")
else:
    print("Try again 😭")
````

#### With `int()` – Fixed Version

```python
myScore = int(input("Your score: "))

if myScore > 100000:
    print("Winner!")
else:
    print("Try again 😭")
```

#### With `float()` – For Decimal Support

```python
myScore = float(input("Your score (decimals allowed): "))

if myScore > 100000:
    print("Winner!")
else:
    print("Try again 😭")
```

---

## 🖥️ Output Example

```
Your score: 150000
Winner! 🏆
```

```
Your score: 50000
Try again 😭
```

---

## 🔍 Why This Matters

* **`input()` always returns text**
* Use **`int()` or `float()` to convert input to numbers**
* Avoids errors when comparing numeric values in `if` statements

---

## 😓 Challenges

* Remembering to convert input when needed
* Deciding when to use `int()` vs `float()`

---

## 🎯 Goals for Tomorrow

* Learn about **loops (`while` and `for`)**
* Start building **Number Guessing Game**

---

## 💬 Reflection

> Today I learned the importance of **type casting** in Python to avoid type errors.
> Excited to move on to loops and game logic tomorrow! 🚀

---

## 🧪 Try It on Replit

[![Run on Replit](https://replit.com/badge/github/pruthvi099/100DaysOfCode-Replit)](https://replit.com/@p_r_u_t_h_v_i_0_9)

---

## 🌐 Connect With Me

* 🧵 Threads: [@p\_r\_u\_t\_h\_v\_i\_0\_9](https://www.threads.com/@iampruthvi_09)
* 🧑‍💻 GitHub: [pruthvi099](https://github.com/pruthvi099)

---

> 💬 *"Consistency over perfection. Just show up and build daily."*

```


