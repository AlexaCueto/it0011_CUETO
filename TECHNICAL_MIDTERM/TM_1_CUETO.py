#CUETO, ALEXA JOYCE G.
#TW23
#CHECK IF THE SUM IS A PALINDROME IN THE FILE NUMBERS.TXT
def palindrome(number):
    number = str(number)
    if number == number[::-1]:
        print("The sum of these numbers is a palindrome.\n")
        return True
    else:
        print("The sum of these numbers is not a palindrome.\n")
        return False

file1 = open("numbers.txt", "r")
numbers = file1.readlines()
file1.close()

for i, line in enumerate(numbers, 1):
    number_list = [int(numbers) for numbers in line.strip().split(',') if numbers.strip()]
    if number_list:
        total = sum(number_list)
        print(f"{i}: {' + '.join(str(numbers) for numbers in number_list)} = {total}")
        palindrome(total)      


