#CUETO, ALEXA JOYCE G
#TW23
#FUNCTION

def mainMenu(): #Function to display menu
    while True:
        print("\n\t\t--MENU--")
        print("\t\t[D] Divide")
        print("\t\t[E] Exponentiation")
        print("\t\t[R] Remainder")
        print("\t\t[F] Summation")
        print("\t\t[X] Exit")
        
        choice =input("\t\tEnter your choice: ")
        
        if choice == "D" or choice == "d":
            division()
        elif choice == "E" or choice == "e":
            exponentiation()
        elif choice == "R" or choice == "r":
            remainder()
        elif choice == "F" or choice =="f":
            summation()
        elif choice =="X" or choice == "x":
            print("\t\tThank you for using the program!")
            break
        else:
            print("\t\tInvalid choice. Try again")


def division():
    firstNumber = input("\n\t\tEnter your first numer: ")
    secondNumber = input("\t\tEnter your second number: ")
    
    if secondNumber == "0": #Error Handling
        print("\t\tThe second number must not be equal to zero.")
        return None
    else:
        result = int(firstNumber) / int(secondNumber)
        print(f"\n\t\tThe result of {firstNumber} divided by {secondNumber} is {result}")
        return result
    
    
def exponentiation():
    baseNumber = input("\n\t\tEnter your base number: ")
    exponentNumber = input("\t\tEnter your exponent number: ")
    
    if exponentNumber < "0" and baseNumber == "0" : #Error Handling
        print("\t\tThe base number must not be equal to zero if the exponent is less than zero.")
        return None
    else:    
        result = int(baseNumber) ** int(exponentNumber)
        print(f"\n\t\tThe result of {baseNumber} raised to the power of {exponentNumber} is {result}")
        return result
    
def remainder():
    firstNumber = input("\n\t\tEnter your first number: ")
    secondNumber = input("\t\tEnter your second numer: ")
    
    if secondNumber == "0": #Error Handling
        print("\t\tThe second number must not be equal to zero.")
        return None
    else:
        result = int(firstNumber) % int(secondNumber)
        print(f"\n\t\tThe remainder of {firstNumber} divided by {secondNumber} is {result}")
        return result
    
def summation():
    firstNumber = input("\n\t\tEnter your first number: ")
    secondNumber = input("\t\tEnter your second number: ")
    
    if secondNumber <= firstNumber: #Error Handling
        print("\t\tThe second number must be greater than the first number.")
        return None
    else:
        result = sum(range(int(firstNumber), int(secondNumber) + 1))
        print(f"\n\t\tThe sum of {firstNumber} to {secondNumber} is {result}")
        return result

mainMenu()