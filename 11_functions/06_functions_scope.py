def sum(a, b):
    # a and b are local variable(means u can only access these variables inside a function.)
    c =  a + b
    z = 1 # It creates a local variable called z which is destroyed after this function returns
    return c

def greet():
    z = 32 # Local variable

z = 8 # Z is a global variable
print(sum(4, 6))
print(z)
# Functions only keeps variables until it returns.