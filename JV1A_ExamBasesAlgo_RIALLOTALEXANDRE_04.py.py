haut = [0,0,0]
milieu = [0,0,0]
bas = [0,0,0]
boucle=1
print(haut)
print(milieu)
print(bas)

while (boucle!= 0):
    print("C'est à X de jouer")
    joueur1=input()

    if (joueur1=='1'):
        haut[0]= "x"
    if (joueur1=='2'):
        haut[1]= "x"
    if (joueur1=='3'):
        haut[2]= "x"
    if (joueur1=='4'):
        milieu[0]= "x"
    if (joueur1=='5'):
        milieu[1]= "x"
    if (joueur1=='6'):
        milieu[2]= "x"
    if (joueur1=='7'):
        bas[0]= "x"
    if (joueur1=='8'):
        bas[1]= "x"
    if (joueur1=='9'):
        bas[2]= "x"

    print(haut)
    print(milieu)
    print(bas)

    print("C'est à O de jouer")
    joueur2=input()

    if (joueur2=='1'):
        haut[0]= "o"
    if (joueur2=='2'):
        haut[1]= "o"
    if (joueur2=='3'):
        haut[2]= "o"
    if (joueur2=='4'):
        milieu[0]= "o"
    if (joueur2=='5'):
        milieu[1]= "o"
    if (joueur2=='6'):
        milieu[2]= "o"
    if (joueur2=='7'):
        bas[0]= "o"
    if (joueur2=='8'):
        bas[1]= "o"
    if (joueur2=='9'):
        bas[2]= "o"

    print(haut)
    print(milieu)
    print(bas)

