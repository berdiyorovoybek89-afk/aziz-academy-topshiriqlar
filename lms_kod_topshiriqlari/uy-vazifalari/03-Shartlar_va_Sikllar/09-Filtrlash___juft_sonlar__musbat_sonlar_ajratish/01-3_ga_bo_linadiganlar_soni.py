n = int(input())
c = 0
for _ in range(n):
    x = int(input())
    if x % 3 == 0:
        c += 1
print(c)