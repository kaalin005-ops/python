'''match-case statement(switch): A alternative to using many 'elif' statements
execute some code if a value matches a 'case'
benefits:cleaner and syntax is more readable

'''

def day_of(day):
    if day==1:
        return "it is sunday"
    elif day==2:
        return "it is monday"
    elif day==3:
        return "it is tuesday"
    elif day==4:
        return "it is wednesday"
    elif day==5:
        return "it is thursday"
    elif day==6:
        return "it is friday"
    elif day==7:
        return "it is saturaday"
    else:
        return "Not a valid day"

print(day_of(1))

'''               👇👇 '''

def day_of_week(day):
    match day:
        case 1:
            return "it is sunday"
        case 2:
            return "it is monday"
        case 3:
            return "it is tuesday"
        case 4:
            return "it is wednesday"
        case 5:
            return "it is thrusday"
        case 6:
            return "it is friday"
        case 7:
            return "it is saturday"
        case _:
            return "Not a valid day"

print(day_of_week(5))