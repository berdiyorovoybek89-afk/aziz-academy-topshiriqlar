soat, stavka, soliq = int(input()), int(input()), int(input())
yalpi = soat * stavka
soliq_summa = yalpi * soliq // 100
print(yalpi, soliq_summa, yalpi - soliq_summa, sep="\n")