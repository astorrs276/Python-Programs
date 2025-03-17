def solve(prices):
    if not prices:
        return 0

    n = len(prices)
    hold = [0] * n
    sell = [0] * n
    rest = [0] * n
        
    hold[0] = -prices[0]
        
    for i in range(1, n):
        hold[i] = max(hold[i-1], (rest[i-1] if i > 1 else 0) - prices[i])
        sell[i] = hold[i-1] + prices[i]
        rest[i] = max(rest[i-1], sell[i-1])
        
    return max(sell[-1], rest[-1])