def dist(a, b, i, j, memo):

    # "Protection"
    if (i, j) in memo:
        return memo[(i, j)]
    
    # 2 base cases (problem specific)
    if i == 0:
        memo[(i, j)] = j
        return memo[(i, j)]
    
    if j == 0:
        memo[(i, j)] = i
        return memo[(i, j)]
    
    # Recursion (Bellman)
    memo[(i, j)] = min(
        dist(a, b, i - 1, j - 1, memo) + int(a[i - 1] != b[j - 1]),
        dist(a, b, i - 1, j, memo) + 1,
        dist(a, b, i, j - 1, memo) + 1
    )

    return memo[(i, j)]


a = input('Enter a word: ')
b = input('Enter another word: ')

memo = {}
d = dist(a, b, len(a), len(b), memo)

print(f'Levenshtein("{a}", "{b}") = {d}')
