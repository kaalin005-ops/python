price1=3.14159
price2=-987.65
price3=12.34


print(f"price 1 is ${price1:10}")
print(f"price 2 is ${price2:10}")#allocate that many spaces
print(f"price 3 is ${price3:10}")

print(f"price 1 is ${price1:3f}")
print(f"price 2 is ${price2:3f}")#3 round to that may decimal places(fixes points)
print(f"price 3 is ${price3:3f}")

print(f"price 1 is ${price1:010}")
print(f"price 2 is ${price2:010}")#allocate and zero pad that many spaces
print(f"price 3 is ${price3:010}")

print(f"price 1 is ${price1:<}")#left justify
print(f"price 2 is ${price2:<}")#right justify
print(f"price 3 is ${price3:^}")#center align

print(f"price 1 is ${price1:+}")
print(f"price 2 is ${price2:+}")#was a plus sign to indiactes positive
print(f"price 3 is ${price3:+}")

print(f"price 1 is ${price1:=}")
print(f"price 2 is ${price2:=}")#places sign to value leftmost position
print(f"price 3 is ${price3:=}")

print(f"price 1 is ${price1:}")
print(f"price 2 is ${price2:}")#insert a space before positive
print(f"price 3 is ${price3:}")

print(f"price 1 is ${price1:,}")
print(f"price 2 is ${price2:,}")#comma separate
print(f"price 3 is ${price3:,}")