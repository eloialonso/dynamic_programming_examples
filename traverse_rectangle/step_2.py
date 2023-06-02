"""
Rappel des étapes : 

1) Coder la récursion (Bellman) sans chercher à mémoïser ni à faire le backtracking (on cherche le min, pas l'argmin).
Cela nécessite probablement de réduire la taille du problème (taille de la matrice ici).

2) Mémoïser, et vérifier que cela permet de résoudre des problèmes plus gros.

3) Faire le backtracking : sans toucher la récurrence, il suffit de stocker l'état d'avant dans le memo, afin de pouvoir reconstituer le chemin optimal une fois qu'on a fini.

"""


import matplotlib.pyplot as plt
import numpy as np


def c(T, i, j, memo):

    # "Protection"
    if (i, j) in memo:
        return memo[(i, j)]
        
    # 2 base cases (problem specific)
    if i == j == 0:
        memo[(i, j)] = T[0, 0]
        return memo[(i, j)]
    
    if i < 0 or j < 0:
        memo[(i, j)] = float('inf')
        return memo[(i, j)]
    
    # Recursion (Bellman)
    memo[(i, j)] = T[i, j] + min(c(T, i - 1, j, memo), c(T, i, j - 1, memo))

    return memo[(i, j)]

n = int(input("n = "))
p = int(input("p = "))
T = np.random.rand(n, p)

min_cost = c(T, n - 1, p - 1, memo={})

print(f"Minimal cost: {min_cost}")
plt.imshow(T, cmap='gray')
plt.colorbar()
plt.show()
