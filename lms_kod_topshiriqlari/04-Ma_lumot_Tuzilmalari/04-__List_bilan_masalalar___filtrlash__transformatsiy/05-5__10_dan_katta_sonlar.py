# n va n ta son beriladi.
# Faqat 10 dan katta sonlarni chiqaring.
n = int(input())
numbers = list(map(int, input().split()))
result = [x for x in numbers if x > 10]
print(result)