

case1=""
case2=""
case3=""
case4=""
case5=""
case6=""
case7=""
case8=""
case9=""
entrecase="---"

print(case1,entrecase,case2,entrecase,case3)
print(case4,entrecase,case5,entrecase,case6)
print(case7,entrecase,case8,entrecase,case9)

boucle=1
while (boucle!=0):
    print("Joueur X")
    joueurX=input()
    if (joueurX == '1'):
        case1= "X"
    if (joueurX == '2'):
        case2= "X"
    if (joueurX == '3'):
        case3= "X"
    if (joueurX == '4'):
        case4= "X"
    if (joueurX == '5'):
        case5= "X"
    if (joueurX == '6'):
        case6= "X"
    if (joueurX == '7'):
        case7= "X"
    if (joueurX == '8'):
        case8= "X"
    if (joueurX == '9'):
        case9= "X"
    

    print(case1,entrecase,case2,entrecase,case3)
    print(case4,entrecase,case5,entrecase,case6)
    print(case7,entrecase,case8,entrecase,case9)

    if (case1==case2==case3):
        print("La partie est terminé Joueur X à gagné")
    print("Joueur O")
    joueurO=input()
    if (joueurO == '1'):
        case1= "O"
    if (joueurO == '2'):
        case2= "O"
    if (joueurO == '3'):
        case3= "O"
    if (joueurO == '4'):
        case4= "O"
    if (joueurO == '5'):
        case5= "O"
    if (joueurO == '6'):
        case6= "O"
    if (joueurO == '7'):
        case7= "O"
    if (joueurO == '8'):
        case8= "O"
    if (joueurO == '9'):
        case9= "O"

    print(case1,entrecase,case2,entrecase,case3)
    print(case4,entrecase,case5,entrecase,case6)
    print(case7,entrecase,case8,entrecase,case9)