def draw_rectangle(width, height):
    # Dessine la première ligne avec des '-' en haut du rectangle
    print("|" + "-"*(width-2) + "|")
    
    # Dessine les lignes du milieu avec un '|' vide de chaque côté
    for i in range(height-2):
        print("|" + " "*(width-2) + "|")
    
    # Dessine la dernière ligne avec des '-' en bas du rectangle
    print("|" + "-"*(width-2) + "|")
print (draw_rectangle(10, 20))