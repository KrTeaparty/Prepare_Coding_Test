n, m = map(int, input().split())

schedule = []
for _ in range(n):
    schedule.append(input())

s, t = map(int, input().split())

cnt = 0
tmp = -1
prev = []

for i in range(s-1, t-1):
    index = []

    while True:
        tmp = schedule[i].find('O', tmp+1)
        if tmp == -1:
            break
        index.append(tmp)

    if index == []:
        cnt = -1
        break
    
    if i == s-1:
        prev = index
    else:
        # 전날과 오늘의 가능한 방의 교집합이 있다면 방을 바꾸지 않아도 된다.
        if set(prev).intersection(index):
            # 해당 방에서 하루를 묵었으니 prev를 교집합으로 업데이트한다.
            prev = set(prev).intersection(index)
        else:
            # 교집합이 없다면 묵었던 방을 이어서 예약할 수 없으니 방을 바꾼 것으로 판정한다.
            cnt += 1
            prev = index

print(cnt)