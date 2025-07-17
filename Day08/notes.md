# Day 8 – 100DaysOfCode

🗕️ **Date:** 2025-07-16
🛠️ **Project/Topic:** Python – Custom Daily Affirmation Generator

---

## ✅ What I Did Today

* Built a **Daily Affirmations Program** using Python
* Practiced **nested if statements** and **string concatenation**
* Learned to handle **case-insensitive user input**

---

## 💡 What I Learned

* How to take **multiple user inputs** and use them in decisions
* Used **nested if statements** to customize messages further
* Created a program that responds differently based on **day of the week**
* Used **`.lower()`** and **`.capitalize()`** to handle text formatting and user-friendly output

---

## 🔧 Code Example

```python
print("\033[96mWelcome to the Daily Affirmation Generator!\033[0m\n")

# Input
name = input("What is your name? ").strip().lower()
fav_thing = input("What's something you love? ").strip()
fav_color = input("What's your favorite color? ").strip()
day = input("What day of the week is it today? ").strip().lower()

# Capitalize name for output
name_output = name.capitalize()

# Affirmations
print("\n\033[92mHere’s your affirmation, " + name_output + ":\033[0m\n")

if day == "monday":
    print("Remember, " + name_output + ", even Mondays can be great with a little " + fav_color + " magic and " + fav_thing + " by your side!")

elif day == "tuesday":
    print("Hey " + name_output + ", keep going! Tuesday is just another step closer to enjoying more " + fav_thing + ".")

elif day == "wednesday":
    if fav_color.lower() == "blue":
        print("Happy Wednesday, " + name_output + "! Like the sky, stay calm and keep " + fav_thing + " close to your heart.")
    else:
        print("Midweek vibes, " + name_output + "! Let your " + fav_color + " energy guide you through the day.")

elif day == "thursday":
    print("Hey " + name_output + ", Thursdays are for gratitude. Be thankful for " + fav_thing + " and all things " + fav_color + "!")

elif day == "friday":
    if fav_thing.lower() == "coffee":
        print("It's Friday, " + name_output + "! Go get that " + fav_thing + " and paint the town " + fav_color + "!")
    else:
        print("Friday feels, " + name_output + "! Enjoy your " + fav_thing + " and get ready for the weekend.")

elif day == "saturday":
    print("Happy Saturday, " + name_output + "! Time to relax, recharge, and surround yourself with " + fav_thing + ".")

elif day == "sunday":
    print("Hey " + name_output + ", Sundays are for peace. Think about " + fav_thing + " and let " + fav_color + " calm you.")

else:
    print("Hmm, I don't recognize that day. But no worries, " + name_output + ", you're still awesome!")
```

---

## 🔠️ Output Example

```
What is your name? pruthvi
What's something you love? python
What's your favorite color? blue
What day of the week is it today? wednesday

Here’s your affirmation, Pruthvi:

Happy Wednesday, Pruthvi! Like the sky, stay calm and keep python close to your heart.
```

---

## 😓 Challenges

* Handling **case insensitivity** correctly with `.lower()` and `.capitalize()`
* Making the output feel **friendly and personalized**

---

## 🌟 Goals for Tomorrow

* Learn **`while` loops** and build a **number guessing game**
* Explore **random numbers** in Python

---

## 💬 Reflection

> Today was fun! Nested `if` statements helped me build something interactive and personalized.
> Looking forward to creating games with loops next! 🎮
> \#Python #100DaysOfCode #Replit #CodingJourney #DevDiaries
