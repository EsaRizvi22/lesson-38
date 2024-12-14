#Store the values of your first name and last name in respective variables.
#  Now add these two strings and store them in the variable full name. 
# Create another variable with the first name multiplied by any number of your choice as its value. 
# Print all the four variables Now add another variable to your program with any string of your choice. 
# Find its length,
#  print its first and last character, 
# and print a sub-string of this original string as well.

firstname="Esa"
lastname="Rizvi"
fullname=firstname+lastname

print("Full name is ",fullname)

print("firstname multiplied by 3 is ",firstname)

word="Hello World"
print("Length of ",word," is ",len(word))
print("First letter of ",word," is ",word[0])
print("Last letter of ",word," is ",word[10])
print("Sliced word is ",word[1:7])