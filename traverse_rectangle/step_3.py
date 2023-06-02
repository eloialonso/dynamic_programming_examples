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
        memo[(i, j)] = T[0, 0], None
        return memo[(i, j)]
    
    if i < 0 or j < 0:
        memo[(i, j)] = float('inf'), None
        return memo[(i, j)]
    
    # Recursion (Bellman)
    cost_right = c(T, i - 1, j, memo)[0]
    cost_down = c(T, i, j - 1, memo)[0]
    
    if cost_right < cost_down:
        memo[(i, j)] = (T[i, j] + cost_right, (i - 1, j))
    else:
        memo[(i, j)] = (T[i, j] + cost_down, (i, j - 1))

    return memo[(i, j)]


def backtracking(memo, i, j):
    path = []
    ij = (i, j)
    while ij is not None:
        path.append(ij)
        _, ij = memo[ij]
    path.reverse()    
    return np.array(path)
    

n = int(input("n = "))
p = int(input("p = "))
T = np.random.rand(n, p)

memo = {}
min_cost = c(T, n - 1, p - 1, memo)
path = backtracking(memo, n - 1, p - 1)

print(f"Minimal cost: {min_cost}")
plt.imshow(T, cmap='gray')
plt.plot(path[:, 1], path[:, 0], 'r-')
plt.colorbar()
plt.show()
