menu={"pizza":3.00,
      "machos":4.50,
      "popcorn":6.0,
      "fries":2.50,
      "chips":1.00,
      "pretzel":3.50,
      "soda":3.50,
      "lemonde":4.25,}

card=[]
total=0

for key, value in menu.items():
    print(f"{key}: {value}")

print("__________________________")

while True:
    food=input("Select an item (q ro quit):").lower()
    if food=="q":
        break
    elif menu.get(food) is not None:
        card.append(food)

print(card)

for food in card:
    total=total+menu.get(food)
    print(food,end=" ")
print()
print(f"Total: {total}")