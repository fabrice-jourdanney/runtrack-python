def ajouter_fruit():
    fruits = ["pomme", "cerise", "orange"]
    fruits.append("Melon")
    return fruits
# Appel de la fonction pour ajouter "Melon" à la liste "fruits"
nouvelle_liste = ajouter_fruit()

# Affichage de la nouvelle liste contenant "Melon"
print(nouvelle_liste)
