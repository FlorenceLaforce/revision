from math import sqrt

def grouper_mouvements(liste_mouvement):
    dict_retour = {}
    for mouvement in liste_mouvement:
        key = f"{sqrt(mouvement[0]**2 + mouvement[1]**2)}" 
        if not key in dict_retour:
            dict_retour[f"{sqrt(mouvement[0]**2 + mouvement[1]**2)}"] = set()
        dict_retour[f"{sqrt(mouvement[0] ** 2 + mouvement[1] ** 2)}"].add(mouvement)


    return dict_retour

mouvements = [(1, 0), (0, 1), (1, 1), (1, 0)]
resultat = grouper_mouvements(mouvements)
print(resultat)
