'''name = "Harry" # Strings are immutable

# name[0] = "R" # You cannot do this

a = len(name) # 5 characters in name spelling
print(a)'''

'''s = "hello world" 
a = len(s)
print(a) #space will also count as it is known as blank character
#Blank character is also counted as a character.

print(s.upper())
print(s.upper(), s) #The original string remain intact.While the upperreturns the new string.
print(s.lower()) # Convert the string to lower case.
print(s.capitalize())'''

#Removing Whitespace
text = "  hello world  "
print(text.strip()) # Output: "hello world"
print(text.lstrip()) # Output: "hello world "
print(text.rstrip()) # Output: " hello world"

#Finding and Replacing
text = "Python is fun" 
print(text.find("is"))  # Output: 7 (i is in 7th index)
print(text.replace("fun","awesome")) #Output: "Python is awesome"

# Splitting and Joining
text= "aaple,banana,orange"
fruits = text.split(",")
print(fruits)  # Output: ['apple', 'banana', 'orange']
print(",".join(['Apple', 'Bananas', 'Pineapples']))

#Checking String properties
text = "python123"
print(text.isalpha()) # Output: False
print(text.isdigit()) # Output: False
print(text.isalnum()) # Output: True [alphanumeric: A String contains only alphabets, and numericals which is numbers.]
print(text.isspace()) # Output: False




