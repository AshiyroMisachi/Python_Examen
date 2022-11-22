myTable = [86,26,31,72,42]
print(myTable)
grand=myTable[0]
inversion=0
positiongrand=0
for i in range (len(myTable)):
    for c in range (i,len(myTable)):
        if (grand>myTable[c]):
            grand=myTable[c]
            positiongrand=c
        inversion=myTable[i]
        myTable[positiongrand]=inversion
        myTable[i]=grand
        print(myTable)