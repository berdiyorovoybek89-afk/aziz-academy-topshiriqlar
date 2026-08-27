# O'rtacha masofasi
# Kurs: Dasturlash / IT
# Mavzu: Dasturlashga kirish — Python nima va nega o'rganamiz
# Ball: 100
# Aziz Academy — AI Topshiriq

# Yechimingizni shu yerga yozing
# Kirish: input(), chiqish: print()
a = []
for _ in range(5):
    a.append(int(input()))
a.sort()
print(sum(a[1:4]) // 3)