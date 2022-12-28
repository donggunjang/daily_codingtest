# 거스름돈 문제 풀이
# 거스름돈으로 사용할 500원, 100원, 10원짜리 동전이 무한히 존재한다고 가정
# 거슬러 줘야 할 돈이 N원일 때, 거슬러 줘야할 동전의 최소 개수를 구하라. 
# 단 거슬러 줘야 할 돈 N은 항상 10의 배수이다.

#아이디어 "가장 큰 화폐 단위부터" 돈을 거슬러 주는 것

n = int(input())
count = 0
#큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

#동전의 개수 세기
for coin in coin_types:
    count += n // coin
    n %= coin

print(count)