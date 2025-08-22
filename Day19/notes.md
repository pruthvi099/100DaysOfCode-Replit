# 🧠 100 Days of Code -- Replit Challenge

[![100DaysOfCode](https://img.shields.io/badge/-100DaysOfCode-black?style=flat-square&logo=python&logoColor=white)](https://www.100daysofcode.com/)\
[![Replit](https://img.shields.io/badge/-Replit-667881?style=flat-square&logo=replit&logoColor=white)](https://replit.com/)

------------------------------------------------------------------------

## 📅 Day 19 / 100 -- Loan Calculator 💰

### 🚀 Challenge of the Day:

Created a **loan calculator** that shows how much money is owed on a\
**\$1,000 loan** with **5% APR** over **10 years**. Practiced using a\
**for loop** for compound interest calculations.

------------------------------------------------------------------------

### 💻 Code Written:

``` python
loan = 1000  # starting amount

for year in range(10):  # loop through 10 years
    loan *= 1.05  # increase by 5% each year

print(f"Total owed after 10 years: ${loan:.2f}")
```

------------------------------------------------------------------------

### 🎯 Example Output:

    Total owed after 10 years: $1628.89

------------------------------------------------------------------------

### ✅ Win of the Day:

-   Learned how to calculate **compound interest** with a loop\
-   Practiced **for loops** with concise one-line updates\
-   Improved understanding of **financial math with Python**

------------------------------------------------------------------------

### 🎯 Next Goal:

Enhance the calculator to show a **year-by-year breakdown** of the loan\
growth 📊
