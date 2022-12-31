# 시간 복잡도를 최적화한 큰 수의 법칙
# M의 크기가 100억 이상처럼 커진다면 시간 복잡도가 기하급수적으로 커질 수 있다. 
# 따라서 간단한 수학적 아이디어를 이용해 효율적인 알고리즘을 생각해보자.

# 이 문제를 풀려면 먼저 반복되는 수열에 대해서 파악해야 한다.
# 가장 큰 수와 두 번째로 큰 수가 더해질 대는 특정한 수열 형태로 일정하게 반복해서 더해지는 특징이 있다.
# 이 문제에서는 큰수가 3번 두번째로 큰수가 1번 반복되는 형태 이기 때문에 수열의 길이는 (K+1)이 된다.
# 따라서 M을 (K+1)로 나눈 몫이 수열이 반복되는 횟수가 된다. 다시 여기에 K를 곱해주면 가장 큰 수가 등장하는 횟수가 된다.
# 이때 M이 (K+1)로 나누어 떨어지지 않는 경우도 고려해야 한다. 이땐 나눈 나머지만큼 가장 큰 수가 추가로 더해진다.

# 가장 큰 수가 더해지는 횟수는 다음과 같다. int((M // (K+1)) * K + M % (K+1)

# 문제 해답 알고리즘

n, m, k = map(int, input().split()) # N M K 를 공백을 기준으로 입력받기
data = list(map(int, input().split())) #N개의 수를 공백으로 구분하여 입력받기

data.sort() #입력받은 N개의 수를 정렬
first = data[n-1] #가장 큰 수
second = data[n-2] #두번째로 큰 수

#가장 큰 수가 더해지는 횟수 계산
count = int(m // (k+1)) * k 
count = m % (k+1)

result = 0
result += (count) * first #가장 큰 수 더하기
result += (m - count) * second #두 번째로 큰 수 더하기

print(result)