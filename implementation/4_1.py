#상하좌우 문제

'''
여행가 A는 N X M 크기의 정사각형 공간 위에 서 있다.
이공간은 1 X 1 크기의 정사각형으로 나누어져 있다. 가장 왼쪽 위 좦는 (1,1)이며, 가장 오른쪽 아래 좌표는 (N,N)에 해당한다.
여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1,1)이다. 우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여 있다.

계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L,R,U,D 중 하나의 문자가 반복적으로 적혀 있다.
L: 왼쪾으로 한칸 이동
R: 오른쪽으로 한칸 이동
U: 위로 한칸 이동
D: 아래로 한칸 이동

계획서가 주어졌을 때 여행가 A가 최종적으로 도찰할 지점의 좌표를 출력하는 프로그램을 작성하시오.
 '''

n = int(input())
x,y = 1,1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L', 'R', 'U', 'D']

#이동 계획을 하나씩 확인
for plan in plans:
    #이동후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    #공간을 벗아나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    #이동수행
    x,y = nx, ny

print(x, y)  
