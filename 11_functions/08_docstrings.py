def sum(a, b):
    '''This will sum two numbers'''
    c = a + b
    return c

print(sum.__doc__) # Docstring is being printed.

# It might look like a regular Python comment, but if you write it.
# right after starting the function, it's called docstring.



# Why python is designed to have docstrings? 
# Because we sometimes want to attach information to a function.


# Here is even proper way to write docstrings:
def add(a, b):
    """
    
    Returns the sum of two numbers.


    parameters:
    a(int): The first number.
    b(int): The second number.


    Returns:
    int: The sum of the two numbers.
    """

return a + b