def unif(n):
    p = 1/n
    esp = (n+1)/2
    variance = (n**2 -1)/12
    return p,esp,variance


def Ajout():
    try:
        n = -1
        while(n<0):
            n = int(input("Entrer le nombre n[n>0]: "))
        return n
    except:
        print("Veuillez entrer que des nombres!!!")
        return Ajout()

if __name__ == '__main__':
    N = Ajout()
    P,E,V = unif(N)
    print("La probabilite est ",P)
    print("L'esperance est ",E)
    print("La variance est ",V)