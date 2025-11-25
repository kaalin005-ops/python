def shipping_labels(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    for value in kwargs.values():
        print(value,end=" ")

shipping_labels("Dr,","spongebob","squarepants","III",
               street="123,fake st",
               city="setroit")

