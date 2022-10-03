#Programme 1
#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    nb_seconde_total = temps[0] * 24 * 3600 + temps[1] * 3600 + temps[2] * 60 + temps[3]
    return nb_seconde_total

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))   

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    temps_0 = seconde // (24 * 3600)
    temps_1 =  seconde // 3600 - (temps_0 * 24)
    temps_2 = seconde // 60 - (temps_0 * 1440 + temps_1 * 60)
    temps_3 = seconde - (temps_0 * 86400 + temps_1 * 3600 + temps_2 * 60)
    return temps_0, temps_1, temps_2, temps_3
    
temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")







#Programme 2

#fonction auxiliaire ici
def mot_pluriel(x):
    x += "s"
    return x 



def afficheTemps(temps):
    temps_0 = temps[0]
    temps_1 = temps[1]
    temps_2 = temps[2]
    temps_3 = temps[3]
    if temps_0 > 1:
        print(temps_0, mot_pluriel("jour"), " ", end = "")
    elif temps_0 == 1:
        print(temps_0, "jour", " ", end = "")
    else:
        print("", end = "")
    
    if temps_1 > 1:
        print(temps_1, mot_pluriel("heure"), " ", end = "")
    elif temps_1 == 1:
        print(temps_1, "heure", " ", end = "")
    else:
        print("", end = "")

    if temps_2 > 1:
        print(temps_2, mot_pluriel("minute"), " ", end = "")
    elif temps_2 == 1:
        print(temps_2, "minute", " ", end = "")
    else:
        print("", end = "")

    if temps_3 > 1:
        print(temps_3, mot_pluriel("seconde"), " ",  end = "")
    elif temps_3 == 1:
        print(temps_3, "seconde", " ", end = "")
    else:
        print("", end = "") 
    
afficheTemps(3, 10, 0, 1)





# Programme 3

def demandeTemps():
    '''Fonction qui demande à l'utilisateur de rentrer un nombre de jours, d'heures, de minutes et
de secondes.'''
    temps_utilisateur_0 = int(input("Entrez un jour"))
    temps_utilisateur_1 = int(input("Entrez une heure"))
    temps_utilisateur_2 = int(input("Entrez une minute"))
    temps_utilisateur_3 = int(input("Entrez une seconde"))
    while temps_utilisateur_1 > 24 or temps_utilisateur_2 > 60 or temps_utilisateur_3 > 60:
        print("Les valeurs saisies ne sont pas correcte, entrez de nouvelles valeurs sous la même forme.")
        temps_utilisateur_0 = int(input("Entrez un jour"))
        temps_utilisateur_1 = int(input("Entrez une heure"))
        temps_utilisateur_2 = int(input("Entrez une minute"))
        temps_utilisateur_3 = int(input("Entrez une seconde"))
    return temps_utilisateur_0, temps_utilisateur_1, temps_utilisateur_2, temps_utilisateur_3

afficheTemps(demandeTemps())


#Programme 4
def sommeTemps(temps1,temps2):
    sommeTempsEnSeconde = tempsEnSeconde(temps1) + tempsEnSeconde(temps2)
    sommeSecondeEnTemps = secondeEnTemps(sommeTempsEnSeconde) 
    afficheTemps(sommeSecondeEnTemps)
    
sommeTemps((2,3,4,25),(5,22,57,1))


#Programme 5
def proportionTemps(temps,proportion):
    proportionSeconde = tempsEnSeconde(temps) * proportion
    return secondeEnTemps(proportionSeconde)

afficheTemps(proportionTemps(proportion = 0.2, temps = (2,0,36,0)))
#appeler la fonction en échangeant l'ordre des arguments



#Programme 6
def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    nb_seconde_total = temps[0] * 24 * 3600 + temps[1] * 3600 + temps[2] * 60 + temps[3]
    return nb_seconde_total

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    temps_0 = seconde // (361 * 24 * 3600)
    temps_1 = seconde // (24 * 3600) - (temps_0 * 361)
    temps_2 =  seconde // 3600 - (temps_0 * 361 * 24 + temps_1 * 24)
    temps_3 = seconde // 60 - (temps_0 * 361 * 24* 60 + temps_1 * 1440 + temps_2 * 60)
    temps_4 = seconde - (temps_0 * 361 * 24 * 3600 + temps_1 * 86400 + temps_2 * 3600 + temps_3 * 60)
    return temps_0, temps_1, temps_2, temps_3, temps_4


    
def tempsEnDate(temps):
    dateEnSeconde = tempsEnSeconde(temps)
    return secondeEnTemps(dateEnSeconde)
    

def mot_pluriel(x):
    x += "s"
    return x 



def afficheTemps(temps):
    temps_0 = temps[0]
    temps_1 = temps[1]
    temps_2 = temps[2]
    temps_3 = temps[3]
    temps_4 = temps[4]
    if temps_0 > 1:
        print(temps_0, mot_pluriel("an"), " ", end = "")
    elif temps_0 == 1:
        print(temps_0, "an", " ", end = "")
    else:
        print("", end = "")
    if temps_1 > 1:
        print(temps_1, mot_pluriel("jour"), " ", end = "")
    elif temps_1 == 1:
        print(temps_1, "jour", " ", end = "")
    else:
        print("", end = "")
    
    if temps_2 > 1:
        print(temps_2, mot_pluriel("heure"), " ", end = "")
    elif temps_2 == 1:
        print(temps_2, "heure", " ", end = "")
    else:
        print("", end = "")

    if temps_3 > 1:
        print(temps_3, mot_pluriel("minute"), " ", end = "")
    elif temps_3 == 1:
        print(temps_3, "minute", " ", end = "")
    else:
        print("", end = "")

    if temps_4 > 1:
        print(temps_4, mot_pluriel("seconde"), " ",  end = "")
    elif temps_4 == 1:
        print(temps_4, "seconde", " ", end = "")
    else:
        print("", end = "") 

    

def afficheDate():
    return afficheTemps(tempsEnDate(temps))
    
temps = secondeEnTemps(100000000000)
afficheDate()


#Programme 7
#tester ici les fonctions de la librairie time

from time import time 
def tempsEnDate(temps):
    return secondeEnTemps(time())

afficheDate()
