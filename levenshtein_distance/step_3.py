def dist(a, b, i, j, memo):

    # "Protection"
    if (i, j) in memo:
        return memo[(i, j)]
    
    # 2 base cases (problem specific)
    if i == 0:
        memo[(i, j)] = j, (i, j - 1)
        return memo[(i, j)]
    
    if j == 0:
        memo[(i, j)] = i, (i - 1, j)
        return memo[(i, j)]
    
    # Recursion (Bellman)
    l = [
        dist(a, b, i - 1, j - 1, memo)[0] + int(a[i - 1] != b[j - 1]),
        dist(a, b, i - 1, j, memo)[0] + 1,
        dist(a, b, i, j - 1, memo)[0] + 1,
    ]
    m = min(l)
    idx = l.index(m)
    if idx == 0:
        memo[(i, j)] = m, (i - 1, j - 1)
    elif idx == 1:
        memo[(i, j)] = m, (i - 1, j)
    else:
        memo[(i, j)] = m, (i, j - 1)

    return memo[(i, j)]


def reconstruct_minimizer(memo, a, b):
    i, j = (len(a), len(b))
    align_a, align_b = '', ''
    while (i, j) != (0, 0):
        _, (new_i, new_j) = memo[(i, j)]
        align_a += a[new_i:i] if new_i < i else '_'
        align_b += b[new_j:j] if new_j < j else '_'
        i, j = new_i, new_j
    return align_a[::-1] + '\n' + align_b[::-1]


a = input('Enter a word: ')
b = input('Enter another word: ')

memo = {}
d = dist(a, b, len(a), len(b), memo)[0]
alignment = reconstruct_minimizer(memo, a, b)

print(f'Levenshtein("{a}", "{b}") = {d}')
print('Alignment:')
print(alignment)
