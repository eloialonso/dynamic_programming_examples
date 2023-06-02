
def c(k, s, memo):

    # "Protection"
    if (k, s) in memo:
        return memo[(k, s)]
    
    # 2 base cases (problem specific)
    if s == 0:
        memo[(k, s)] = (0, 0)
        return memo[(k, s)]

    if k == 0:
        memo[(k, s)] = float('inf'), None
        return memo[(k, s)]
    
    # Recursion (Bellman)
    coin = coins[k - 1]
    l = [x + c(k - 1, s - x * coin, memo)[0] for x in range(1 + s // coin)]
    m = min(l)
    i = l.index(m)
    memo[(k, s)] = (m, i)
    
    return memo[(k, s)]


def reconstruct_minimizer(memo, s, coins):
    change = []
    k = len(coins)
    while s != 0:
        _, n = memo[(k, s)]
        change.extend([coins[k - 1]] * n)
        s -= n * coins[k - 1]
        k -= 1   
    return change[::-1]


s = int(input('Enter a number: '))
coins = [200, 100, 50, 20, 10, 5, 2, 1]

memo = {}
min_number_coins = c(len(coins), s, memo)[0]
change = reconstruct_minimizer(memo, s, coins)

assert sum(change) == s
print(f'{min_number_coins} coins are necessary: {s} = {" + ".join(map(str, change))}')