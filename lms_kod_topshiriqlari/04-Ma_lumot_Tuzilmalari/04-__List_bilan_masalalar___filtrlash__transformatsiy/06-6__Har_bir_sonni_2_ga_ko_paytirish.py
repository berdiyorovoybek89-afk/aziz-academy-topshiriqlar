# n va n ta son beriladi.
# Har bir sonni 2 ga ko‘paytirib yangi list chiqaring.
n = int(input())
numbers = list(map(int, input().split()))
result = [x * 2 for x in numbers]
print(result)