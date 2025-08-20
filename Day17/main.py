while True:
    print("You are in a corridor, do you go left or right?")
    direction = input("> ").lower()

    if direction == "left":
        print("You have fallen to your death 💀")
        break
    elif direction == "right":
        print("You move forward into the darkness... 🌌")
        continue
    else:
        print("That's not a valid choice, try again!")

# OUTPUT:
# You are in a corridor, do you go left or right?
# > right
# You move forward into the darkness... 🌌
# You are in a corridor, do you go left or right?
# > right
# You move forward into the darkness... 🌌
# You are in a corridor, do you go left or right?
# > left
# You have fallen to your death 💀