# Définir une liste non vide
liste = [1, 2, 3, 4, 5]

# Afficher la liste avant l'échange
print("Liste avant échange : ", liste)

# Échanger les valeurs de la première et de la dernière case
liste[0], liste[-1] = liste[-1], liste[0]

# Afficher la liste après l'échange
print("Liste après échange : ", liste)
