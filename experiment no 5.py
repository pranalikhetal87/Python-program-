#Experient no.5
#questionno 1
# c  = input("Enter a string: ")

# Calculate length
length = len("nagesh")
print("Length of the string is:", length)
 
 #question 2
 # Take string input from user
string = input("Enter a string: ")

# Check length condition
if len(string) < 2:
    print("Empty string")
else:
    result = string[:2] + string[-2:]
    print("New string is:", result)
    
 #question 3 
 # Take two strings as input
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Concatenate strings
result = str1 + str2
print("Concatenated string is:", result)