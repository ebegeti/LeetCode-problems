def maxProfit( prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    buy = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        profit = prices[i] - buy

        if profit > max_profit:
            max_profit = profit

        if prices[i] < buy:
            buy = prices[i]

    return max_profit

print(maxProfit([2,4,1]))