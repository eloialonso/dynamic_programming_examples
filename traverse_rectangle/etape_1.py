"""
Rappel des étapes : 

1) Coder la récursion (Bellman) sans chercher à mémoïser ni à faire le backtracking (on cherche le min, pas l'argmin).
Cela nécessite probablement de réduire la taille du problème (taille de la matrice ici).

2) Faire le backtracking : sans toucher la récurrence, il suffit de stocker l'état d'avant dans le memo, afin de pouvoir reconstituer le chemin optimal une fois qu'on a fini.

3) Mémoïser, et vérifier que cela permet de résoudre des problèmes plus gros.

"""


import matplotlib.pyplot as plt
import numpy as np


def c(T, i, j):

    # 2 cas d'arrêts (spécifiques à ce problème), qu'on peut mémoiser aussi
    if i == j == 0:
        return T[0, 0]
    
    if i < 0 or j < 0:
        return float('inf')
    
    # Récursion
    return T[i, j] + min(c(T, i - 1, j), c(T, i, j - 1))

n = int(input("n = "))
p = int(input("p = "))
T = np.random.rand(n, p)

min_cost = c(T, n - 1, p - 1)

print(f"Coût minimal: {min_cost}")
plt.imshow(T, cmap='gray')
plt.colorbar()
plt.show()
