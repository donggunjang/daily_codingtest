# 큰 수의 법칙

# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
# 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.

# 예를 들어 순서대로 2,4,5,4,6 이루어진 배열이 있을 때 M이 8이고, K가 3이라 가정 
# 이경우 특정한 인덱스의 수가 연속해서 세 번까지만 더해질 수 있으므로 큰 수의 법칙의 따라 
# 6+6+6+5+6+6+6+5 인 46이 된다.
# 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주한다.

#문제 풀이

#N,M,K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

#N개의 자연수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k): #가장큰수를 k번 더하기
        if m == 0: #m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1 #더할 대마다 1씩 빼기
    if m == 0: #m이 0이라면 반복문 탈출
        break
    result += second
    m -= 1

print(result)