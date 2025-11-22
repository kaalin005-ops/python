unit=input("Is this temperature in celsius or Fahrenheit(C/H):")
temp=float(input("Enter the temperature"))

if unit=="C":
    print(f"The temperature in fahrenheit is: {round((9*temp)/5+32, 1)}")
elif unit=="F":
    print(f"The temperature in celsius is: {round((temp-32)*5/9, 1)}")

else:
    print(f"{unit} is an invalid unit of measurement")