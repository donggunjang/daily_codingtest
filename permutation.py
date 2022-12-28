#순열(permutation)이란?
#서로다른 n개에서 r개를 선택하여 일렬로 나열하는 것
#nPr = n! / (n-r)!
#파이썬 라이브러리 itertools 이용

import itertools

data = [1,2,3,4]
print("순열")
for x in itertools.permutations(data, 2):
    print(list(x))

#조합(combination)이란?
#서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 선택하는 것
#nCr = n! / r! * (n-r)! 이다

data2 = [1,2,3]
print("조합")
for i in itertools.combinations(data2, 2):
    print(list(i))