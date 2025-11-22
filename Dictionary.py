#A collection of{key:value} pairs orderes and changeable.no duplicates

capitals={"usa":"washindton",
          "India":"new delhi","china":"beijing","russia":"moscow"}

#print(dir(capitals))
#print(help(capitals))

print(capitals.get("India"))

if capitals.get("japan"):
    print("that capital exsists")
else:
    print("that capital doesn't exist")

capitals.update({"germany":"berlin"})
print(capitals)

capitals.pop("china")
print(capitals)

capitals.popitem()
print(capitals)

#capitals.clear()
keys=capitals.keys()


for key in keys:
    print(key)


values=capitals.values()
for values in capitals.values():
    print(values)


items=capitals.items()
for key, value in capitals.items():
    print(f"{key},{value}")