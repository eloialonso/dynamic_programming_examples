def dist(a, b, i, j):

    # 2 base cases (problem specific)
    if i == 0:
        return j
    
    if j == 0:
        return i
    
    # Recursion (Bellman)
    return min(
        dist(a, b, i - 1, j - 1) + int(a[i - 1] != b[j - 1]),
        dist(a, b, i - 1, j) + 1,
        dist(a, b, i, j - 1) + 1
    )


a = input('Enter a word: ')
b = input('Enter another word: ')

d = dist(a, b, len(a), len(b))

print(f'Levenshtein("{a}", "{b}") = {d}')
