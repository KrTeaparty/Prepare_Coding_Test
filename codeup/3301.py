# 거스름돈
n = int(input())

money = [50000, 10000, 5000, 1000, 500, 100,50, 10]
cnt = 0

for i in money:
    cnt += n // i
    n %= i

print(cnt)