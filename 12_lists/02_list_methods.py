marks = [5, 2, 21, 5, 7]
extra_marks = [53, 23, 32]

print(marks)
# marks.append(63) # This will change the original list
# marks.pop() # Remove the last element from the list.
marks.extend(extra_marks) # By extend, i can pass a list, another list which'll basically be appended at the end of the list.
print(marks)