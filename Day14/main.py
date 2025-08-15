from getpass import getpass as input

print("🎮 Rock, Paper, Scissors – 2 Player Edition 🪨📄✂️\n")
print("Instructions: Type R for Rock, P for Paper, or S for Scissors.")

# Function to validate and standardize input
def get_choice(player):
    while True:
        choice = input(f"{player}, enter your choice (R/P/S): ").strip().lower()
        if choice in ['r', 'rock']:
            return 'r'
        elif choice in ['p', 'paper']:
            return 'p'
        elif choice in ['s', 'scissors', 'scissor']:
            return 's'
        else:
            print("⚠ Invalid choice! Please enter R, P, or S.")

# Get both players' choices
player1 = get_choice("Player 1")
player2 = get_choice("Player 2")

# Decide the winner
if player1 == player2:
    result = "🤝 It's a tie!"
elif (player1 == 'r' and player2 == 's') or \
     (player1 == 'p' and player2 == 'r') or \
     (player1 == 's' and player2 == 'p'):
    result = "🎉 Player 1 wins! 🏆"
else:
    result = "🎉 Player 2 wins! 🏆"

# Show results
choices_map = {'r': '🪨 Rock', 'p': '📄 Paper', 's': '✂️ Scissors'}
print("\n--- Game Results ---")
print(f"Player 1 chose: {choices_map[player1]}")
print(f"Player 2 chose: {choices_map[player2]}")
print(result)

# Output

# 🎮 Rock, Paper, Scissors – 2 Player Edition 🪨📄✂️

# Instructions: Type R for Rock, P for Paper, or S for Scissors.
# Player 1, enter your choice (R/P/S):
# Player 2, enter your choice (R/P/S):

# --- Game Results ---
# Player 1 chose: 🪨 Rock
# Player 2 chose: ✂️ Scissors
# 🎉 Player 1 wins! 🏆