#variable scope=where a variable is visible and accessible
#scope resolution=(LeGB) Local->Enclosed->global-> built-in

x = "global"


def outer():
    x = "enclosed"

    def inner():
        x = "local"
        print("Inner:", x)  # Local scope

    inner()
    print("Outer:", x)  # Enclosing scope


outer()
print("Global:", x)  # Global scope