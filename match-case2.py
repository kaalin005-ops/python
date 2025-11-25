def is_weekend(day):
    match day:
        case "saturday" | "sunday":
            return True
        case "Monday"|"tuesday"|"wednexday":
            return False
        case _:
            return false

print(is_weekend("Monday"))