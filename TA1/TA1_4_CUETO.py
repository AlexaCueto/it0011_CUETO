#1
#333
#55555
#666666
#7777777

print("(B) WHILE NESTED LOOP")

i = 1
while i <= 7: #prints the number of rows
    if i % 2 != 0:  #odd numbers
        j = 1
        while j <= i:
            print(i, end="")
            j += 1
        print()  #next line
    i += 1  
