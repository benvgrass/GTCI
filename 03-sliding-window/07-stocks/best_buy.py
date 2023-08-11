def max_profit(stock_prices):
    profit_max = 0
    buy = 0

    for sell in range(1, len(stock_prices)):
        if stock_prices[sell] < stock_prices[buy]:
            buy = sell
        else:
            profit_max = max(profit_max, stock_prices[sell] - stock_prices[buy])

    return profit_max
