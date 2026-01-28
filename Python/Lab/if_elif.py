#Python program to demonstrate the use of if statement by pring the grades of students from their marks

'''
# Checking user eligibility for casting vote, using if statement

age = float(input("Enter your age :"))
if age>=18:
    print("Congratulations! you can cast your vote")

print("Program ended!")

# Checking whether student is pass or fail in the exam, using if..else statement!

marks = float(input("Enter your marks : "))

if marks>=40:
    print("Congratulations! you have passed the exam.")
else:
    print("Sorry! Yor have failed in the exam")
'''
# Computing student Grades using if..elif..else statement

marks = float(input("Enter the marks :"))

if marks>=90:
    print("Excellent! you have got A+ grades")

elif marks>=80:
    print("Congratulations! you have got A grades")

elif marks>=70:
    print("Great! you have got B+ grades")

elif marks>=60:
    print("Nice you have got B grades")

elif marks>=50:
    print(" You have got C grades")

elif marks>=40:
    print("You have got D grades")

else:
    print("Sorry! you have Failed. Better luck next time!")

