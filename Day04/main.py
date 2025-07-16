print("\033[96mWelcome to your adventure simulator!\033[0m")
print("\033[93mI am going to ask you a bunch of questions and then create an epic story with you as the star!\033[0m\n")

# Input
name = input("\033[1mWhat is your name? \033[0m")
enemy = input("\033[1mWhat is your worst enemy’s name? \033[0m")
superpower = input("\033[1mWhat is your superpower? \033[0m")
location = input("\033[1mWhere do you live? \033[0m")
fav_food = input("\033[1mWhat is your favorite food? \033[0m")

# Output story with inline ANSI codes
print()
print(f"Hello \033[92m{name}\033[0m! Your ability to \033[95m{superpower}\033[0m will make sure you never have to look at \033[91m{enemy}\033[0m again.")
print(f"Go eat \033[93m{fav_food}\033[0m as you walk down the streets of \033[94m{location}\033[0m and use \033[95m{superpower}\033[0m for good and not evil!")
