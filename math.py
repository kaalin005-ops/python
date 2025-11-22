import math
x=9.9
print(f"pi={math.pi}")
print(f"math.e={math.e}")

result=math.sqrt(x)
print(f"sqrt={round(result)}")

res=math.ceil(x)
print(f"ceil={res}")

re=math.floor(x)
print(f"floor={re}")

#write a python program to convert degrees to radian

import math

def degrees_to_radians(degrees):
    radians = degrees * (math.pi / 180)
    return radians

# Example usage
degree_input = float(input("Enter angle in degrees: "))
radian_output = degrees_to_radians(degree_input)
print(f"{degree_input} degrees is equal to {radian_output:.2f} radians")


radius=float(input('Enter the radius of a circle: '))

circumference=2*math.pi*radius

print(f"the circumference is: {round(circumference,2)}cm")

