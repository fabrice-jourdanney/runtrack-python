def tri_croissant(liste):
    """
    Trie une liste dans l'ordre croissant.
    """
    liste_triee = sorted(liste)
    return liste_triee

# Exemple d'utilisation
ma_liste = [5, 3, 8, 1, 6]
liste_triee = tri_croissant(ma_liste)
print(liste_triee)
