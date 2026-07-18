n = int(input())
musbat_soni = 0
manfiy_soni = 0
for _ in range(n):
    son = int(input())
    if son > 0:
        musbat_soni += 1
    elif son < 0:
        manfiy_soni += 1
print(musbat_soni, manfiy_soni)