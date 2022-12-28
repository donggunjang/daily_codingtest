import math

n = int(input())

array = [True for i in range(n+1)]

#에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n)+1)): #2부터 n의 젝곱근까지의 무든 수를 확인
    if array[i] == True: # i가 소수인 경우(남은 수인 경우)
        # i를 제외한 i의 배수들 모두 지우기
        j = 2
        while i * j <= n:
            array[i*j] = False
            j += 1
    #모든 소수를 출력        
    for  i in range(2, n+1):
        if array[i]:
            print(i, end=' ')

