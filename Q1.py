from math import sqrt

def analyse_position(liste_tuple):
    positions = []
    distances = []
    dict_retour = {}
    ensemble_x_unique = set()


    for position in liste_tuple:
        distances.append(sqrt((position[0] ** 2 + position[1]) ** 2))
        ensemble_x_unique.add(position[0])
        positions.append(position)
        positions.sort()

    #x>y
    liste_x_decrois = list(filter(lambda x: x[0] > x[1], liste_tuple))
    liste_x_decrois.sort()

    #calculer moyenne
    distance_moyenne = sum(distances) / len(distances)

    #sortie
    dict_retour['distance moyenne'] = distance_moyenne
    dict_retour['positions la plus éloigner'] = positions[-1]
    dict_retour['Position x > y'] = liste_x_decrois
    dict_retour['Ensemble x unique'] = ensemble_x_unique

    return dict_retour

positions = [(1, 0), (2, 2), (0, 1), (2, 2)]
resultat = analyse_position(positions)
print(resultat)

