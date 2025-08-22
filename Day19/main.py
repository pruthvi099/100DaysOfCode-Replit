loan = 1000  # starting amount
for year in range(10):  # 10 years
    loan *= 1.05  # increase by 5% each year

print(f"Total owed after 10 years: ${loan:.2f}")


# Output
# Total owed after 10 years: $1628.89