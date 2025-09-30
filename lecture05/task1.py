import random

num_dice = int(input("How many dice do you want to roll? "))

total = 0


for i in range(num_dice):
    roll = random.randint(1, 6)  # roll a six-sided die
    print(f"Die {i+1}: {roll}")
    total += roll

# Print the sum of the rolls
print("Total sum:", total)