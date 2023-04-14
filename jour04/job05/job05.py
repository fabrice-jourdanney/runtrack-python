# Créer la liste L d'entiers
L = [5, 10, 15, 20, 25]

# Afficher la valeur de L[1]
print("La valeur de L[1] est :", L[1])

# Écrire une fonction pour mettre à jour L[3]
def mettre_a_jour_L3(liste):
    liste[3] = liste[2] + liste[4]

# Mettre à jour L[3]
mettre_a_jour_L3(L)

# Afficher la valeur du dernier terme de la liste
print("La valeur du dernier terme de la liste est :", L[-1])
