from statistics import variance, mean, stdev

def AjoutNombre():
    try:
        taille = int(input("Entrer la taille de la serie: "))
        if taille <= 0:
            print("La taille doit être positive et non nulle!")
            return AjoutNombre()
        else:
            Serie = []
            for i in range(1, taille + 1):
                print("\t+++", i, " occurence +++")
                valeur = float(input("Entrer un reel: "))
                Serie.append(valeur)
            return Serie
    except:
        print("Vous devez entrer un chiffre!")
        return AjoutNombre()

def descr(list):
    moyenne = mean(list)
    ecart_type = stdev(list)
    return moyenne,ecart_type

if __name__ == '__main__':
    Serie = AjoutNombre()
    moyenne,ecart = descr(Serie)
    print("La variance est: ", variance(Serie))
    print("La moyenne: ", moyenne)
    print("L'ecart-type: ",ecart)
