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


# OUTPUT:
# Is it a leap year? (yes/no): yes
# There are 31622400 seconds in this year.


# Is it a leap year? (yes/no): no
# There are 31536000 seconds in this year.