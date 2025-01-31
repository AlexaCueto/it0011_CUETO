#              1
#             12
#            123
#           1234
#          12345

print("(A) FOR NESTED LOOP")

for i in range(1,6): #prints the number of rows
    for j in range(5,i,-1): #prints the whitespaces
        print(" ",end="")
    for k in range(1,i+1): #prints the numbers
        print(k,end="")
    print()