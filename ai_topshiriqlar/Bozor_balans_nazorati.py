# Bozor: balans nazorati
# Kurs: Dasturlash / IT
# Mavzu: Dasturlashga kirish — Python nima va nega o'rganamiz
# Ball: 100
# Aziz Academy — AI Topshiriq

# Yechimingizni shu yerga yozing
# Kirish: input(), chiqish: print()
import sys
data = sys.stdin.read().split()
if data:
    n = int(data[0])
    ops = data[1 : n + 1]
    balance = 200000
    min_balance = balance
    expenses_count = 0
    for op in ops:
        val = int(op)
        balance += val
        if val < 0:
            expenses_count += 1
        if balance < min_balance:
            min_balance = balance
    print(balance)
    print(min_balance)
    print(expenses_count)