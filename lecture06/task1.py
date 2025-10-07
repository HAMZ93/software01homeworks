month = int(input("Enter the month number (1-12): "))

if month in (12, 1, 2):
    print("Winter")
elif month in range(3, 6):
    print("Spring")
elif month in range(6, 9):
    print("Summer")
elif month in range(9, 12):
    print("Autumn")
else:
    print("Invalid month number")