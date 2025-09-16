LEGAL_SIZE = 42
length = int(input("Length of zander (cm): "))

if length < LEGAL_SIZE:
    print(f"Release the fish. It is {LEGAL_SIZE - length} cm below the limit.")
else:
    print("You may keep the fish.")