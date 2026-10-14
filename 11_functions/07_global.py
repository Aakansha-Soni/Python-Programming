def sum(a, b):
    print("Hey I am summing ")
    c = a + b
    #  z = 0 # will it change? No it will not, declaring another z = 0 inside another function is not going to change it.
    global z # Global keyword is simply used to modify global variables.
    # Please modify global z
    z = 0 # Now it will refer to the global variable z and not create a local variable.
   
    return c

z = 3 # Global variable
print(sum(3, 12))
print(z)

# Interview Question: Can you modify a global variable inside a function?
# Yes! We can.But we've to use global.