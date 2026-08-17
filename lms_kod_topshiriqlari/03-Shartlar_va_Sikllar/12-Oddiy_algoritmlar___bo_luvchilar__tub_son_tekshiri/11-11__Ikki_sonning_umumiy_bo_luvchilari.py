# a va b beriladi.
# Ikkala sonning umumiy bo‘luvchilarini chiqar.
import math
a, b = map(int, input().split())
for i in range(1, math.gcd(a, b) + 1):
    if a % i == 0 and b % i == 0:
        print(i)