def profit(prices):
    min_price = float("inf")
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price

        max_profit = max(max_profit, price - min_price)
    return max_profit

print("Max profit: ",profit([7, 1, 5, 3, 6, 4]))
