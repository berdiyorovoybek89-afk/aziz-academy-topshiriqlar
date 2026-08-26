# n va n ta son beriladi.
# Faqat toq sonlardan iborat list chiqaring.
n = int(input())
sonlar = list(map(int, input().split()))
toqlar = [x for x in sonlar if x % 2 != 0]
print(toqlar)