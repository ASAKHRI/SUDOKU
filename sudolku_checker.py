import numpy as np

grille = np.random.randint(1,9, size=(9,9))
grille

grille_v = np.array([[1,5,7,4,6,9,8,3,2],[3,9,6,2,1,8,7,4,5],[2,8,4,7,5,3,1,9,6],[6,7,2,5,3,1,9,8,4],[5,4,9,8,2,7,6,1,3],[8,3,1,6,4,9,2,5,7],[4,1,5,9,6,2,3,7,8],[7,6,3,1,8,5,4,2,9],[9,2,8,3,7,4,6,5,1]])
grille_v

def verif (grid) :
    
    for i in range (9) : 
        x = grid[i,:]
        y = grid[:,i]
        X = (i//3)*3
        Y = (i//3)*3
        if len(set(x)) != 9 or len(set(y)) != 9 or len(set(grid[X:X+3, Y:Y+3].ravel())) != 9 :  
            return False 
        return True  
    


verif(grille_v)