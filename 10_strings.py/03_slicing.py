'''name = "Harry"

# Positive Index slicing
print(name[0:2]) # Goes from 0 to 2-1,i.e., [0 - 1].

#cNegative Index slicing
print(name[2:-1]) # Same as name[2:4] because here we add length of a string to the number.'''

# Slicing with steps
name = "Harry0123456789"

# print(name[0:10:n]) #Skip n - 1 characters
print(name[0:10:1]) # skip 0 characters , in skip 0  nothing will happen.The same string will return to the program.
print(name[0:10:2]) # skip 1 character
print(name[0:10:3]) # skip 3-1 ie 2 character

print(name[:4]) # Replace the first empty number with 0 # name[0:4]
print(name[1:]) # Replace the second empty number with length # name[1:15]

print(name[3:])
print(name[:3])