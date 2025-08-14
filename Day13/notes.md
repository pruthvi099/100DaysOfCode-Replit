# 🧠 100 Days of Code – Replit Challenge

[![100DaysOfCode](https://img.shields.io/badge/-100DaysOfCode-black?style=flat-square&logo=python&logoColor=white)](https://www.100daysofcode.com/)  
[![Replit](https://img.shields.io/badge/-Replit-667881?style=flat-square&logo=replit&logoColor=white)](https://replit.com/@p_r_u_t_h_v_i_0_9)  
[![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/pruthvi099)  

---

# 🗓️ Day 13 / 100 – 100 Days of Code

## 📅 Date: 2025-08-07  
## 🛠️ Project/Topic: Python – Grade Generator

---

## ✅ What I Did Today

- Created a **Grade Generator** program  
- Took **test name**, **max score**, and **score received** as inputs  
- Calculated **percentage** and **assigned letter grades** using `if/elif`  
- Added **emojis and messages** to make results fun and engaging  

---

## 💡 What I Learned

### 📊 Conditional Logic in Action  
| Concept | Example | Why it Matters |
|---------|---------|----------------|
| Percentage calculation | `(score / max) * 100` | Basis for grading |
| Rounding | `round(percentage, 2)` | Cleaner display |
| If/elif ladder | Checking percentage ranges | Assigns correct grade |
| User input | `input()` and `float()` | Works with numbers and text |
| Feedback UX | Emojis, custom messages | Makes it fun for users |

---

## 🔧 Final Code

```python
print("🎓 Grade Generator\n")

test_name = input("Enter the name of the test: ")
max_score = float(input("Enter the maximum score possible: "))
score_received = float(input("Enter the score you received: "))

percentage = round((score_received / max_score) * 100, 2)

if percentage >= 90:
    grade = "A+"
    message = "🏆 Outstanding! Keep it up!"
elif percentage >= 80:
    grade = "A"
    message = "🎉 Great work! You're doing amazing!"
elif percentage >= 70:
    grade = "B"
    message = "👍 Good job! You can push for an A!"
elif percentage >= 60:
    grade = "C"
    message = "🙂 Not bad, but there’s room to improve!"
elif percentage >= 50:
    grade = "D"
    message = "⚠ Keep working, you can do better!"
else:
    grade = "U"
    message = "💔 Don’t give up — you can bounce back!"

print(f"\n📚 Test: {test_name}")
print(f"✅ Your Score: {score_received}/{max_score}")
print(f"📊 Percentage: {percentage}%")
print(f"🎯 Grade: {grade}")
print(message)
```

---

## 🤔 Why It Matters

- Teaches **conditional branching** in Python  
- Shows how **user input** can drive program flow  
- Adds **personalized feedback** for better UX  

---

## 😓 Challenges

- Deciding **grade boundaries**  
- Formatting output so it’s **clear and friendly**  
- Remembering to **convert input to numbers** before calculations  

---

## 🎯 Goals for Tomorrow

- Add **color-coded terminal output** for grades  
- Try **loops** so user can calculate multiple grades without restarting the program  

---

## 💬 Reflection

> Creating this felt like building a mini school report card generator.  
> Loved adding emojis — they make even a “D” a little less sad 😅.  

---

## 🧪 Try It on Replit

[![Run on Replit](https://replit.com/badge/github/pruthvi099/100DaysOfCode-Replit)](https://replit.com/@p_r_u_t_h_v_i_0_9)
