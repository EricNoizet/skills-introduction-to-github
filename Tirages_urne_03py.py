# La fonction tirages_sans_remise effectue des tirages sans remise dans une urne contenant un certain nombre de boules noires et un certain nombre de boules blanches. Elle compte le nombre de boules noires tirées consécutivement jusqu'à ce qu'une boule blanche soit tirée, puis renvoie le nombre de boules noires tirées.
# test deux

## import des bibliothèques
import random
import numpy as np

def tirages_sans_remise(nb_boules_noires, nb_boules_blanches):
    """
    Effectue des tirages sans remise dans une urne jusqu'à obtenir une boule blanche.
    Argument :
    nb_boules_noires -- nombre de boules noires
    nb_boules_blanches -- nombre de boules blanches

    Retour :
    nb_noires -- nombre de boules noires tirées avant la première boule blanche
    """

    urne = ['N'] * nb_boules_noires + ['B'] * nb_boules_blanches
    random.shuffle(urne)

    nb_noires = 0

    for i in range (len(urne)):
        if urne[i] == 'N' :
            nb_noires+=1
        else :
            return nb_noires


def tirages_sans_remise_3(nb_boules_noires, nb_boules_blanches):
    """
    C'est de la triche !
    """
    urne = ['N'] * nb_boules_noires + ['B'] * nb_boules_blanches
    random.shuffle(urne)
    nb_noires = urne.index('B')
    return nb_noires



def tirages_sans_remise_2(nb_boules_noires, nb_boules_blanches):
    """
    Effectue des tirages sans remise dans une urne jusqu'à obtenir une boule blanche.
    Argument :
    nb_boules_noires -- nombre de boules noires
    nb_boules_blanches -- nombre de boules blanches

    Retour :
    nb_noires -- nombre de boules noires tirées avant la première boule blanche

    Ici, pas de fonction random.shuffle autorisée
    """

    urne = ['N'] * nb_boules_noires + ['B'] * nb_boules_blanches

    nb_noires = 0
    while len(urne)>0:
        numero = np.random.randint(len(urne))
        boule_tiree = urne[numero]
        if boule_tiree == 'B':
            return nb_noires
        else:
            urne.pop(numero)
            nb_noires += 1


# Paramètres de l'urne
nb_boules_noires = 6
nb_boules_blanches = 4

# Effectuer le tirage et calculer le nombre de boules nécessaires
nombre_boules_noires_tirees = tirages_sans_remise_2(nb_boules_noires, nb_boules_blanches)

# Afficher le résultat
print("Nombre de boules noires tirées :", nombre_boules_noires_tirees)
