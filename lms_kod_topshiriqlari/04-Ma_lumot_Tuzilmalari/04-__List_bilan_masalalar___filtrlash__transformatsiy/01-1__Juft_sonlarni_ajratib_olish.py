# n va n ta son beriladi.
# Faqat juft sonlardan iborat yangi list chiqaring.
n = int(input())
sonlar = list(map(int, input().split()))
juftlar = [x for x in sonlar if x % 2 == 0]
print(juftlar)