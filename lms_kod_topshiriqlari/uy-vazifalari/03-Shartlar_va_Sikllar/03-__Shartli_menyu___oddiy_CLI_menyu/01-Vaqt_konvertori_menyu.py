m = input()
if m in ("1", "2"):
    n = int(input())
    a, b = n // 60, n % 60
    print(f"{a} minut {b} soniya" if m == "1" else f"{a} soat {b} minut")
else:
    print("Notogri tanlov")