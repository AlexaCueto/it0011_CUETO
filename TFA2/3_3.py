#3_3
#CUETO, ALEXA JOYCE G.
#TW23

lName = input("Enter last name: ")
fName = input("Enter first name: ")
age = int(input("Enter age: "))
contactNo = input("Enter contact number: ")
course = input("Enter course: ")

infoString = f"Full Name: {fName} {lName}\nAge: {age}\nContact Number: {contactNo}\nCourse: {course}"

file1 = open("students.txt", "w")
W = (infoString)
file1.writelines(W)
file1.close()

print("Your student information has been saved to 'students.txt'")


