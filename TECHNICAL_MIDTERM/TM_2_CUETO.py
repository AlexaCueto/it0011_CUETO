#CUETO, ALEXA JOYCE G.
#TW23
#TRANSLATE GIVEN DATE FORMAT TO MORE HUMAN READABLE

inputDate = input("Enter date (MM/DD/YY): ")

def dateFormat(inputDate):
    month, day, year = inputDate.split("/")
    
    months ={ #dictionary of months
        1: "January", 2: "February", 3: "March", 4: "April",
        5: "May", 6: "June", 7: "July", 8: "August",
        9: "September", 10: "October", 11: "November", 12: "December"
    }
    
    if int(month) not in months:
        print("You have entered an invalid month.")
        return
    
    month = months[int(month)]
    if len(year) == 2:
        year = "20" + year
    else:
        year = year
    
    print(f"Date Output: {month} {int(day)}, {year}")

dateFormat(inputDate)