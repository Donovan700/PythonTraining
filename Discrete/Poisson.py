from math import exp,factorial

def Poisson(labda,x,cumulative=True):
    if cumul:
        fish = 0.0
        for i in range(0,x):
            fish += exp(-labda)*((labda**i)/factorial(i))
    else:
        fish = exp(-labda)*((labda**x)/factorial(x))
    return fish


def Ajout():
    try:
        X = -1
        Labda = -1
        while(Labda<0):
            Labda = float(input("Entrer la valeur de labda[labda>0]: "))
        while(X<0):
            X = int(input("Entrer la valeur de x(P(X=x))[x>0]: "))
        return Labda,X
    except:
        print("Veuillez entrer que des nombres!!!")
        return Ajout()


def IsCumul():
    #Lecture de la variable cumul_input
    cumul_input = input("Cumulatif? (true/false): ")
    #Convertion en minuscule pour avoir la valeur vrai ou faux
    if cumul_input.lower() == "true":
        return True
    elif cumul_input.lower() == "false":
        return False
    else:
        print("Veuillez entrer True ou False!") #En cas d'erreur d'entrer,Appel recursif de la fonction
        return IsCumul()

if __name__ == '__main__':
    L,x = Ajout()
    cumul = IsCumul()
    Po = Poisson(L,x,cumul)
    print(Po)