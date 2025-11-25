#keywords arguments=an arguments by an identifier
#                   helps with readability
#    order of arguments doesn't matter

#        positing,default,keyword,arditary

def hello(greeting,title,first,last):
    print(f"{greeting} {title}{first} {last}")


hello("hello",title="mr.",last="john",first="james")

print("1","2","3",sep="-")

def get_phone(country,area,first,last):
    return f"{country}-{area}-{first}-{last}"

phone_num=get_phone(country=1,area=123,first=456,last=7890)
print(phone_num)