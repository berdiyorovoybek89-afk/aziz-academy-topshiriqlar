# n beriladi.
# n dan kichik bo‘lgan eng katta bo‘luvchini toping.
# Agar yo‘q bo‘lsa, 0 chiqaring.
n = int(input())
ans = 0
for i in range(n - 1, 0, -1):
    if n % i == 0:
        ans = i
        break
print(ans)