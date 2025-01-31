#Count the sum of the digits from a given input string digits.

stringDigit = (input("Enter a string digit: "))
i = stringDigit

print("The string digit you entered is: ", stringDigit)

sum = 0

for i in range(0, len(stringDigit)):
    if stringDigit[i].isdigit():
        sum = sum + int(stringDigit[i])

print("Sum of the digits: " , sum)