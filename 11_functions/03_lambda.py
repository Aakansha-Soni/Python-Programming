square = lambda x: x * x # Lambda functions are anonymous, inline functions.
print(square(4)) # Output: 16

numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)

square = lambda x: x * x
'''
As good as writing
def square(x):
    return x*x
'''
sum = lambda x, y: x+y
'''
As good as writing
def sum(x, y):
    return x + y
'''
print(square(3))
print(sum(3, 62))

# What are lambda functions exactly used for?
#--> Sometimes we want to create a one liner function, or we want to pass a function to a function.
