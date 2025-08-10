print("100 Days of Code QUIZ")
print()
print("How many can you answer correctly?")

# Fix 1: Use input() instead of just assigning a string
ans1 = input("What language are we writing in? ").lower()
if ans1 == "python":
    print("Correct")
else:
    print("Nope🙈")

# Fix 2: Convert ans2 to int
ans2 = int(input("Which lesson number is this? "))

# Fix 3: Correct order of if-elif-else
if ans2 > 12:
    print("We're not quite that far yet")
elif ans2 == 12:
    print("That's right!")
else:
    print("We've gone well past that!")


# OUTPUT:
# 100 Days of Code QUIZ

# How many can you answer correctly?
# What language are we writing in? Python
# Correct
# Which lesson number is this? 12
# That's right!
