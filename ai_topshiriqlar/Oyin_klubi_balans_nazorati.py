# O'yin klubi: balans nazorati
# Kurs: Dasturlash / IT
# Mavzu: Dasturlashga kirish — Python nima va nega o'rganamiz
# Ball: 100
# Aziz Academy — AI Topshiriq

b = 500000
m = b
c = 0
for _ i in range(int(input())):
    x = int(input())
    b += x
    if b < m:
        m = b
        if x < 0:
            c += 1
print(b)
print(m)
print(c)