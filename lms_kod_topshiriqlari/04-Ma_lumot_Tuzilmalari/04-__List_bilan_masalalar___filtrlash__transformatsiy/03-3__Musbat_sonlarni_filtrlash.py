# n va n ta son beriladi.
# Faqat musbat sonlarni chiqaring.
n = int(input())
sonlar = list(map(int, input().split()))
musbatlar = [x for x in sonlar if x > 0]
print(musbatlar)