# une urne, avec une boule blanche (1) et une rouge (0)
# on tire une boule au hasard, on regarde sa couleur, on la remet dans l'urne, et on ajoute une boule de la même couleur
# Xn (n entier > 0) : on compte le nombre de boules blanches tirées au bout de n tirs
#  Au pire, Xn vaut 0 (on n'a jamais tiré de blanche)
#  Au mieux, Xn vaut n (on n'a tiré que des blanches)
# Pour une urne fixée, le nombre de blanches tirées vaut sum(urne)-1
#  (on doit retirer la blanche initiale)
# La proba d'obtenir k entre 0 et N vaut 1/(n+1) (car loi uniforme : c'est ce qu'on vérifie)

## import des bibliothèques
import numpy as np

## fonctions utiles
def tirage(L):
    '''
    Choisit une position au hasard dans la liste L et renvoie l'élément associé.
    '''
    alea = np.random.randint(0,len(L))
    return L[alea]

def completer(L):
    '''
    Tire un élément au hasard dans la liste L, et l'ajoute en bout de liste.
    Renvoie ensuite la liste.
    '''
    tir = tirage(L)
    L.append(tir)
    return L

def nombre_tirages_blancs(L,n):
    '''
    Fais n tirages, et renvoie le nombre de boules balnches tirées : c'est Xn.
    Pour une urne fixée, le nombre de blanches tirées vaut sum(urne)-1
    (on doit retirer la blanche initiale)
    '''
    for i in range(n):
        completer(L)
    return sum(L)-1

def proba(L,k,n,N):
    '''
    Renvoie la probabilité d'obtenir k boules blanches après n tirages.
    La loi de probabilité est uniforme sur n+1 termes (de 0 à n inclus).
    La probabilité tend donc vers 1/(n+1)
    '''
    succes=0
    for i in range(N):
        Ttravail=L.copy() # il faut faire une copie de L (urne), sinon urne est modifiée
        n_tirages = nombre_tirages_blancs(Ttravail,n)
        if k == n_tirages:
            succes += 1
    return succes/N

## programme
urne = [0,1]

# on fait n tirs. Chaque proba doit tendre vers 1/(n+1).
n=4
N=100000
Liste_probabilités=[]

for i in range(n+1):
    Liste_probabilités.append(proba(urne,i,n,N))
print(Liste_probabilités)