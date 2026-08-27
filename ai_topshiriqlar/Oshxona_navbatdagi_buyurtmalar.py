# Oshxona: navbatdagi buyurtmalar
# Kurs: Dasturlash / IT
# Mavzu: Dasturlashga kirish — Python nima va nega o'rganamiz
# Ball: 100
# Aziz Academy — AI Topshiriq

import sys
data = sys.stdin.read().split()
if data:
    n = int(data[0])
    orders = [int(x) for x in data[1 : n + 1]]
    accepted = 0
    total = 0
    for x in orders:
        if total + x > 50000:
            break
        total += x
        accepted += 1
    print(accepted)
    print(total)
    print(n - accepted)