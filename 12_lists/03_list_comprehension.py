# Create a list containing the table of five.

a = 5
table = []
for i in range(1, 11): # Goes from 1 to 10
    table.append(5*i)

print(table)
# This mathod is very long...there is a shortcut known as list comprehensive through which we can
#write this five lines of code in a single line.

table = [5*i for i in range(1,11)]
print(table)











