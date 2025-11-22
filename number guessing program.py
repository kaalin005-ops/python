import random
number=random.randint(1,10)
print(number)

#rock paper,scissor

options=("rocks", "papers", "scissors")
option=random.choice(options)
print(option)

#cards

cards=["2","3","4","5","6","7","8","9","j","q","t"]

random.shuffle(cards)
print(cards)