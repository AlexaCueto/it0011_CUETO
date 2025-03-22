#CUETO, ALEXA JOYCE G
#TW23
#OOP and Exception

class Item:
    def __init__(self, itemID, itemName, itemDesc, itemPrice): #constructor
        self.itemID = itemID #self is the instance of item class
        self.itemName = itemName
        self.itemDesc = itemDesc
        self.itemPrice  = itemPrice

    def __str__(self): #string representation of the object
        return f"\n\t\tItem ID: {self.itemID}\n\t\tItem Name: {self.itemName}\n\t\tItem Description: {self.itemDesc}\n\t\tItem Price: {self.itemPrice}" 

items ={}

def mainMenu():
    while True:
        print("\n\t\t--Item Management Application for Marketplace Items--")
        print("\n\t\t--Menu--")
        print("\t\t1. Add Item")
        print("\t\t2. Show All Items")
        print("\t\t3. Update Item")
        print("\t\t4. Delete Item")
        print("\t\t5. Exit")
        
        choice = input("\t\tEnter your choice: ")
        
        if choice == "1":
            addItem()
        elif choice == "2":
            showAllItems()
        elif choice == "3":
            updateItem()
        elif choice == "4":
            deleteItem()
        elif choice == "5":
            print("\t\tThank you for using the program!")
            break
        else:
            print("\t\tInvalid choice. Try again.")
        
def addItem():
    try: #exception handling
        itemID =int(input("\n\t\tEnter ITEM ID (5 DIGITS): ")) #inputs ID from user
        if itemID in items:  #checks if the ID already exists
            print("\t\tItem ID already exists.")
            return None
        
        if len(str(itemID)) != 5: #checks if the ID is not 5 digits
            print("\t\tItem ID must be 5 digits.")
            return None
        
        name = input("\t\tEnter Item Name: ")
        if name == "": #checks if the name is empty
            print("\t\tItem Name cannot be empty.")
            return None
        
        description = input("\t\tEnter Item Description: ")
        if description == "": #checks if the description is empty
            print("\t\tItem Description cannot be empty.")
            return None
        
        price = float(input("\t\tEnter Item Price: PHP "))
        if price <= 0.00: #checks if the price is less than or equal to zero
            print("\t\tItem Price must be greater than zero.")
            return None
        
        items[itemID] = Item(itemID, name, description, price) #adds the item to the dictionary
        print("\t\tItem ", itemID, " added successfully.")
    
    except ValueError:
        print("\t\tInvalid input. Please enter a valid value.")
        return None
    
def showAllItems():
    if not items:
        print("\t\tNo items to show.") #checks if there are no items to show
        return None
    else:
        print("\n\t\t--Items--")
        for itemID in items:
            print(items[itemID]) #prints the items
    
    
def updateItem():
    print("\n\t\t--Items--")
    for itemID in items:
        print(items[itemID]) #prints the items
            
    itemID = int(input("\n\t\tEnter Item ID to update (5 DIGITS): "))
    if itemID not in items:
        print("\t\tItem ID does not exist.")
        return None
    
    if len(str(itemID)) != 5:
        print("\t\tItem ID must be 5 digits.")
        return None
    
    try:
        name = input("\t\tEnter new name [Leave blank to retain current value]: ")
        if name:
            items[itemID].itemName = name
        
        description = input("\t\tEnter new description [Leave blank to retain current value]: ")
        if description:
            items[itemID].itemDesc = description
            
        price = input("\t\tEnter new price [Leave blank to retain current value]: PHP ")
        if price:
            price = float(price)
            if price <= 0.00:
                print("\t\tItem Price must be greater than zero.")
                return None
            items[itemID].itemPrice = price
        
        print("\t\tItem ", itemID, " updated successfully.")
    except ValueError:
        print("\t\tInvalid input. Please enter a valid value.")
        return None

def deleteItem():
    print("\n\t\t--Items--")
    for itemID in items:
        print(items[itemID]) #prints the items
        
    itemID =int(input("\n\t\tEnter Item ID to delete (5 DIGITS): "))
    if itemID in items:
        del items[itemID]
        print("\t\tItem ", itemID, " deleted successfully.")
    else:
        print("\t\tItem ID does not exist.")
        return None
        
    if len(str(itemID)) != 5:
        print("\t\tItem ID must be 5 digits.")
        return None

mainMenu()