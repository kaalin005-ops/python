weight=float(input("Enter your weight:"))
unit=input("kilograms or pounds?(k or L):")

if unit=="k":
    weight=weight*2.205
    unit="Lbs."
elif unit=="L":
    weight=weight/2.205
    unit="Kgs."
else:
    print(f"{unit} was not valid")

print(f"your weight is:{weight} {unit}")