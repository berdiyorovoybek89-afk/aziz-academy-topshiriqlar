n = int(input())
i = 2
while i * i <= n and n % i:
    i += 1
print("ha" if i * i > n and n > 1 else "yo'q")