fruits=["apple","orange","banana","coconut"]
vegetables=["celery","carrots","potatoes"]
meats=["chiken","first","turkey"]

groceries=[fruits,vegetables,meats]

#print(groceries[1][2])

for collection in groceries:
    #print(collection)
    for food in collection:
        print(food,end=" ")
    print()