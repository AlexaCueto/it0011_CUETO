#3.1 
#CUETO, ALEXA JOYCE G.
#TW23

fName = input("Enter your first name: ")
lName = input("Enter your last name: ")
age = int(input("Enter your age: "))

slicedFName = fName[:3]
formattedString = f"Hello, {slicedFName}! Welcome. You are {age} years old. "

print("Full Name: ", fName + " " + lName)
print("Sliced Name: ", slicedFName)
print(formattedString)