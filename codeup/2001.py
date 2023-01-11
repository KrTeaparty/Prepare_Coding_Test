# 최소 대금
pizza_prices = []
juice_prices = []
for _ in range(3):
    pizza_prices.append(int(input()))
for _ in range(2):
    juice_prices.append(int(input()))

pizza_prices.sort()
juice_prices.sort()

print(round((pizza_prices[0] + juice_prices[0]) * 1.1, 1))
