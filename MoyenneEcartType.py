#Code from scratch


from math import sqrt
Serie = []

def descr(Serie):
    return Moyenne(Serie),EcartType(Serie)

def Moyenne(list):
    sum=0
    for i in list:
        sum += i
    moyenne = sum/(len(list))
    return moyenne

def EcartType(list):
    SerieCarre(Serie)
    et = sqrt((MoyenneCarre(Serie)-Moyenne(Serie)**2)/len(Serie))
    return et

def SerieCarre(list):
    SerieC = []
    for elem in Serie:
        elem = elem**2
        SerieC.append(elem)
    return SerieC

def MoyenneCarre(list):
    serieCarre = SerieCarre(Serie)
    moyCarre = Moyenne(serieCarre)
    return moyCarre

def AjoutNombre(list):
    try:
        taille = int(input("Entrer la taille de la serie: "))
        if(taille<=0):
            print("La taille doit etre positif et non nul!")
            AjoutNombre(Serie)
        else:
            for i in range(0,taille):
                print("+++",i+1," occurence +++")
                i = int(input("Entrer un chiffre: "))
                list.append(i)
    except:
        print("Vous devez entrer un chiffre!")
        AjoutNombre(Serie)

if __name__ == '__main__':
    AjoutNombre(Serie)
    moyenne,et = descr(Serie)
    print("Moyenne: ",moyenne)
    print("Ecart-type: ",et)