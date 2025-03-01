#CUETO, ALEXA JOYCE G
#TW23
#DICTIONARY

import csv

exchangeRates ={} #Initialize as dictionary

with open("currency.csv", mode="r") as file:
    reader = csv.reader(file)
    next(reader) 
    for row in reader:
        code, name, rate = row
        exchangeRates[code] = float(rate)
        
dollarMoney = float(input("How much dollar do you have? "))
currency = input("What currency do you want to have? ")

if currency in exchangeRates:
    convertedMoney = dollarMoney * exchangeRates[currency]
    print(f"\nDollar: {dollarMoney} USD")
    print(f"{currency}: {convertedMoney:.9f}")
else:
    print("Currency not found")
