#temps[0] = Jour; temps[1] = heure; temps[2] = minute; temps[3] = seconde

temps = (4, 3, 13, 20)

def TempsEnSeconde(temps):
    nb_seconde_total = temps[0] * 24 * 3600 + temps[1] * 3600 + temps[2] * 60 + temps[3]
    return nb_seconde_total

print("Le nombre de seconde total est de", TempsEnSeconde(temps))



#Programme 2
#temps_0 = Jour; temps_1 = heure; temps_2 = minute; temps_3 = seconde
nb_de_seconde = 357200

def Temps_Correspondant(nb_de_seconde):
    '''Cette fonction prend un nombre de secondes et renvoie le temps correspondant'''
    temps_0 = nb_de_seconde // (24 * 3600)
    temps_1 =  nb_de_seconde // 3600 - (temps_0 * 24)
    temps_2 = nb_de_seconde // 60 - (temps_0 * 1440 + temps_1 * 60)
    temps_3 = nb_de_seconde - (temps_0 * 86400 + temps_1 * 3600 + temps_2 * 60)
    return temps_0, "jours", temps_1, "heures", temps_2, "minutes et", temps_3, "secondes"

print("Le temps correspondant est", Temps_Correspondant(nb_de_seconde))



#Programme 3

nb_de_seconde = 3600

temps_0 = nb_de_seconde // (24 * 3600)
temps_1 =  nb_de_seconde // 3600 - (temps_0 * 24)
temps_2 = nb_de_seconde // 60 - (temps_0 * 1440 + temps_1 * 60)
temps_3 = nb_de_seconde - (temps_0 * 86400 + temps_1 * 3600 + temps_2 * 60)

def afficheTemps(nb_de_seconde):
    '''Cette fonction prend un nombre de secondes et renvoie le temps correspondant'''
    temps_0 = nb_de_seconde // (24 * 3600)
    temps_1 =  nb_de_seconde // 3600 - (temps_0 * 24)
    temps_2 = nb_de_seconde // 60 - (temps_0 * 1440 + temps_1 * 60)
    temps_3 = nb_de_seconde - (temps_0 * 86400 + temps_1 * 3600 + temps_2 * 60)
    return temps_0, temps_1, temps_2, temps_3,

def mot_pluriel(x):
    x += "s"
    return x 

if temps_0 > 1:
    print(temps_0, mot_pluriel("jour"), " ", end = "")
elif temps_0 == 1:
    print(temps_0, "jour", " ", end = "")
else:
    print("")
    
if temps_1 > 1:
    print(temps_1, mot_pluriel("heure"), " ", end = "")
elif temps_1 == 1:
    print(temps_1, "heure", " ", end = "")
else:
    print("")

if temps_2 > 1:
    print(temps_2, mot_pluriel("minute"), " ", end = "")
elif temps_2 == 1:
    print(temps_2, "minute", " ", end = "")
else:
    print("")

if temps_3 > 1:
    print(temps_3, mot_pluriel("seconde"), " ",  end = "")
elif temps_3 == 1:
    print(temps_1, "seconde", " ", end = "")
else:
    print("")



# Programme 4

# temps_utilisateur[0] = jour, temps_utilisateur[1] = heure, temps_utilisateur[2] = minute, temps_utilisateur[3] = seconde

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



def TempsEnSeconde(temps_utilisateur):
    '''Cette fonction prend comme argument le temps et renvoie le nombre de seconde total correspondant
    à ce temps.'''
    nb_seconde_total = temps_utilisateur_0 * 24 * 3600 + temps_utilisateur_1 * 3600 + temps_utilisateur_2 * 60 + temps_utilisateur_3
    return nb_seconde_total

print("Le nombre de seconde total est de", TempsEnSeconde(temps))