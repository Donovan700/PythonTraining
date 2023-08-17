from math import comb



def Ajout():
    try:
        n = -1
        k = -1
        p = -1
        while(n<0):
            n = int(input("Entrer le nombre de repetition(n positif): "))
        while(k>n or k<0):
            k = int(input("Entrer le nombre de succes(k) [0<k<n] : "))
        while(p<0 or p>1):
            p = float(input("Entrer la probabilite d'un succes(p) [0<p<1]: "))
        return n,k,p
    except:
        print("Veuillez entrer que des entier!!")
        Ajout()


def IsCumul():
    try:
        cumul = bool(input("Cumulatif?(True/False): "))
        return cumul
    except:
        print("Veuillez entrer True ou False!")
        IsCumul()


def binom(n,k,p,cumul=False):
    if cumul:
        combinaison = comb(n,k)
        x = combinaison*(p**k)*((1-p)**(n-k))
    else:
        x=0
        for i in range(0,n):
            combinaison = comb(n,i)
            x += combinaison*(p**k)*((1-p)**(n-k))
    return x

if __name__ == '__main__':
    N,K,P = Ajout()
    cumulatif = IsCumul()
    print("P(X) = ",binom(N,K,P,cumulatif))
