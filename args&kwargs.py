#*args=allows you to pass multiple non-key arguments
#**kwargs=allows you to pass multiple keyword-arguments

#         *unpacking operator
#         position,keyword,default,Arbitary


def add(*args):
    total=0
    for arg in args:
        total+=arg
    return total

print(add(1,2,3))

def display(*args):
    for arg in args:
        print(arg,end=" ")

display("Dr","Alan","master","mind")


def print_address(**kwargs):
    for key,value in kwargs.keys():
        print(f"{key}:{value}")

print(street="123",
      city="Detroit",
      state="Mi",
      Zip="54321")