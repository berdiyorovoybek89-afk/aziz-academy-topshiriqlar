# n va n ta so‘z beriladi.
# Uzunligi 3 dan katta bo‘lgan so‘zlarni list qilib chiqaring.
n = int(input())
words = input().split()
result = [w for w in words if len(w) >= n]
print(result)