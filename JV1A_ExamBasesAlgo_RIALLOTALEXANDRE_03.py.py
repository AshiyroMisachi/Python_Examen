myTable = [72,26,31,86,42]
print(myTable)
grand=myTable[0]
inversion=0
for tri in range (len(myTable)):
    #recherche élèment plus grand
    for recherche in range(len(myTable)):
        grand=myTable[recherche]
        if (grand < myTable[recherche]):
            grand = myTable(recherche)

    for i in range (len(myTable)):
        if (grand > myTable[i]):
            inversion=myTable[i-1]
            myTable[i-1] = myTable[i]
            myTable[i] = inversion
        print(myTable)

#Je pense que le tri à bulle est considéré comme lent car on doit comparé l'élément le plus grand
# avec l'entiérété de la liste pour le faire remonté et cela pour chaque numéro de la grille
# Malgré cela son temps d'exécution est proche d'une milliseconde     