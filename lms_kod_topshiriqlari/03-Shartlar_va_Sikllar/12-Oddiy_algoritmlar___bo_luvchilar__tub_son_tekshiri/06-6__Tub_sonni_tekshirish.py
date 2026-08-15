# n beriladi.
# Agar n tub bo‘lsa "Prime", aks holda "Composite" chiqaring.
# (1 uchun ham Composite chiqaring)
n = int(input())
print("Prime" if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)) else "Composite")