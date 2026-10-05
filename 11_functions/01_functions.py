a = 4
b = 2
c = 1

average = (a + b + c)/3
print(average)
a1 = 6
b1 = 7
c1 = 12

average1 = (a1 + b1 + c1)/3
print(average1)

def average(a, b, c): # In order to create a function in Python, we use def keyword.
# NOTE: Any function in python start with def keyword.
    d = (a + b + c)/3.0
    print(d) # In output nothing happens, because we've just defined the function, but we did not call this function.

average(3, 5, 1)

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))








