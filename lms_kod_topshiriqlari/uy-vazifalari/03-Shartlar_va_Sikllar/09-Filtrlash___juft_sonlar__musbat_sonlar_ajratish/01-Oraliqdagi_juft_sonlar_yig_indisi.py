a = int(input())
b = int(input())
juft_yigindi = 0
for son in range(a, b + 1):
    if son % 2 == 0:
        juft_yigindi += son
print(juft_yigindi)