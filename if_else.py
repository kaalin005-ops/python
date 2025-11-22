#if=Do some code only if some condition is true
#   else do something else

age=int(input("Enter your age: "))

if age>=18:
    print("you are now signed up!")
elif age<0:
    print("you haven't been born yet!")
elif age>=100:
    print("you are too old to sign up")
else:
    print("you must be 18+ to sign up")