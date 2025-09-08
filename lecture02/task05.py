GRAMS_PER_LOT = 13.3
LOTS_PER_POUND = 32
POUNDS_PER_TALENT = 20

print("Enter the mass in medieval units:")
talents = int(input("Talents: "))
pounds = int(input("Pounds: "))
lots = int(input("Lots: "))

total_grams = (
    talents * POUNDS_PER_TALENT * LOTS_PER_POUND * GRAMS_PER_LOT +
    pounds * LOTS_PER_POUND * GRAMS_PER_LOT +
    lots * GRAMS_PER_LOT
)

kilograms = int(total_grams // 1000)
grams = total_grams % 1000

print(f"\nMass in modern units: {kilograms} kilograms and {grams:.2f} grams")
print(f"Total grams: {total_grams:.2f} g")