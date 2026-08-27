# Davomiylikni hisoblash
# Kurs: Dasturlash / IT
# Mavzu: Dasturlashga kirish — Python nima va nega o'rganamiz
# Ball: 100
# Aziz Academy — AI Topshiriq

# Yechimingizni shu yerga yozing
# Kirish: input(), chiqish: print()
h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())
total_minutes = (h2 * 60 + m2) - (h1 * 60 + m1)
hours = total_minutes // 60
minutes = total_minutes % 60
print(hours)
print(minutes)