# n beriladi.
# 1 dan n gacha bo‘lgan tub sonlar sonini hisoblang.
n = int(input())
print(sum(all(i % j != 0 for j in range(2, int(i**0.5) + 1)) for i in range(2, n + 1)))