# Python Program to calculate factorial of a given number using while loop

num = int(input("Enter an positive integer : "))

if num<0:
    print("Kindly try again with a positive interger value")
    
elif num==0:
    print("The factorial of 0 is : 1")

else:
    factorial = 1
    i=1
    while i <= num:
        factorial = factorial * i
        i = i+1  
    print(f"The factorial of {num} is : {factorial}")

