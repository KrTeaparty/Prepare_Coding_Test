# 생년월일 출력
front, back = input().split('-')

if back[0] in ['1', '2']:
    year = '19'
else:
    year = '20'

year += front[0:2]
month = front[2:4]
day = front[4:]
if int(back[0]) % 2 == 0:
    gender = 'F'
else: 
    gender = 'M'

print(year,'/',month,'/',day,' ', gender, sep='')