# 🧠 100 Days of Code -- Replit Challenge

[![100DaysOfCode](https://img.shields.io/badge/-100DaysOfCode-black?style=flat-square&logo=python&logoColor=white)](https://www.100daysofcode.com/)\
[![Replit](https://img.shields.io/badge/-Replit-667881?style=flat-square&logo=replit&logoColor=white)](https://replit.com/)

------------------------------------------------------------------------

## 📅 Day 20 / 100 -- List Generator 📋

### 🚀 Challenge of the Day:

Built a **List Generator** that asks the user for a starting number,
ending number, and increment, then prints the generated sequence using a
**for loop** and Python's `range()`.

------------------------------------------------------------------------

### 💻 Code Written:

``` python
# List Generator Program

# Get user inputs
start = int(input("Start at: "))
end = int(input("End before: "))
step = int(input("Increment between values: "))

# Generate and display the sequence
for num in range(start, end, step):
    print(num)
```

------------------------------------------------------------------------

### 🎯 Example Output:

    Start at: 200
    End before: 300
    Increment between values: 20
    200
    220
    240
    260
    280

------------------------------------------------------------------------

### ✅ Win of the Day:

-   Practiced using **range()** with custom start, end, and step\
-   Learned how to handle **dynamic user inputs**\
-   Reinforced how loops work with flexible conditions

------------------------------------------------------------------------

### 🎯 Next Goal:

Enhance program to **store results in a list** and display the whole
list at once 📝

------------------------------------------------------------------------
