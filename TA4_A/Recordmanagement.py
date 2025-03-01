#CUETO, ALEXA JOYCE G
#TW23
#LIST AND TUPLES

students = []  #Stores student records as list
filename = "StudentsRecords"  #Default file for saving and loading records

def openFile():
    global students
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
        students = []
        for line in lines:
            studentID, firstName, lastName, classStanding, majorExam = line.strip().split("|")
            students.append((studentID, (firstName, lastName), float(classStanding), float(majorExam)))
        print(f"\t\tFile '{filename}' loaded successfully.")
    except FileNotFoundError:
        print(f"\t\tFile '{filename}' not found. No records loaded.")

def saveFile():
    with open(filename, "w") as file:
        for student in students:
            file.write(f"{student[0]}|{student[1][0]}|{student[1][1]}|{student[2]}|{student[3]}\n")
    print(f"\t\tRecords saved successfully to '{filename}'.")

def saveAsFile():
    new_filename = input("\t\tEnter new filename (with .txt extension): ")
    with open(new_filename, "w") as file:
        for student in students:
            file.write(f"{student[0]}|{student[1][0]}|{student[1][1]}|{student[2]}|{student[3]}\n")
    print(f"\t\tRecords saved successfully as '{new_filename}'.")

def showAllRecords():
    while True:
        print("\n\t\t--SHOW RECORD--")
        print("\t\t1. Order by Last Name")
        print("\t\t2. Order by Grade")
        print("\t\t3. Back to Main Menu")
        
        subChoice = input("\t\tEnter your choice (number): ")

        if subChoice == "1":
            orderLastName()
        elif subChoice == "2":
            orderGrade()
        elif subChoice == "3":
            return  
        else:
            print("\t\tInvalid choice. Please try again.")

def menu():
    while True:
        print("\n\t\t--MENU--")
        print("\t\t1. Open File")
        print("\t\t2. Save File")
        print("\t\t3. Save As File")
        print("\t\t4. Show All Students Records")
        print("\t\t5. Show Student Record")
        print("\t\t6. Add Record")
        print("\t\t7. Edit Record")
        print("\t\t8. Delete Record")
        print("\t\t9. Exit")
        
        choice = input("\t\tEnter your choice (number): ")

        if choice == "1":
            openFile()
        elif choice == "2":
            saveFile()
        elif choice == "3":
            saveAsFile()
        elif choice == "4":
            showAllRecords()
        elif choice == "5":
            showRecord()
        elif choice == "6":
            addRecord()
        elif choice == "7":
            editRecord()
        elif choice == "8":
            deleteRecord()
        elif choice == "9":
            print("\t\tExiting program...")
            break
        else:
            print("\t\tInvalid choice. Please try again.")
            
def addRecord():
    print("\n\t\t--ADD RECORD--")
    studentID = input("\t\tEnter Student ID (6 digits): ")
    if len(studentID) != 6 or not studentID.isdigit():
        print("\t\tInvalid ID. Must be 6 digits.")
        return
    
    firstName = input("\t\tEnter First Name: ")
    lastName = input("\t\tEnter Last Name: ")
    classStanding = float(input("\t\tEnter Class Standing Grade: "))
    majorExam = float(input("\t\tEnter Major Exam Grade: "))

    students.append((studentID, (firstName, lastName), classStanding, majorExam))
    print("\t\tStudent record added successfully.")

#Function to get the last name of a student
def getLastName(student):
    return student[1][1]  #Extract last name

def orderLastName():
    sortedStudents = sorted(students, key=getLastName)  
    print("\n\t\t--STUDENT RECORDS (Ordered by Last Name)--")
    print("\t\tID\t\tName\t\t\tClass Standing\t\tExam")
    print("-" * 90)
    for student in sortedStudents:
        print(f"\t\t{student[0]}\t\t{student[1][0]} {student[1][1]}\t\t{student[2]}\t\t\t{student[3]}")


def computeGrade(student):
    return 0.6 * student[2] + 0.4 * student[3]  #Compute final grade

def orderGrade():
    sortedStudents = sorted(students, key=computeGrade, reverse=True) 
    print("\n\t\t--STUDENT RECORDS (Ordered by Grade)--")
    print("\t\tID\t\tName\t\t\tClass Standing\t\tExam")
    print("-" * 90)
    for student in sortedStudents:
         print(f"\t\t{student[0]}\t\t{student[1][0]} {student[1][1]}\t\t{student[2]}\t\t\t{student[3]}")
         
def showRecord():
    studentID = input("\t\tEnter Student ID: ")
    for student in students:
        if student[0] == studentID:
            print("\n\t\t--STUDENT RECORD--")
            print("\t\tID\t\tName\t\t\tClass Standing\t\tExam")
            print("-" * 90)
            print(f"\t\t{student[0]}\t\t{student[1][0]} {student[1][1]}\t\t{student[2]}\t\t\t{student[3]}")
            return
    print("\t\tStudent not found.")

def editRecord():
    studentID = input("\t\tEnter Student ID to Edit: ")
    for i, student in enumerate(students):
        if student[0] == studentID:
            firstName, lastName = student[1]
            classStanding = student[2]
            majorExam = student[3]
            
            print("\t\tEdit Menu:")
            print("\t\t1. Edit First Name")
            print("\t\t2. Edit Last Name")
            print("\t\t3. Edit Class Standing Grade")
            print("\t\t4. Edit Major Exam Grade")

            editChoice = input("\t\tEnter your choice: ")

            if editChoice == "1":
                firstName = input("\t\tEnter New First Name: ")
            elif editChoice == "2":
                lastName = input("\t\tEnter New Last Name: ")
            elif editChoice == "3":
                classStanding = float(input("\t\tEnter New Class Standing Grade: "))
            elif editChoice == "4":
                majorExam = float(input("\t\tEnter New Major Exam Grade: "))
            else:
                print("\t\tInvalid choice. Please try again.")
                return
            
            students[i] = (studentID, (firstName, lastName), classStanding, majorExam)
            print("\t\tStudent record updated successfully.")
            return
        
    print("\t\tStudent not found.")

def deleteRecord():
    studentID = input("\t\tEnter Student ID to Delete: ")
    for i, student in enumerate(students):
        if student[0] == studentID:
            del students[i]
            print("\t\tStudent record deleted successfully.")
            return
    print("\t\tStudent not found.")
menu()
