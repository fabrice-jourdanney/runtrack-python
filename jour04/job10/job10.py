L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
produit = 1

for x in L:
    if x >= 25 and x <= 90:
        produit *= x

print("Le produit des valeurs de la liste dans l'intervalle [25, 90] est :", produit)
