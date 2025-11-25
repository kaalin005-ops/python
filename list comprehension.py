#list comrehension= A concise wayb to creatte list in python
                  # combat and easier to read than traditional loops
                  #[expression for value in iterable if condition]
doubles=[]
for x in range(1,11):
    doubles.append(x*2)
print(doubles)

'''expression for value in iterable if condition'''
double=[x*2 for x in range(1,11)]
triples=[y*3 for y in range(1,11)]
squares=[z*z for z in range(1,11)]

print(double)
print(triples)
print(squares)
#fruits.upper()
fruits=[fruits[0] for fruits in["apple","orange","banana","coconut"]]
print(fruits)



numbers=[-1,2,3,4,5,6,7]
positive=[num for num in numbers if num>=0]
negative=[num for num in numbers if num < 0]
print(negative)
print(positive)
even=[num for num in numbers if num % 2 == 0]
print(even)
odd=[num for num in numbers if num % 2 == 1]
print(odd)