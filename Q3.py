import csv
from abc import ABC, abstractmethod

class Entites(ABC):
    def __init__(self, nom, annee_arrivee):
        self.nom = nom
        self.annee_arrivee = annee_arrivee

    @abstractmethod
    def description(self):
        pass

    def __str__(self):
        return f'Nom: {self.nom}, Annee: {self.annee_arrivee}'

class Animals(Entites):
    def __init__(self, nom, annee_arrivee, especes):
        super().__init__(nom, annee_arrivee)
        self.especes = especes


#numero 4
    def __lt__(self, e1):
        if self.annee_arrivee < e1.annee_arrivee:
            return True
        elif self.annee_arrivee == e1.annee_arrivee:
            if ord(self.nom[0]) > ord(e1.nom[0]):
                return True
        else:
            return False
    def description(self):
        return f"Animal : {self.especes}"

class Enclos(Entites):
    def __init__(self, nom, annee_arrivee, capacite):
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

def sauvegarder_parc(parc, fichier):
    with open(fichier, 'w', newline='') as cvsfile:
        fichier = csv.writer(cvsfile)
        fichier.writerow(['type', 'Nom', 'Annee_arrivee', 'espece', 'Capacite'])
        for entite in parc.entites:
            if isinstance(entite, Animals):
                fichier.writerow([entite.__class__.__name__, entite.nom, entite.annee_arrivee, entite.especes])
            elif isinstance(entite, Enclos):
                fichier.writerow([entite.__class__.__name__, entite.nom, entite.annee_arrivee, '', entite.capacite])

def charger_parc(fichier):
    with open(fichier, 'r', newline='') as cvsfile:
        parc = ParcAnimalier()
        fichier = csv.reader(cvsfile)
        for entite in fichier:
            if entite[0] == 'Animals':
                parc.ajouter_entites(Animals(entite[1], entite[2], entite[3]))
            if entite[0] == 'Enclos':
                parc.ajouter_entites(Enclos(entite[1], entite[2], entite[4]))
    return parc

parc = ParcAnimalier()
parc.ajouter_entites(Animals("Simba", 2019, "Lion"), Enclos("Savane",
2021, 10))
entites = parc.entiter_par_annee(2020)
for entite in entites:
    print(entite.description())

print([str(e) for e in entites])

a1 = Animals("Simba", 2019, "Lion")
a2 = Animals("Nala", 2019, "Lion")
a3 = Animals("Dumbo", 2017, "Éléphant")
print(a1 < a2)
print(a1 < a3)

parc = ParcAnimalier()
parc.ajouter_entites(Animals("Simba", 2019, "Lion"), Enclos("Savane",
2021, 10))
sauvegarder_parc(parc, "parc.csv")
nouveau_parc = charger_parc("parc.csv")
print([str(e) for e in nouveau_parc.entites])




