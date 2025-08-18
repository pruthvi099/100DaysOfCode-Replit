while True:
    answer = input("Do you want to continue? (y/n): ").strip().lower()
    if answer == "n":
        print("👋 Goodbye!")
        break  # exits the loop
    else:
        print("🚀 Let's keep going!")


# OUTPUT:
# Do you want to continue? (y/n): y
# 🚀 Let's keep going!
# Do you want to continue? (y/n): y
# 🚀 Let's keep going!
# Do you want to continue? (y/n): n
# 👋 Goodbye!