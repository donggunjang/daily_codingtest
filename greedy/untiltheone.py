# 1이 될때 까지

# 어떠한 수 N이 1이 될때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
# 단, 두 번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.
'''
1. N에서 1을 뺀다.
2. N을 K로 나눈다.
'''


#공백으로 구분하여 N,K 입력 받기
n, k = map(int, input().split())

result = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k:
    #N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    #K로 나누기
    n = n // k
    result += 1

#마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1
print(result)