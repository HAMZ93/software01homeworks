import math

def pizza_unit_price(diameter_cm, price_eur):
    radius_m = (diameter_cm / 2) / 100
    area_m2 = math.pi * radius_m**2
    return price_eur / area_m2

def main():
    d1 = float(input("Enter diameter of the first pizza (cm): "))
    p1 = float(input("Enter price of the first pizza (€): "))
    d2 = float(input("Enter diameter of the second pizza (cm): "))
    p2 = float(input("Enter price of the second pizza (€): "))

    unit1 = pizza_unit_price(d1, p1)
    unit2 = pizza_unit_price(d2, p2)

    print(f"First pizza: {unit1:.2f} €/m²")
    print(f"Second pizza: {unit2:.2f} €/m²")

    if unit1 < unit2:
        print("The first pizza offers better value for money.")
    elif unit2 < unit1:
        print("The second pizza offers better value for money.")
    else:
        print("Both pizzas offer the same value for money.")

if __name__ == "__main__":
    main()