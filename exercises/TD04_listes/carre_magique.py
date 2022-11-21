#1er exo
carre_mag = [[4,14,15,1], [9,7,6,12], [5,11,10,8], [16,2,3,13]]
"""#1ère solution
carre_pas_mag = []
for i_lignes in len(carre_mag):
    carre_pas_mag.append([])
    for j_colonnes in range (len(carre_pas_mag[i_lignes])):
        carre_pas_mag[i_lignes].append(carre_mag[i_lignes][j_colonnes]) 
#2ème solution
carre_pas_mag = []
for lignes in carre_mag:
    carre_pas_mag.append(lignes.copy())"""
#3ème solution
carre_pas_mag = [lignes[:] for lignes in carre_mag]
"""[:] permet d'aller du premier élément de la liste au dernier"""
carre_pas_mag[3][2] = 7

def affichecarre(carre):
    for i in carre:
        print(i)
    print(i)

#2ème exo
def testLignesEgale(carre):
    somme = sum(carre[0])
    for lignes in carre:
        if sum(lignes) ! = somme:
            return -1
    return somme
print(testLignesEgale(carre_mag))
print(testLignesEgale(carre_pas_mag))

#3ème exo
def testColonnesEgales(carre):
    colonne_1 = [lignes[0] for lignes in carre]
    somme = sum(colonne_1)
    for j in range(1, len(carre)):
        colonne = [lignes[j] for lignes in carre]
        if sum(colonne) != somme:
            return -1
    return somme

print(testColonnesEgales(carre_mag))
print(testColonnesEgales(carre_pas_mag))

#4ème exo
def testDiagonalesEgales(carre):
    taille = len(carre)
    diag_1 = [carre[i][i] for i in range taille ]
    diag_2 = [carre[i][taille -i -1] for i in range taille]
    somme = sum(diag_1)
    if sum(diag_2) != somme:
        return -1
    return somme
    
    print(testDiagonalesEgales(carre_mag))
print(testDiagonalesEgales(carre_pas_mag))

#5ème exo
def estNormal(carre):
    liste = []
    for lignes in carre:
        liste.extend(lignes)
    taille = len(carre)
    for entier in range(1, taille * taille + 1):
        if entier not in list:
            return False
        return True
print(estNormal(carre_mag))
print(estNormal(carre_mag))