def max_profit(prices):
    if not prices:
        return 0

    n = len(prices)
    left_profits = [0] * n
    right_profits = [0] * n

    min_price = prices[0]
    for i in range(1, n):
        min_price = min(min_price, prices[i])
        left_profits[i] = max(left_profits[i - 1], prices[i] - min_price)

    max_price = prices[-1]
    for i in range(n - 2, -1, -1):
        max_price = max(max_price, prices[i])
        right_profits[i] = max(right_profits[i + 1], max_price - prices[i])

    max_profit = 0
    for i in range(n):
        max_profit = max(max_profit, left_profits[i] + right_profits[i])

    return max_profit

print(max_profit([3, 3, 5, 0, 0, 3, 1, 4]))
print(max_profit([1, 2, 3, 4, 5]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([1, 2, 4, 2, 5, 7, 2, 4, 9, 0]))
print(max_profit([3, 2, 6, 5, 0, 3]))