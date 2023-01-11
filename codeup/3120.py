# 리모컨
import time
a, b = map(int, input().split())

cnt = 0
op_types = [10, 5, 1]
residual = abs(a - b)

while True:
    if residual == 0:
        break
    next_residuals = [abs(residual - op) for op in op_types]
    residual = min(next_residuals)
    cnt += 1
    
print(cnt)