# CUETO, ALEXA JOYCE G
# TW23
# LIST AND TUPLES

students = []  # Stores student records as tuples
filename = "StudentsRecords.txt"  # Default file for saving and loading records

def openFile():
    global students
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
        students = []
        for line in lines:
            studentID, firstName, lastName, classStanding, majorExam = line.strip().split("|")
            students.append((studentID, (firstName, lastName), float(classStanding), float(majorExam)))
        print(f"File '{filename}' loaded successfully.")
    except FileNotFoundError:
        print(f"File '{filename}' not found. No records loaded.")

def saveFile():
    with open(filename, "w") as file:
        for student in students:
            file.write(f"{student[0]}|{student[1][0]}|{student[1][1]}|{student[2]}|{student[3]}\n")
    print(f"Records saved successfully to '{filename}'.")

def saveAsFile():
    new_filename = input("Enter new filename (with .txt extension): ")
    with open(new_filename, "w") as file:
        for student in students:
            file.write(f"{student[0]}|{student[1][0]}|{student[1][1]}|{student[2]}|{student[3]}\n")
    print(f"Records saved successfully as '{new_filename}'.")

def showAllRecords():
    while True:
        print("\n\t\t--SHOW RECORD--")
        print("\t\t1. Order by Last Name")
        print("\t\t2. Order by Grade")
        print("\t\t3. Back to Main Menu")
        
        subChoice = input("Enter your choice (number): ")

        if subChoice == "1":
            orderLastName()
        elif subChoice == "2":
            orderGrade()
        elif subChoice == "3":
            return  
        else:
            print("Invalid choice. Please try again.")

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
        
        choice = input("Enter your choice (number): ")

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
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")
            
def addRecord():
    print("\n\t\t--ADD RECORD--")
    studentID = input("Enter Student ID (6 digits): ")
    if len(studentID) != 6 or not studentID.isdigit():
        print("Invalid ID. Must be 6 digits.")
        return
    
    firstName = input("Enter First Name: ")
    lastName = input("Enter Last Name: ")
    classStanding = float(input("Enter Class Standing Grade: "))
    majorExam = float(input("Enter Major Exam Grade: "))

    students.append((studentID, (firstName, lastName), classStanding, majorExam))
    print("Student record added successfully.")
    
def orderLastName():
    sortedStudents = sorted(students, key=lambda s: s[1][1])  # Sort by last name
    print("\n\t\t--STUDENT RECORDS (Ordered by Last Name)--")
    for student in sortedStudents:
        print(student)

def orderGrade():
    sortedStudents = sorted(students, key=lambda s: (0.6 * s[2] + 0.4 * s[3]), reverse=True)
    print("\n\t\t--STUDENT RECORDS (Ordered by Grade)--")
    for student in sortedStudents:
        print(student)

def showRecord():
    studentID = input("Enter Student ID: ")
    for student in students:
        if student[0] == studentID:
            print("\n\t\t--STUDENT RECORD--")
            print(f"ID: {student[0]}, Name: {student[1][0]} {student[1][1]}, Class Standing: {student[2]}, Exam: {student[3]}")
            return
    print("Student not found.")

def editRecord():
    studentID = input("Enter Student ID to Edit: ")
    for i, student in enumerate(students):
        if student[0] == studentID:
            firstName = input("Enter New First Name: ")
            lastName = input("Enter New Last Name: ")
            classStanding = float(input("Enter New Class Standing Grade: "))
            majorExam = float(input("Enter New Major Exam Grade: "))
            
            students[i] = (studentID, (firstName, lastName), classStanding, majorExam)
            print("Student record updated successfully.")
            return
    print("Student not found.")

def deleteRecord():
    studentID = input("Enter Student ID to Delete: ")
    for i, student in enumerate(students):
        if student[0] == studentID:
            del students[i]
            print("Student record deleted successfully.")
            return
    print("Student not found.")
    

menu()
