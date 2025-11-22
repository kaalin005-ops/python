#Accessing elements of a sequence using[] (indexing operator)
#[start:end:step]

credit="1234-4567-8910"
print(credit[0])#first numbeer
print(credit[:4])#first 4
print(credit[5:])#5th index to 9 th index
print(credit[-1])#reverse index
print(credit[::2])#print 2 index of mutiple

last_digit=credit[-4:]#only 4 digit from last
print(last_digit)

print(f"****-****-{credit}")

credit=credit[::-1]
print(credit)


