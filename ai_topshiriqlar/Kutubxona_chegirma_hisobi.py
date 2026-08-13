# Kutubxona: chegirma hisobi
# Kurs: Dasturlash / IT
# Mavzu: O'rnatish va muhit — Python, interpreter, IDE sozlash
# Ball: 100
# Aziz Academy — AI Topshiriq

# Yechimingizni shu yerga yozing
# Kirish: input(), chiqish: print()
price1 = int(input())
price2 = int(input())
total = price1 + price2
discounted = total * 0.8
if discounted < 100000:
    discounted += 5000
print(int(discounted))