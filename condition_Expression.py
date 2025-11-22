#condition expression=A one-line shortcut for the if-else statement(ternery operator)
#                     print or assign one of two values based on a condition
#                     x if condition else y


num=5
print("positive" if num>0 else "negative")

print(f"{"Even" if num%2==0 else "ODD"}")

a=6
b=7
max_num= a if a>b else b
min_num=a if a<b else b
print(min_num)
