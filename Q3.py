from abc import ABC, abstractmethod

class Entites(ABC):
    def __init__(self, nom: str, annee_arrivee: int):
        self.nom = nom
        self.annee_arrivee = annee_arrivee

    @abstractmethod
    def description(self):
        pass

    def __str__(self):
        return f'Nom: {self.nom}, Annee: {self.annee_arrivee}'

class Animals(Entites):
    def __init__(self, nom: str, annee_arrivee: int, especes: str):
        super().__init__(nom, annee_arrivee)
        self.especes = especes

    def description(self):
        return f"Animal : {self.especes}"

class Enclos(Entites):
    def __init__(self, nom: str, annee_arrivee: int, capacite: int):
        super().__init__(nom, annee_arrivee)
        self.capacite = capacite

    def description(self):
        return f"Enclo capacité: {self.capacite}"

class ParcAnimalier:
    def __init__(self):
        self.entites = []

    def ajouter_entites(self, *entites):
        for entite in entites:
            self.entites.append(entite)


    def entiter_par_annee(self, min_annee):
        liste_reponses = []
        for entite in self.entites:
            if entite.annee_arrivee >= min_annee:
                liste_reponses.append(entite)
        liste_reponses.sort(key=lambda x: x.annee_arrivee)
        return liste_reponses

parc = ParcAnimalier()
parc.ajouter_entites(Animals("Simba", 2019, "Lion"), Enclos("Savane",
2021, 10))
entites = parc.entiter_par_annee(2020)
for entite in entites:
    print(entite.description())

print([str(e) for e in entites])







