import matplotlib.pyplot as plt
import numpy as np


def c(T, i, j):

    # 2 base cases (problem specific)
    if i == j == 0:
        return T[0, 0]
    
    if i < 0 or j < 0:
        return float('inf')
    
    # Recursion (Bellman)
    return T[i, j] + min(c(T, i - 1, j), c(T, i, j - 1))

n = int(input("n = "))
p = int(input("p = "))
T = np.random.rand(n, p)

min_cost = c(T, n - 1, p - 1)

print(f"Minimal cost: {min_cost}")
plt.imshow(T, cmap='gray')
plt.colorbar()
plt.show()
