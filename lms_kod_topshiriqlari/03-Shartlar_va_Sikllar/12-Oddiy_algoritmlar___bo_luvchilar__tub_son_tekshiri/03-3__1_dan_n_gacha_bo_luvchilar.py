# n beriladi.
# 1 dan n gacha bo‘lgan bo‘luvchilarni chiqaring.
n = int(input())
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
    