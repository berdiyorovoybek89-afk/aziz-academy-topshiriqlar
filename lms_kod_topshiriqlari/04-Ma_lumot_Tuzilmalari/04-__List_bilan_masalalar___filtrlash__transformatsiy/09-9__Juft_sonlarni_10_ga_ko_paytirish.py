# n va n ta son beriladi.
# Faqat juft sonlarni olib, ularni 10 ga ko‘paytirib list chiqaring.
n = int(input())
numbers = list(map(int, input().split()))
result = [x * 10 for x in numbers if x % 2 == 0]
print(result)