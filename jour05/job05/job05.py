def distance_toilettes(marches: int, hauteur: int) -> float:
    hauteur_en_metres = hauteur / 100  # conversion en mètres
    distance_quotidienne = marches * hauteur_en_metres * 5  # distance quotidienne en mètres
    distance_hebdomadaire = distance_quotidienne * 7
    return round(distance_hebdomadaire, 2)
distance_toilettes(50, 20)
'Pour 50 marches de 20 cm, le gardien parcours 525.00 m par semaine.'
