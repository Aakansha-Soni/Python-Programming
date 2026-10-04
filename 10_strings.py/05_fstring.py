# String formatting

# template = "Dear Aakansha, You are awesome. Take this 10000$ bag"

template = "Dear {}, You are awesome. Take this {}$ bag"

#Generate different types of strings for different people and different amount. 
a = "John"
a1 = 10000
b = "Jack"
b1 = 1000
c = "Marie"
c2 = 300

s1 = template.format(a, a1)
print(s1)

#While this method is good and it was used before Python 3.6, creators of Python realized that there can be
# a better way to do this, and one of the best ways to do this is f string. 

print(f"{a} you are awesome and take this {a1}$ bag")
# Note: f string is a simple way to put variables inside a string.