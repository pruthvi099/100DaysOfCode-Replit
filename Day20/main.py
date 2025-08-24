# List Generator Program

# Get user inputs
start = int(input("Start at: "))
end = int(input("End before: "))
step = int(input("Increment between values: "))

# Generate the sequence using range()
for num in range(start, end, step):
    print(num)



# OUTPUT :
# Start at: 200
# End before: 300
# Increment between values: 20
# 200
# 220
# 240
# 260
# 280
