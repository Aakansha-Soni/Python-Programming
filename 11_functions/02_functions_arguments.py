def add(a, b): # Positional argument
    return a + b

c = add(3, 5)
print(c)

def add(a, b, plus=0): # Default argument 
    x = a + b + plus
    return x

c = add(3, 5, 2)
print(c)


c = add(3, 5, 2) #Keyword argument
print(c)

c1 = add(b=5, a=3)








