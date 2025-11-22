operator=input("Enter an operator(+,-,*,/): ")
num1=float(input("Enter the 1st number:"))
num2=float(input("enter the 2nd number: "))

if operator=='+':
    print(f"ADDED:{num1+num2}")
elif operator=='-':
    print(f"ADDED:{num1 - num2}")
elif operator=='*':
    print(f"ADDED:{num1 * num2}")
elif operator=='/':
    print(f"ADDED:{num1 / num2}")
else:
    print(f"in valid operator")
