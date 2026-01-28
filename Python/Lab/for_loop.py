# Python Program to navigate through the elements of a list using a for statement.
list1 = [1,2,3,4,5,6,7,8,9,10]
print("List1  : ",list1)

squares = []
for a in list1:
    square = a ** 2
    squares.append(square)

print("Squares: ",squares)