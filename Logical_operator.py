#logical operators=evalute mutiple conditions(or,and,not)
#or=at least one condition must be true
#and=both condition must be true
#not= inverts the condition(not False,not True)\


temp = 25
is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
elif temp >= 28 and is_raining:
    print("It is HOT outside")
    print("It is sunny")
else:
    print("nothing else")

is_logged_in = True

if not is_logged_in:
    print("Please log in to continue.")
else:
    print("Welcome back!")