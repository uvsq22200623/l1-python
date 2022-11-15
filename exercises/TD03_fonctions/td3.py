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
    temps_0 = seconde // (365 * 24 * 3600)
    temps_1 = seconde // (24 * 3600) - (temps_0 * 365)
    temps_2 =  seconde // 3600 - (temps_0 * 361 * 24 + temps_1 * 24)
    temps_3 = seconde // 60 - (temps_0 * 365 * 24* 60 + temps_1 * 1440 + temps_2 * 60)
    temps_4 = seconde - (temps_0 * 365 * 24 * 3600 + temps_1 * 86400 + temps_2 * 3600 + temps_3 * 60)
    return temps_0, temps_1, temps_2, temps_3, temps_4
    
temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")
