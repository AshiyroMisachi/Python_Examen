myTable = [86,26,31,72,42]
print(myTable)
grand=myTable[0]
inversion=0
for entier in range(len(myTable)):
    for i in range (len(myTable)):
        if (grand > myTable[i]):
            grand=myTable[i-1]
            inversion=myTable[i-1]
            myTable[i-1] = myTable[i]
            myTable[i] = inversion
            print(myTable)