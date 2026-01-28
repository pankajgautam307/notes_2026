 
def greatest(a, b): 
    if a > b:
        return a    
    else:
        return b
 
num1 = float(input("Enter first number: ")) 
num2 = float(input("Enter second number: ")) 
print(f"The greatest number is: {greatest(num1, num2)}")