n = int(input())
s = 0
while n:
    a = int(input())
    if a <= 0:
        n -= 1
        continue
    s += a
    n -= 1
print(s)