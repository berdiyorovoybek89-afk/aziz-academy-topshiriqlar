n = int(input())
yigindi = sum(i for i in range(1, n + 1) if n % i == 0)
print(yigindi)