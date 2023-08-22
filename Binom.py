#Importation de la librairie
from scipy.stats import binom


#Fonction ajout pour ajouter les valeurs n,k,p

def Ajout():
    try:
        #Initialisation de n,k,p
        n = -1 #n en tant que -1 pour entrer dans la boucle 
        k = -1 #k en tant que -1 pour entrer dans la boucle
        p = -1 #p en tant que -1 pour entrer dans la boucle
        while(n<0):
            n = int(input("Entrer le nombre de repetition(n positif): "))
        while(k>n or k<0): #0<k<n
            k = int(input("Entrer le nombre de succes(k) [0<k<n] : "))
        while(p<0 or p>1): #0<p<1
            p = float(input("Entrer la probabilite d'un succes(p) [0<p<1]: "))
        return n,k,p
    except:
        print("Veuillez entrer que des entier!!")
        return Ajout() #Appel récursif de la fonction en cas d'erreur
    


#Fonction qui determine si c'est cumulatif ou non


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


#Fonction qui calcul la loi binomiale

def binomiale(n, k, p, cumulative=True):
    binomial = binom(n, p) #Initialisation de l'objet binomiale avec les paramètres n,p
    
    if cumulative:
        return binomial.cdf(k) #Si c'est cumulatif,on calcul la probabilité cumulatif jusqu'à k-ième succès
    else:
        return binomial.pmf(k) #On calcul juste la probabilité sans cumulatif
    

#Fonction principale


if __name__ == '__main__':
    N,K,P = Ajout()
    cumulatif = IsCumul()
    print("P(X) = ",binomiale(N,K,P,cumulatif))