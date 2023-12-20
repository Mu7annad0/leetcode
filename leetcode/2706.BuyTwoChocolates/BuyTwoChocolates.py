def buyChoco(prices, money):
    prices.sort()
    if prices[0] + prices[1] > money:
        return money
    else:
        return money - (prices[0] + prices[1])


if __name__ == "__main__":
    prices = [3, 2, 2]
    money = 3

    print(buyChoco(prices, money))
