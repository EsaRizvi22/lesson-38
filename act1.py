#Store your Name, Age, Weight
#Whether you are a student or not (True for yes, False for no) in respective variables.
#What do you think is the data type of each variable? 
# Print the data type of every variable.
#  Change the datatype of Age to string and Weight to an integer.

name="Ali"
age=5
weight=20.8
isStudent=True

print("Data type of ",name," before type casting is ",type(name))
print("Data type of ",age," before type casting is ",type(age))
print("Data type of ",weight," before type casting is ",type(weight))
print("Data type of ",isStudent," before type casting is ",type(isStudent))

age=float(age)
weight=str(weight)
isStudent=str(isStudent)

print("Data type of ",age," after type casting is ",type(age))
print("Data type of ",weight," after type casting is ",type(weight))
print("Data type of ",isStudent," after type casting is ",type(isStudent))