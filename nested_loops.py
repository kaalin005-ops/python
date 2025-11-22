#A loop within another loop(outer,inner)
#x=5
#y=5
#while x>0:
    #while y>0:
        #print("do something") infinite loop


for x in range(3):
    for y in range(2):
        print("do something")

x = 1  # or any positive value
if x > 0:
    for y in range(9):
        print("do something")

x = 5
count = 1  # initialize counter

while x > 0:
    for y in range(9):
        print(f"{count} do")
        count += 1
    x=x-1