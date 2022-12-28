import math

n = 5
data = [10, 20, 30, 40, 50]

#접두사 합(prefix Sum) 배열 계산
sum_value = 0 
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

#구간합 구하기
L = int(input())
R = int(input())
print(prefix_sum[R] - prefix_sum[L-1])