import math
import sys

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

n = list(map(int, input().split()))
for i in n:
    print(f"{is_prime_number(i)}", end=' ')