# n va n ta son beriladi.
# Faqat musbat sonlarni oling.
# Ularni 2 ga ko‘paytiring.
# Natijaviy listni chiqaring.
n = int(input())
numbers = list(map(int, input().split()))
result = [x * 2 for x in numbers if x > 0]
print(result)