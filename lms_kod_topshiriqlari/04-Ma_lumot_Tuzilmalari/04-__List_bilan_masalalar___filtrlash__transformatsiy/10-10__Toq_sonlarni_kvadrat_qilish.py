# n va n ta son beriladi.
# Faqat toq sonlarni olib, kvadratidan iborat list chiqaring.
n = int(input())
numbers = list(map(int, input().split()))
result = [x ** 2 for x in numbers if x % 2 != 0]
print(result)