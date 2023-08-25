from math import sqrt,pi,exp


def Norm(m,e,x,cumulative=True):
    if cumulative:
        fonction = 0
        for i in range(0,x):
            fonction += (1/(2*e*sqrt(pi)))*exp(((i-m)/e)**2)
    else:
        fonction = (1/(2*e*sqrt(pi)))*exp(((x-m)/e)**2)
    return fonction


def Ajout():
    try:
        moy = -1
        ecart = -1
        X = -1
        while(moy<0):
            moy = float(input("Entrer la moyenne[m>0]: "))
        while(ecart<0):
            ecart = float(input("Entrer l'ecart-type[e>0]: "))
        while(X<0):
            X = int(input("Entrer la valeur a chercher[X>0]: "))
        return moy,ecart,X
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
    moyenne,ecartType,x = Ajout()
    cumul = IsCumul()
    normale = Norm(moyenne,ecartType,x,cumul)
    print("P(X=",x,")= ",normale)