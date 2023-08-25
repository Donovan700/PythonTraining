def Bern(p):
    esp = p
    q=1-p
    variance = p*q
    return esp,variance,q


def Ajout():
    try:
        p=-1
        while(p<0 or p>1):
            p = float(input("Entrer la probabilite de succes[0<p<1]: "))
        return p
    except:
        print("Veuillez entrer que des nombres!!!!")
        return Ajout()

if __name__ == '__main__':
    P = Ajout()
    esperance,Variance,Q = Bern(P)
    print("L'esperance est ",esperance)
    print("La variance est ",Variance)
    print("La probabilité d'echec est ",Q)