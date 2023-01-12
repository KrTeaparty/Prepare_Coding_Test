# 최고의 피자
n = int(input())
price_d, price_t = map(int, input().split())
calories_d = int(input())

calories_t = []
for _ in range(n):
    calories_t.append(int(input()))

calories_t.sort(reverse=True)

price_p = price_d
calories_p = calories_d
best_pizza = calories_d // price_d

# 지금까지의 1달러 당 열량이 토핑의 1달러 당 열량보다 낮으면 토핑 추가
for t in calories_t:
    if best_pizza < (t//price_t):
        price_p += price_t
        calories_p += t
        best_pizza = calories_p // price_p
    else:
        break

print(best_pizza)