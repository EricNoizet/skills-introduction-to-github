# Exercice : Tirage d'une boule blanche après avoir tiré une boule noire

# Supposons que nous ayons une urne contenant 6 boules noires et 4 boules blanches. Nous effectuons des tirages sans remise jusqu'à obtenir la première boule noire. Ensuite, nous continuons à tirer des boules sans remise jusqu'à obtenir la première boule blanche après avoir tiré une boule noire.

# Votre tâche consiste à écrire un programme Python qui simule ce processus de tirage et qui calcule le nombre total de boules que nous devons tirer (y compris la dernière boule) pour obtenir la première boule blanche après avoir tiré une boule noire.


## import des bibliothèques
import random
import numpy as np

def tirage_boules(nb_boules_noires, nb_boules_blanches):
    urne = ['N'] * nb_boules_noires + ['B'] * nb_boules_blanches
    random.shuffle(urne)
    # print(urne)
    nb_boules_tirees = 0
    noire_tiree = False

    for i in range (len(urne)):

        if urne[i] == 'N':
            noire_tiree = True
        elif urne[i] == 'B' and noire_tiree:
            return i+1      # return i donne le numéro de l'élément blanc

    return "pas d'évènement" # si on a tiré toutes les blanches en premier


def tirage_boules_2(nb_boules_noires, nb_boules_blanches):
    urne = [0] * nb_boules_noires + [1] * nb_boules_blanches
    random.shuffle(urne)
    # print(urne)
    for i in range (len(urne)):
        if urne[i] == 1:
            if np.prod(np.array(urne[0:i])) == 0:
                return i+1      # return i donne le numéro de l'élément blanc

    return "pas d'évènement" # si on a tiré toutes les blanches en premier


def tirage_boules_3(nb_boules_noires, nb_boules_blanches):
    urne = ['N'] * nb_boules_noires + ['B'] * nb_boules_blanches
    random.shuffle(urne)
    # print(urne)
    for i in range (len(urne)):
        if urne[i] == 'B':
            if 'N' in urne[0:i]:
                return i+1      # return i donne le numéro de l'élément blanc

    return "pas d'évènement" # si on a tiré toutes les blanches en premier


def proba(k,nb_boules_noires,nb_boules_blanches,N):
    '''
    Renvoie la probabilité d'obtenir k boules blanches après n tirages.
    La loi de probabilité est uniforme sur n+1 termes (de 0 à n inclus).
    La probabilité tend donc vers 1/(n+1)
    '''
    succes=0
    for i in range(N):
        num_boule = tirage_boules_2(nb_boules_noires, nb_boules_blanches)
        if k == num_boule:
            succes += 1
    return succes/N


# Paramètres de l'urne
nb_boules_noires = 6
nb_boules_blanches = 4

# Effectuer le tirage et calculer le nombre de boules nécessaires
nombre_boules_tirees = tirage_boules_2(nb_boules_noires, nb_boules_blanches)

# Afficher le résultat
print("Numéro de la boule blanche :", nombre_boules_tirees)
