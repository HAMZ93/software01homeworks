airports = {}

while True:
    choice = input()

    if choice == "1":
        icao = input()
        name = input()
        airports[icao] = name
        print("Airport saved!")
    elif choice == "2":
        icao = input()
        if icao in airports:
            print(airports[icao])
        else:
            print("Airport not found")
    elif choice == "3":
        break