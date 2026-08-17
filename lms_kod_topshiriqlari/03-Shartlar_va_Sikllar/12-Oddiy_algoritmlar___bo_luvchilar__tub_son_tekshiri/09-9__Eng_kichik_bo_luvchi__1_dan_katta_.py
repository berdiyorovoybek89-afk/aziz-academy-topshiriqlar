# n beriladi.
# 1 dan katta eng kichik bo‘luvchini toping.
# Agar bo‘lmasa (n=1), 0 chiqaring.n
n = int(input())
if n <= 1:
    print(0)
else:
    for i in range(2, n + 1):
        if n % i == 0:
            print(i)
            break