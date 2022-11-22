myTable = [42,26,31,72,86]
inversion=0
print(myTable)

inversion = myTable[0]
myTable[0] = myTable [4]
myTable [4] = inversion

print(myTable)