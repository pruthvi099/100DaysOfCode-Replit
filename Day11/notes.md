# 🧠 100 Days of Code – Day 11 Notes

## 📅 Date: 2025-08-05
## 🛠️ Topic: Python – Conditional Statements (`if`, `elif`, `else`)

---

## ✅ Concepts Covered

### 🔁 Conditional Statements

| Statement | Description                              |
|-----------|------------------------------------------|
| `if`      | Executes a block if condition is `True`  |
| `elif`    | Checks next condition if previous was `False` |
| `else`    | Executes if none of the above are `True` |

---

## 🧪 Practice Code

```python
# Ask the user if it's a leap year
is_leap = input("Is it a leap year? (yes/no): ").lower()

# Seconds in a day
seconds_per_day = 24 * 60 * 60  # 86400

# Decide number of days in the year
if is_leap == "yes":
    days = 366
else:
    days = 365

# Calculate total seconds
seconds_in_year = days * seconds_per_day

# Show the result
print("There are", seconds_in_year, "seconds in this year.")
```

### 🖥️ Output Example

```
Is it a leap year? (yes/no): yes
There are 31622400 seconds in this year.
```

```
Is it a leap year? (yes/no): no
There are 31536000 seconds in this year.
```

---

## 🧠 Key Takeaways

- Use `.lower()` to make input case-insensitive
- `if` is the basic building block for decision making
- `elif` adds more options
- `else` is the fallback if no conditions match

---

## 📌 Tip

> Always validate user input when using `if` statements. This helps avoid unexpected results!

---

## 🔜 Coming Up

- `while` loops and `for` loops
- Pattern printing
- Loop-based logic and automation