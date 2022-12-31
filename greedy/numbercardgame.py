# 숫자 카드 게임
# 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임이다.
# 1. 카드들이 N X M 형태로 놓여 있다. N은 행의 개수, M은 열의 개수를 의미
# 2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
# 3. 그다음 선태된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
# 4. 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후헤 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을
#    고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.

# 카드들이 M X N 형태로 놓여 있을 때, 게임의 룰에 맞게 카드를 뽑는 프로그램을 만드시오.
# 문제 풀이
# 각 행마다 가장 작은 수를 찾은후 그중 가장 큰수를 찾는다.

#문제 풀이 알고리즘

#공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력 받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    #현재 줄에서 가장 작은 수 찾기
    min_value = min(data)
    #가장 작은 수 들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)