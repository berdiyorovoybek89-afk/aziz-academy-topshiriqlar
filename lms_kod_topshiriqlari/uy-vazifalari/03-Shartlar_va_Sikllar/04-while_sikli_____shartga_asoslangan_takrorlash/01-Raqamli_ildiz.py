n = int(input())
while n >= 10:
    summa = 0
    while n > 0:
        summa += n % 10
        n //= 10
    n = summa 
print(n)