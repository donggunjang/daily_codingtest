# 1일 될때까지 문제 시간 복잡도 최소화 알고리즘

n, k = map(int, input().split())
result = 0

while True:
    #(N==K로 나누어 떨어지는 수)가 될때까지 1씩 빼기
    target = (n//k) * k
    result += (n - target)
    n = target
    #N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1 
    n = n // k

#남은 수에 대해 1씩 빼기 
result += (n - 1)
print(result)