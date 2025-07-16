
# Day 6 – 100DaysOfCode

📅 Date: 2025-07-10  
🛠️ Project/Topic: Python `if-elif-else` – Secure Login System

---

## ✅ What I Did Today

- Built a **Secure Login Program** in Python  
- Practiced using **`elif` statements** to handle **multiple conditions**

---

## 💡 What I Learned

- How to use `if`, `elif`, and `else` together  
- Checking **multiple conditions** with `and` operators  
- Giving **different responses** based on username/password combinations

---

## 🔧 Code Example

```python
print("SECURE LOGIN")
username = input("Username > ")
password = input("Password> ")

if username == "pruthvi" and password == "password":
    print("Welcome Pruthvi!")
elif username == "pruthvi" and password == "1234":
    print("Hey there Pruthvi!")
else:
    print("Go away!")
```

---

## 🖥️ Output

### Case 1: Correct username and password

```
SECURE LOGIN
Username > pruthvi
Password> password
Welcome Pruthvi!
```

### Case 2: Same username, different password

```
SECURE LOGIN
Username > pruthvi
Password> 1234
Hey there Pruthvi!
```

### Case 3: Wrong input

```
SECURE LOGIN
Username > someoneelse
Password> anything
Go away!
```

---

## 😓 Challenges

- Remembering how `and` works in conditionals  
- Keeping **indentation clean** and consistent  

---

## 🎯 Goals for Tomorrow

- Use **`while` loops** to build a **Number Guessing Game**  
- Practice **looping with conditions** and `break` statements  

---

## 💬 Reflection

> Today I learned about **elif** and how it makes code cleaner and more scalable.  
Excited to move into **loops and game logic** tomorrow! 🚀  
#Python #100DaysOfCode #Replit #CodingJourney #DevDiaries
