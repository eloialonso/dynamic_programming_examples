
def c(k, s):

    # 2 base cases (problem specific)
    if s == 0:
        return 0

    if k == 0:
        return float('inf')
    
    # Recursion (Bellman)
    coin = coins[k - 1]
    m = min([x + c(k - 1, s - x * coin) for x in range(1 + s // coin)])
    
    return m

s = int(input('Enter a number: '))
coins = [200, 100, 50, 20, 10, 5, 2, 1]

min_number_coins = c(len(coins), s)

print(f'{min_number_coins} coins are necessary to make {s} with coins {coins}')