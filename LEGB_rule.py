'''Python follows the LEGB rule when looking up variable names, and searches for them in this order:

Local - Inside the current function
Enclosing - Inside enclosing functions (from inner to outer)
Global - At the top level of the module
Built-in - In Python's built-in namespace'''

x="gobal"

def outer():
    x="enclosing"
    def innner():
        x="local"
        print("inner:",x)
    innner()
    print("outer:",x)
outer()

print("global",x)