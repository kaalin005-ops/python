foods=[]
prices=[]
total=0

while True:
    food=input("Enter a food to buy (q to quit):")
    if food.lower()=="q":
        break
    else:
        price=float(input(f"Enter the price of a {food}:"))
        foods.append(food)
        prices.append(price)
print("_____--your card--______")
print("___--item you purchased--____")
for food in foods:
    print(foods,end=" ")

print("\n_____---total--_____")
for price in prices:
    total+=price
print(f"you total is:${total}")