L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
somme = 0

for nombre in L:
    if nombre % 2 == 0:  # Vérifie si le nombre est pair
        somme += nombre  # Ajoute le nombre pair à la somme totale

print("La somme des nombres pairs dans la liste est:", somme)

