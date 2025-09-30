
numbers = []

while True:
    user_input = input("Enter a number (empty to quit): ")
    if user_input == "":   # empty string -> stop
        break
    numbers.append(int(user_input))


numbers.sort(reverse=True)

print("The five greatest numbers:", numbers[:5])