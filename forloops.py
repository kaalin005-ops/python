#-->Execute a block of code a fixed number of times
#-->you can iterates over a range,string,sequence etc

for x in range(1,10):
    print(x)

print("________________")

for x in range(1,10,3):
    print(x)

print("________________")

for x in reversed(range(1,11)):
    print(x)

    print("________________")

for x in range(1,21):
    if x==13:
        break
    else:
        print(x)
