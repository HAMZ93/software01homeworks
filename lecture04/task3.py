numbers = []

while True:
    user_input = input("Enter a number (leave blank to stop): ")
    if user_input == "":
        break
    numbers.append(float(user_input))

if numbers:
    print("Smallest:", min(numbers))
    print("Largest:", max(numbers))
else:
    print("No numbers entered.")

