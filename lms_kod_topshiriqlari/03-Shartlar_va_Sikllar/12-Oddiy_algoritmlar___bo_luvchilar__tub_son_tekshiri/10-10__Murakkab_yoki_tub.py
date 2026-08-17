# n beriladi.
# Agar n tub bo‘lsa "Prime", aks holda "Not Prime" chiqaring.
import math
n = int(input())
print("Not Prime" if n < 2 or any(n % i == 0 for i in range(2, math.isqrt(n) + 1))else "Prime")