# 🎓 Grade Generator - Day 13 Challenge

# Step 1: Get user input
test_name = input("Enter the name of the test: ")
max_score = float(input("Enter the maximum score possible: "))
score_received = float(input("Enter the score you received: "))

# Step 2: Calculate percentage
percentage = (score_received / max_score) * 100
percentage = round(percentage, 2)

# Step 3: Determine letter grade
if percentage >= 90:
    grade = "A+"
    message = "🏆 Outstanding! Keep it up!"
    color = "\033[92m"  # Green
elif percentage >= 80:
    grade = "A"
    message = "🎉 Great work! You're doing amazing!"
    color = "\033[92m"
elif percentage >= 70:
    grade = "B"
    message = "👍 Good job! You can push for an A!"
    color = "\033[94m"  # Blue
elif percentage >= 60:
    grade = "C"
    message = "🙂 Not bad, but there’s room to improve!"
    color = "\033[93m"  # Yellow
elif percentage >= 50:
    grade = "D"
    message = "⚠ Keep working, you can do better!"
    color = "\033[91m"  # Red
else:
    grade = "U"
    message = "💔 Don’t give up — you can bounce back!"
    color = "\033[91m"

# Step 4: Show results
reset = "\033[0m"  # Reset text color
print(f"\n{color}📚 Test: {test_name}")
print(f"✅ Your Score: {score_received}/{max_score}")
print(f"📊 Percentage: {percentage}%")
print(f"🎯 Grade: {grade}")
print(f"{message}{reset}")

# Output Example:
# Enter the name of the test: English
# Enter the maximum score possible: 75
# Enter the score you received: 65

# 📚 Test: English       
# ✅ Your Score: 65.0/75.0
# 📊 Percentage: 86.67%
# 🎯 Grade: A
# 🎉 Great work! You're doing amazing!