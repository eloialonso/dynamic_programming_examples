
def c(k, s, memo):

    # "Protection"
    if (k, s) in memo:
        return memo[(k, s)]
    
    # 2 base cases (problem specific)
    if s == 0:
        memo[(k, s)] = 0
        return memo[(k, s)]

    if k == 0:
        memo[(k, s)] = float('inf')
        return memo[(k, s)]
    
    # Recursion (Bellman)
    coin = coins[k - 1]
    m = min([x + c(k - 1, s - x * coin, memo) for x in range(1 + s // coin)])
    memo[(k, s)] = m
    
    return memo[(k, s)]


s = int(input('Enter a number: '))
coins = [200, 100, 50, 20, 10, 5, 2, 1]

memo = {}
min_number_coins = c(len(coins), s, memo)

print(f'{min_number_coins} coins are necessary to make {s} with coins {coins}')