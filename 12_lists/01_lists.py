marks = [54, 23, 64, 93, 32]
mixed = [43, "Hello", False, 4.2]

print(marks)
print(mixed)
# How to access the elements of a list?
# Always access the element of a list by providing index, just like strings.

# So if you write marks zero, you'll get 54 because at index zero it has 54.

print(marks[0])
print(marks[2])
# NOTE:Index of list, string and tuple starts from zero.

# Can you also do the same with mixed?
#yes! Can do that.

print(mixed[2])

# Can you do slicing in list?
#yes! Can do that.

print(marks[2:4])
print(marks[2])
print(mixed[4]) # Error Index out of bound 


