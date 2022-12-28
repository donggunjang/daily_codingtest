import math
import sys

m, n= map(int, input().split())
array = [True for i in range(1000001)]
array[1] = 0 #1은 소수가 아님

#에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n))+1):
    if array[i] == True: #소수일 경우
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

# M부터 N까지의 소수 구하기
for i in range(m, n+1):
    if array[i]:
        print(i)