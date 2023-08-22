 #importation de la librairie moyenne
from statistics import mean
from math import sqrt


#Fonction qui prends la taille et les valeurs de la série
def AjoutNombre():
    try:
        taille = int(input("Entrer la taille de la serie: "))
        if taille <= 0:
            print("La taille doit être positive et non nulle!")
            return AjoutNombre() #En cas de taille négatif,Appel récursif de la fonction
        else:
            Tableau = [] #Declaration d'un tableau vide
            for i in range(1, taille+1):
                print("\t+++", i, " occurence +++") #Affichage
                valeur = float(input("Entrer un reel: "))
                Tableau.append(valeur) #Ajout des valeurs entrées par saisie dans le tableau
            return Tableau
    except:
        print("Vous devez entrer un chiffre!")
        return AjoutNombre()


#Calcul de la variance

def Variance(list):
    #Retour la valeur null si la liste ne contient pas des valeurs
    if not list:
        return None
    moyen = mean(list)
    #Declaration et initialisation du tableau carré qui contient les valeurs de la liste au carré
    carre = [(x - moyen)**2 for x in list]
    variance = sum(carre) / len(list)
    return variance


#Fonction qui calcul la moyenne et l'ecart-type


def descr(list):
    #Calcul la moyenne de la série
    moyenne = mean(list)
    #Calcul l'ecart-type de la série
    ecart_type = sqrt(Variance(list))
    return moyenne,ecart_type


#Fonction Principal


if __name__ == '__main__':
    Serie = AjoutNombre()
    moyenne,ecart = descr(Serie)
    print("La moyenne: ", moyenne)
    print("L'ecart-type: ",ecart)
