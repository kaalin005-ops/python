#default arguments=A default value for certain parameters

#                  default is used when that arguments is omitted

#                  make your functions more flexible,reduces # of arguments

#

def net_price(list,discount=0,tax=0.5):
    return list*(1-discount)*(1+tax)

print(net_price(500))

import time
def count(end,start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("Done!")

count(10)