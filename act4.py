#First of all, take two numbers from the user, 
# store them in variables x and y, respectively.
#  Write a Python program to swap the values present inside x and y and display the results.

num1=int(input("Enter first name"))
num2=int(input("Enter second name"))

print("Before swapping first number is ",num1)
print("Before swapping second number is ",num2)
temp=num1
num1=num2
num2=temp

print("After Swapping first number is ",num1)
print("After swapping second number is ",num2)