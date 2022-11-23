import numpy as np
#création d'un tableau aléatoire
grille = np.random.randint(0,10, size=(9,9))
#vérification sur les lignes et les colonnes
def check_row (grille):
    x = grille[:,0]
    y = grille[0,:]
# verification dans les lignes et colonnes   
    if len(set(x)) ==  len(x) and len(set(y)) == len(y) :
        return True
    else :
        return False

# teste sur ma matrice

check_row(grille)